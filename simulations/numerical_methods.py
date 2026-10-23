"""A small, independently benchmarkable 1D frequency-domain Maxwell reduction.

Lengths are micrometers. The convention is exp(-i omega t). A real-index,
nonmagnetic film occupies 0 <= z <= d and has identical exterior media.
The unknown is tangential Ey at normal incidence. This is FDFD, not FDTD,
and it has a discrete radiation boundary rather than a PML.
"""
from dataclasses import asdict, dataclass

import numpy as np
from scipy.linalg import solve_banded

from waves_interfaces import film

MODEL_VERSION = "slab-fdfd-1.0"


@dataclass(frozen=True)
class Slab:
    wavelength_um: float = 1.55
    thickness_um: float = .60
    n_film: float = 2.4
    n_exterior: float = 1.

    def validate(self):
        for name, value in asdict(self).items():
            if isinstance(value, (bool, np.bool_)) or np.iscomplexobj(value):
                raise ValueError(f"{name} must be a positive finite real scalar.")
            array = np.asarray(value)
            if array.ndim or not np.isfinite(array) or value <= 0:
                raise ValueError(f"{name} must be a positive finite real scalar.")


def _integer(value, name, minimum=0):
    if (isinstance(value, (bool, np.bool_))
            or not isinstance(value, (int, np.integer)) or value < minimum):
        raise ValueError(f"{name} must be an integer >= {minimum}.")
    return int(value)


def phase_error_deg(value, reference, amplitude_floor=1e-12):
    """Circular phase error; NaN where either amplitude is too small."""
    if not np.isfinite(amplitude_floor) or amplitude_floor <= 0:
        raise ValueError("amplitude_floor must be positive and finite.")
    value, reference = np.broadcast_arrays(np.asarray(value, complex),
                                           np.asarray(reference, complex))
    angle = np.rad2deg(np.angle(value * np.conj(reference)))
    return np.where((abs(value) > amplitude_floor) & (abs(reference) > amplitude_floor),
                    angle, np.nan)


def exact_slab(slab=Slab()):
    """Independent Fresnel/Fabry-Perot result at z=0 and z=d.

    Reuses Chapter 2's exact planar model. The finite-difference solver below
    does not call this function or use the analytical answer.
    """
    slab.validate()
    return film(slab.n_exterior, slab.n_film, slab.n_exterior,
                slab.thickness_um, slab.wavelength_um)


def exact_slab_fields(slab, z_um):
    """Continuous exact Ey, normalized to incident Ey=1 at z=0."""
    slab.validate()
    z = np.asarray(z_um, float)
    if not np.all(np.isfinite(z)):
        raise ValueError("z_um must be finite.")
    reference = exact_slab(slab)
    k0 = 2*np.pi/slab.wavelength_um
    ke, kf = k0*slab.n_exterior, k0*slab.n_film
    r, t = reference['r'], reference['t']
    forward = ((1+r) + slab.n_exterior/slab.n_film*(1-r))/2
    backward = ((1+r) - slab.n_exterior/slab.n_film*(1-r))/2
    return np.where(z < 0, np.exp(1j*ke*z)+r*np.exp(-1j*ke*z),
                    np.where(z > slab.thickness_um,
                             t*np.exp(1j*ke*(z-slab.thickness_um)),
                             forward*np.exp(1j*kf*z)+backward*np.exp(-1j*kf*z)))


def solve_slab(slab=Slab(), cells=64, left_padding_cells=0,
               right_padding_cells=0, right_boundary='discrete',
               deembed='discrete'):
    """Solve a node-centered second-order Helmholtz boundary-value problem.

    h=d/cells. Both physical film faces lie on nodes. Their permittivity is
    the arithmetic mean of the adjacent media, appropriate to this tangential
    electric field and constant permeability. This rule is not a vector/TM
    interface treatment. All material and exterior discrete waves are kept
    below their grid cutoff k0*n*h=2.

    ``discrete`` is an exactly matched discrete exterior. ``continuum`` on
    the right deliberately substitutes exp(i*k0*ne*h) for exp(i*theta), and
    creates a reflected incoming wave. T_net includes that incoming flux;
    |E at the right boundary|^2 is not its forward transmitted power.

    ``deembed='continuum'`` deliberately removes padding with the continuum
    wave number. Only reported r/t phases change; E always uses the correct
    discrete incident normalization at z=0. Numerical r is at z=0 and t is
    the forward coefficient at z=d. With a mismatched boundary, these belong
    to a contaminated boundary problem rather than the open slab alone.
    """
    slab.validate()
    cells = _integer(cells, 'cells', 2)
    pleft = _integer(left_padding_cells, 'left_padding_cells')
    pright = _integer(right_padding_cells, 'right_padding_cells')
    if right_boundary not in ('discrete', 'continuum'):
        raise ValueError("right_boundary must be 'discrete' or 'continuum'.")
    if deembed not in ('discrete', 'continuum'):
        raise ValueError("deembed must be 'discrete' or 'continuum'.")
    h = slab.thickness_um/cells
    k0 = 2*np.pi/slab.wavelength_um
    if k0*h*max(slab.n_film, slab.n_exterior) >= 2*(1-1e-12):
        raise ValueError("Increase cells: k0*n*h must be below the discrete grid cutoff 2.")
    kappa = k0*slab.n_exterior*h
    theta = 2*np.arcsin(kappa/2)
    count = cells+pleft+pright+1
    z = (np.arange(count)-pleft)*h
    eps = np.full(count, slab.n_exterior**2)
    eps[pleft:pleft+cells+1] = slab.n_film**2
    eps[pleft] = eps[pleft+cells] = (slab.n_exterior**2+slab.n_film**2)/2
    main = (-2+(k0*h)**2*eps).astype(complex)
    left_multiplier = np.exp(1j*theta)
    right_multiplier = np.exp(1j*(theta if right_boundary == 'discrete' else kappa))
    main[0] += left_multiplier
    main[-1] += right_multiplier
    banded = np.zeros((3, count), complex)
    banded[0, 1:] = 1
    banded[1] = main
    banded[2, :-1] = 1
    rhs = np.zeros(count, complex)
    rhs[0] = 2j*np.sin(theta)
    raw = solve_banded((1, 1), banded, rhs)
    applied = main*raw
    applied[:-1] += raw[1:]
    applied[1:] += raw[:-1]
    algebraic_residual = np.linalg.norm(applied-rhs)/np.linalg.norm(rhs)

    # Decompose exterior fields using the discrete dispersion relation.
    rho = ((right_multiplier-np.exp(1j*theta))
           / (np.exp(-1j*theta)-right_multiplier))
    forward_boundary = raw[-1]/(1+rho)
    backward_boundary = rho*forward_boundary
    plane_phase = theta if deembed == 'discrete' else kappa
    r = (raw[0]-1)*np.exp(-2j*plane_phase*pleft)
    t = forward_boundary*np.exp(-1j*plane_phase*(pleft+pright))
    backward_exit = backward_boundary*np.exp(-1j*theta*pleft+1j*theta*pright)
    T_forward = float(abs(forward_boundary)**2)
    T_backward = float(abs(backward_boundary)**2)
    T_net = T_forward-T_backward
    R = float(abs(r)**2)
    E = raw*np.exp(-1j*theta*pleft)
    current = np.imag(np.conj(E[:-1])*E[1:])/np.sin(theta)
    return dict(slab=asdict(slab), cells=cells, step_um=h,
                left_padding_cells=pleft, right_padding_cells=pright,
                boundary=right_boundary, deembed=deembed,
                phase_step_rad=float(theta), continuum_phase_step_rad=float(kappa),
                r=complex(r), t=complex(t), backward_exit=complex(backward_exit),
                R=R, T=T_forward, T_forward=T_forward,
                T_backward=T_backward, T_net=float(T_net),
                boundary_reflection=complex(rho),
                energy_defect=float(abs(1-R-T_net)),
                algebraic_residual=float(algebraic_residual),
                z_um=z, epsilon_r=eps, E=E, current=current,
                current_z_um=(z[:-1]+z[1:])/2,
                current_spread=float(np.ptp(current)))


def summarize_result(result, reference=None):
    """JSON-safe scalar row for plots; field arrays are exported separately."""
    slab = Slab(**result['slab'])
    reference = exact_slab(slab) if reference is None else reference
    row = {key: result[key] for key in (
        'cells', 'step_um', 'left_padding_cells', 'right_padding_cells',
        'boundary', 'deembed', 'phase_step_rad', 'continuum_phase_step_rad',
        'R', 'T', 'T_forward', 'T_backward', 'T_net', 'energy_defect',
        'algebraic_residual', 'current_spread')}
    for name in ('r', 't', 'backward_exit', 'boundary_reflection'):
        row[name+'_real'] = float(result[name].real)
        row[name+'_imag'] = float(result[name].imag)
    row.update(complex_t_error=float(abs(result['t']-reference['t'])),
               complex_r_error=float(abs(result['r']-reference['r'])),
               power_T_error=float(abs(result['T_net']-reference['T'])),
               power_R_error=float(abs(result['R']-reference['R'])),
               phase_deg=float(np.rad2deg(np.angle(result['t']))),
               phase_error_deg=float(phase_error_deg(result['t'], reference['t'])),
               boundary_reflection_amplitude=float(abs(result['boundary_reflection'])))
    return row


def slab_sheet_approximation(slab=Slab()):
    """First thin-film electric-sheet approximation with matching phase planes.

    The sheet is centered at z=d/2 in the exterior background. This model
    difference is independent of the finite-difference spatial mesh.
    """
    slab.validate()
    k0 = 2*np.pi/slab.wavelength_um
    g = -1j*k0*(slab.n_film**2-slab.n_exterior**2)*slab.thickness_um
    background = np.exp(1j*k0*slab.n_exterior*slab.thickness_um)
    r = -g/(2*slab.n_exterior+g)*background
    t = 2*slab.n_exterior/(2*slab.n_exterior+g)*background
    return dict(r=complex(r), t=complex(t), R=float(abs(r)**2),
                T=float(abs(t)**2), admittance=complex(g),
                energy_defect=float(abs(1-abs(r)**2-abs(t)**2)))
