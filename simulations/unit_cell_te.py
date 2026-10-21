"""One-layer, 1D, lossless dielectric TE RCWA for the graduate course.

Lengths are micrometers. exp(-i omega t), Ey polarization, incidence from z<0.
The centered ridge occupies |x| < width/2 and 0 < z < height.
r is referenced to z=0; t to z=height. This is not a TM/2D-lattice solver.
"""
from dataclasses import dataclass, asdict
import numpy as np
from scipy.linalg import eigh, solve

SOLVER_VERSION = "te-ridge-1.0"


@dataclass(frozen=True)
class Cell:
    period_um: float = 0.65
    width_um: float = 0.325
    height_um: float = 0.60
    wavelength_um: float = 1.55
    n_ridge: float = 2.4
    n_gap: float = 1.0
    n_incident: float = 1.0
    n_substrate: float = 1.5
    angle_deg: float = 0.0

    def validate(self):
        values = np.asarray(list(asdict(self).values()))
        if np.iscomplexobj(values) or not np.all(np.isfinite(values)):
            raise ValueError("Parameters must be finite real numbers.")
        for key in ("period_um", "wavelength_um", "n_ridge", "n_gap", "n_incident", "n_substrate"):
            if getattr(self, key) <= 0:
                raise ValueError(f"{key} must be positive.")
        if not 0 <= self.width_um <= self.period_um or self.height_um < 0:
            raise ValueError("Require 0 <= width <= period and height >= 0.")
        if not -89 < self.angle_deg < 89:
            raise ValueError("Use incidence strictly between -89 and 89 degrees.")


def outgoing_q(index, alpha):
    """Positive real or positive imaginary kz/k0 in a lossless medium."""
    return np.sqrt((index * index - np.asarray(alpha) ** 2).astype(complex))


def solve_cell(cell=Cell(), half_order=16):
    """Return complex field amplitudes and incident-power-normalized orders.

    Retains m=-M,...,M, so there are 2M+1 spatial harmonics. Exact rectangle
    Fourier coefficients remove raster discretization. Modes are referenced
    at opposite layer faces to avoid exponentially growing propagation.
    """
    cell.validate()
    if isinstance(half_order, (bool, np.bool_)) or not isinstance(half_order, (int, np.integer)) or half_order < 0:
        raise ValueError("half_order must be a nonnegative integer.")
    m = np.arange(-half_order, half_order + 1)
    count = len(m)
    alpha0 = cell.n_incident * np.sin(np.deg2rad(cell.angle_deg))
    alpha = alpha0 + m * cell.wavelength_um / cell.period_um
    # A truncation must include every geometrically open exterior channel.
    next_alpha = alpha0 + np.array([-half_order - 1, half_order + 1]) * cell.wavelength_um / cell.period_um
    if np.any(np.abs(next_alpha) <= max(cell.n_incident, cell.n_substrate)):
        raise ValueError("Increase half_order to include all exterior open/grazing orders.")
    qi, qt = outgoing_q(cell.n_incident, alpha), outgoing_q(cell.n_substrate, alpha)
    if min(np.min(np.abs(qi)), np.min(np.abs(qt))) < 1e-9:
        raise ValueError("An exterior order is grazing; evaluate away from exact cutoff.")
    fill = cell.width_um / cell.period_um
    difference = m[:, None] - m[None, :]
    eps = (cell.n_ridge ** 2 - cell.n_gap ** 2) * fill * np.sinc(fill * difference)
    eps += cell.n_gap ** 2 * np.eye(count)
    eigenvalues, W = eigh(eps - np.diag(alpha ** 2))
    q = np.sqrt(eigenvalues.astype(complex))
    if np.min(np.abs(q)) < 1e-10:
        raise ValueError("A layer eigenmode is at cutoff; perturb parameters away from this singular basis.")
    V = W * q[None, :]
    P = np.exp(2j * np.pi * q * cell.height_um / cell.wavelength_um)
    # a: forward modes at z=0; b: backward modes at z=height.
    QW_i, QW_t = qi[:, None] * W, qt[:, None] * W
    matrix = np.block([[V + QW_i, (QW_i - V) * P],
                       [(V - QW_t) * P, -V - QW_t]])
    incident = np.zeros(count, complex)
    incident[half_order] = 1
    rhs = np.r_[2 * qi * incident, np.zeros(count, complex)]
    coefficients = solve(matrix, rhs, assume_a="gen")
    a, b = coefficients[:count], coefficients[count:]
    r = W @ (a + P * b) - incident
    t = W @ (P * a + b)
    R = qi.real / qi[half_order].real * np.abs(r) ** 2
    T = qt.real / qi[half_order].real * np.abs(t) ** 2
    residual = np.linalg.norm(matrix @ coefficients - rhs) / np.linalg.norm(rhs)
    return dict(orders=m, alpha=alpha, qi=qi, qt=qt, r=r, t=t,
                R=R, T=T, R_total=float(R.sum()), T_total=float(T.sum()),
                balance_error=float(abs(1 - R.sum() - T.sum())),
                solve_residual=float(residual), half_order=int(half_order),
                modes=dict(W=W, q=q, a=a, b=b))


def sample_ey(cell, result, x_um, z_um):
    """Reconstruct Ey/Eincident on a rectangular x,z grid, including near fields."""
    x, z = np.asarray(x_um), np.asarray(z_um)
    k0 = 2*np.pi/cell.wavelength_um
    basis = np.exp(1j*k0*result["alpha"][:, None]*x[None, :])
    field = np.empty((len(z), len(x)), complex)
    modes = result["modes"]
    for row, depth in enumerate(z):
        if depth < 0:
            reflected = result["r"]*np.exp(-1j*k0*result["qi"]*depth)
            field[row] = reflected @ basis + np.exp(1j*k0*(result["alpha"][result["half_order"]]*x + result["qi"][result["half_order"]]*depth))
        elif depth > cell.height_um:
            transmitted = result["t"]*np.exp(1j*k0*result["qt"]*(depth-cell.height_um))
            field[row] = transmitted @ basis
        else:
            modal = modes["a"]*np.exp(1j*k0*modes["q"]*depth) + modes["b"]*np.exp(1j*k0*modes["q"]*(cell.height_um-depth))
            field[row] = (modes["W"] @ modal) @ basis
    return field


def film_reference(cell, layer_index):
    """Independent scalar Fresnel/Fabry-Perot expression for a uniform film."""
    cell.validate()
    alpha = np.array([cell.n_incident * np.sin(np.deg2rad(cell.angle_deg))])
    q0 = outgoing_q(cell.n_incident, alpha)[0]
    q1 = outgoing_q(layer_index, alpha)[0]
    q2 = outgoing_q(cell.n_substrate, alpha)[0]
    r01, r12 = (q0-q1)/(q0+q1), (q1-q2)/(q1+q2)
    t01, t12 = 2*q0/(q0+q1), 2*q1/(q1+q2)
    phase = np.exp(2j*np.pi*q1*cell.height_um/cell.wavelength_um)
    denominator = 1+r01*r12*phase**2
    return (r01+r12*phase**2)/denominator, t01*t12*phase/denominator


def deembed_te(r_monitor, t_monitor, wavelength_um, qi0, qt0, incident_offset_um, output_offset_um):
    """Move homogeneous-medium monitor amplitudes back to the two layer faces.

    The incident monitor is at -Li and output monitor at height+Lt.
    Each measured coefficient is divided by incident Ey at -Li.
    """
    k0 = 2*np.pi/wavelength_um
    return (r_monitor*np.exp(-2j*k0*qi0*incident_offset_um),
            t_monitor*np.exp(-1j*k0*(qi0*incident_offset_um+qt0*output_offset_um)))


def phase_error_deg(value, reference):
    """Circular phase difference; only use where both amplitudes are meaningful."""
    return np.rad2deg(np.angle(np.asarray(value) * np.conj(reference)))
