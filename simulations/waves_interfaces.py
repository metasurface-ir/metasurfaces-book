"""Exact planar teaching models with exp(-i omega t) and exp(+i k.r).

Bulk media are isotropic, nonmagnetic, and have positive real constant indices.
Interface coefficients use a COMMON tangential electric-field basis on both
sides, including reflected TM waves. Film coefficients use entrance/exit planes;
sheet coefficients use one coincident sheet plane. No patterned geometry solver
or fabricated-device validation is implemented in this module.
"""
import numpy as np

MODEL_VERSION = 'waves-interfaces-1.0'
PHASE_FLOOR = 1e-12


def _real(value, name, minimum=None, strict=False):
    array = np.asarray(value)
    if np.iscomplexobj(array) or not np.all(np.isfinite(array)):
        raise ValueError(f'{name} must contain finite real values.')
    array = array.astype(float)
    if minimum is not None and np.any(array <= minimum if strict else array < minimum):
        raise ValueError(f'{name} is outside its allowed domain.')
    return array


def _phase(value):
    return np.where(np.abs(value) > PHASE_FLOOR, np.rad2deg(np.angle(value)), np.nan)


def interface(n1=1., n2=1.5, angle_deg=0., polarization='TE'):
    """One interface: tangential E amplitudes and normal incident-flux ratios.

    At transmitted cutoff use the explicit TE/TM limiting coefficients. The TM
    tangential coefficient vanishes there; this does not imply that Ez vanishes.
    q2 is kz2/k0. A positive imaginary q2 is a decaying transmitted wave.
    """
    n1 = _real(n1, 'n1', 0, True)
    n2 = _real(n2, 'n2', 0, True)
    angle = _real(angle_deg, 'angle', 0)
    if np.any(angle >= 90) or polarization not in ('TE', 'TM'):
        raise ValueError('Use 0 <= angle < 90 degrees and TE or TM.')
    n1, n2, angle = np.broadcast_arrays(n1, n2, angle)
    qx = n1 * np.sin(np.deg2rad(angle))
    q1 = n1 * np.cos(np.deg2rad(angle))
    # Avoid cancellation in matched media near grazing incidence. A transmitted
    # cutoff is possible only for genuine high-to-low index incidence.
    discriminant = (n2-n1)*(n2+n1)+q1**2
    cutoff = (n1 > n2) & (np.abs(discriminant) <= 1e-12 * np.maximum(1., np.maximum(n1**2, n2**2)))
    q2 = np.sqrt(np.where(cutoff, 0., discriminant).astype(complex))
    y1 = q1 if polarization == 'TE' else n1**2 / q1
    y2 = q2 if polarization == 'TE' else n2**2 / np.where(cutoff, 1.+0j, q2)
    r = (y1-y2)/(y1+y2)
    t = 2*y1/(y1+y2)
    if polarization == 'TM':
        r = np.where(cutoff, -1.+0j, r)
        t = np.where(cutoff, 0.+0j, t)
    R = np.abs(r)**2
    T = np.where(cutoff, 0., y2.real/y1*np.abs(t)**2)
    regime = np.where(cutoff, 'cutoff', np.where(discriminant > 0, 'propagating', 'evanescent'))
    return dict(r=r, t=t, R=R, T=T, phase_deg=_phase(t), q2=q2,
                qx=qx, y1=y1, regime=regime, balance_error=np.abs(1-R-T))


def film(n1=1., nf=np.sqrt(1.5), n2=1.5, thickness_um=.1224744871391589,
         wavelength_um=.6):
    """Exact normal-incidence coherent film; t is referenced to its EXIT plane."""
    n1 = _real(n1, 'n1', 0, True)
    nf = _real(nf, 'nf', 0, True)
    n2 = _real(n2, 'n2', 0, True)
    d = _real(thickness_um, 'thickness', 0)
    wavelength = _real(wavelength_um, 'wavelength', 0, True)
    delta = 2*np.pi*nf*d/wavelength
    r01, r12 = (n1-nf)/(n1+nf), (nf-n2)/(nf+n2)
    denominator = 1+r01*r12*np.exp(2j*delta)
    r = (r01+r12*np.exp(2j*delta))/denominator
    t = (2*n1/(n1+nf))*(2*nf/(nf+n2))*np.exp(1j*delta)/denominator
    R, T = np.abs(r)**2, n2/n1*np.abs(t)**2
    return dict(r=r, t=t, R=R, T=T, phase_deg=_phase(t),
                delta=delta, balance_error=np.abs(1-R-T))


def film_scattering(n1=1., nf=np.sqrt(1.5), n2=1.5,
                    thickness_um=.1224744871391589, wavelength_um=.6):
    """Power-normalized reciprocal two-port S at the film entrance/exit planes."""
    left = film(n1, nf, n2, thickness_um, wavelength_um)
    right = film(n2, nf, n1, thickness_um, wavelength_um)
    return np.stack([np.stack([left['r'], np.sqrt(n1/n2)*right['t']], axis=-1),
                     np.stack([np.sqrt(n2/n1)*left['t'], right['r']], axis=-1)], axis=-2)


def sheet(conductance=0., susceptance=0., n1=1., n2=1.):
    """Passive electric shunt g=eta0*Ys=G+iB at normal incidence.

    Continuity enforces t=1+r. Bulk n is real/nonmagnetic; G>=0 is dissipative.
    Positive B is inductive under this module's exp(-i omega t) convention.
    """
    G = _real(conductance, 'conductance', 0)
    B = _real(susceptance, 'susceptance')
    n1 = _real(n1, 'n1', 0, True)
    n2 = _real(n2, 'n2', 0, True)
    g = G+1j*B
    r = (n1-n2-g)/(n1+n2+g)
    t = 2*n1/(n1+n2+g)
    R, T = np.abs(r)**2, n2/n1*np.abs(t)**2
    A = G/n1*np.abs(t)**2
    return dict(r=r, t=t, R=R, T=T, A=A, phase_deg=_phase(t),
                balance_error=np.abs(1-R-T-A))


def sheet_scattering(conductance=0., susceptance=0., n1=1., n2=1.):
    left = sheet(conductance, susceptance, n1, n2)
    right = sheet(conductance, susceptance, n2, n1)
    return np.stack([np.stack([left['r'], np.sqrt(n1/n2)*right['t']], axis=-1),
                     np.stack([np.sqrt(n2/n1)*left['t'], right['r']], axis=-1)], axis=-2)


def coherent_sheet(conductance=2., susceptance=0., phase_deg=0.):
    """Equal-power coherent inputs, fixed total incident power=1, symmetric air."""
    phase = _real(phase_deg, 'relative phase')
    s = sheet(conductance, susceptance)
    a2 = np.exp(1j*np.deg2rad(phase))
    b1 = (s['r']+s['t']*a2)/np.sqrt(2.)
    b2 = (s['t']+s['r']*a2)/np.sqrt(2.)
    outgoing = np.abs(b1)**2+np.abs(b2)**2
    return dict(b1=b1, b2=b2, outgoing=outgoing, absorbed=1-outgoing)


def retrieve_sheet(r, t, n1=1., n2=1., minimum_amplitude=1e-8):
    """Retrieve g only for a validated coincident-plane electric-sheet model.

    This algebra is not a geometry/material retrieval. Finite films generally
    violate t=1+r at their entrance/exit planes and are deliberately rejected.
    """
    n1 = _real(n1, 'n1', 0, True)
    n2 = _real(n2, 'n2', 0, True)
    floor = _real(minimum_amplitude, 'minimum amplitude', 0, True)
    r, t = np.asarray(r, dtype=complex), np.asarray(t, dtype=complex)
    if not np.all(np.isfinite(r)) or not np.all(np.isfinite(t)):
        raise ValueError('Use finite complex coefficients.')
    if np.any(np.abs(t) <= floor):
        raise ValueError('Transmission is too small for a stable sheet retrieval.')
    if np.any(np.abs(t-1-r) > 1e-9):
        raise ValueError('Coefficients do not obey coincident-plane electric-sheet continuity.')
    return 2*n1/t-(n1+n2)


def polarization(alpha_deg=45., delta_deg=90., analyzer_deg=0.):
    """Unit Jones vector and coordinate-defined Stokes values, no handedness label.

    V=2 Im(conj(Ex)*Ey). For exp(-iwt), E at t=0 and +quarter cycle is
    respectively (Re Ex, Re Ey) and (Im Ex, Im Ey) at a fixed spatial point.
    """
    alpha = np.deg2rad(_real(alpha_deg, 'alpha'))
    delta = np.deg2rad(_real(delta_deg, 'delta'))
    beta = np.deg2rad(_real(analyzer_deg, 'analyzer'))
    Ex, Ey = np.cos(alpha).astype(complex), np.sin(alpha)*np.exp(1j*delta)
    cross = np.conj(Ex)*Ey
    I = np.abs(Ex)**2+np.abs(Ey)**2
    Q, U, V = np.abs(Ex)**2-np.abs(Ey)**2, 2*cross.real, 2*cross.imag
    power = np.abs(np.cos(beta)*Ex+np.sin(beta)*Ey)**2
    return dict(Ex=Ex, Ey=Ey, I=I, Q=Q, U=U, V=V, analyzer_power=power)


def te_interface_fields(x_um, z_um, n1=1.5, n2=1., angle_deg=50., wavelength_um=.6):
    """TE field and normal Poynting flux for a lossless interface, incident Ey=1.

    x/z broadcast. Hx/Hz are scaled by vacuum impedance. This is an exact
    planar field, not a numerical Maxwell discretization or patterned geometry.
    """
    wavelength = _real(wavelength_um, 'wavelength', 0, True)
    x, z = _real(x_um, 'x'), _real(z_um, 'z')
    v = interface(n1, n2, angle_deg, 'TE')
    q1 = _real(n1, 'n1', 0, True)*np.cos(np.deg2rad(angle_deg))
    k0 = 2*np.pi/wavelength
    incoming = np.exp(1j*k0*(v['qx']*x+q1*z))
    reflected = v['r']*np.exp(1j*k0*(v['qx']*x-q1*z))
    # Mask the output exponent before evaluation to avoid a growing extension
    # of the evanescent solution into the unrelated incident region.
    transmitted = v['t']*np.exp(1j*k0*(v['qx']*x+v['q2']*np.maximum(z, 0)))
    E = np.where(z < 0, incoming+reflected, transmitted)
    Hx = np.where(z < 0, -q1*incoming+q1*reflected, -v['q2']*transmitted)
    Hz = v['qx']*E
    flux = -np.real(E*np.conj(Hx))/q1
    return dict(E=E, Hx_eta0=Hx, Hz_eta0=Hz, normal_flux=flux)
