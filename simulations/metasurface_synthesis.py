"""Chapter 5: restricted full-wave TE supercells and scalar/Jones models.

Extends the Chapter 3 equations to multiple coplanar ridges of a common height.
Scalar propagation and Jones matrices are separate models, not ridge solutions.
All lengths use micrometers; exp(-i omega t), exp(i k.r).
"""
from dataclasses import replace
import numpy as np
from scipy.linalg import eigh, solve
from unit_cell_te import Cell, outgoing_q

SOLVER_VERSION = 'te-supercell-1.0'


def solve_supercell(widths_um, pitch_um=.65, height_um=1.5, wavelength_um=1.55,
                    n_ridge=2.4, n_gap=1., n_incident=1., n_substrate=1.5,
                    angle_deg=0., half_order=48):
    """Exact rectangle Fourier coefficients; all ridges share a common height.

    Cell j is [j*p,(j+1)*p]; its centered ridge has width widths_um[j].
    Returns field ratios referenced to z=0 (r) and z=height (t).
    """
    widths = np.asarray(widths_um)
    if widths.ndim != 1 or not len(widths) or np.iscomplexobj(widths) or not np.all(np.isfinite(widths)):
        raise ValueError('Use a nonempty one-dimensional vector of finite real widths.')
    if not np.isfinite(pitch_um) or pitch_um<=0 or np.any(widths<0) or np.any(widths>pitch_um):
        raise ValueError('Require positive pitch and 0 <= each width <= pitch.')
    count_cells = len(widths)
    cell = Cell(period_um=count_cells*pitch_um, width_um=float(widths[0]), height_um=height_um,
                wavelength_um=wavelength_um, n_ridge=n_ridge, n_gap=n_gap,
                n_incident=n_incident, n_substrate=n_substrate, angle_deg=angle_deg)
    cell.validate()
    if isinstance(half_order, (bool,np.bool_)) or not isinstance(half_order,(int,np.integer)) or half_order<0:
        raise ValueError('half_order must be a nonnegative integer.')
    m = np.arange(-half_order,half_order+1)
    alpha0 = n_incident*np.sin(np.deg2rad(angle_deg))
    alpha = alpha0 + m*wavelength_um/cell.period_um
    neighbors = alpha0 + np.array([-half_order-1,half_order+1])*wavelength_um/cell.period_um
    if np.any(abs(neighbors)<=max(n_incident,n_substrate)):
        raise ValueError('Increase half_order to include all exterior open channels.')
    qi,qt = outgoing_q(n_incident,alpha),outgoing_q(n_substrate,alpha)
    if min(np.min(abs(qi)),np.min(abs(qt)))<1e-9:
        raise ValueError('Exact exterior grazing cutoff is excluded; perturb the parameters.')
    ell = np.arange(-2*half_order,2*half_order+1)
    centers=(np.arange(count_cells)+.5)*pitch_um
    eps_coeff=np.sum((n_ridge**2-n_gap**2)*(widths[:,None]/cell.period_um)*
                     np.sinc(widths[:,None]*ell/cell.period_um)*
                     np.exp(-2j*np.pi*centers[:,None]*ell/cell.period_um),axis=0)
    eps_coeff[2*half_order]+=n_gap**2
    eps = eps_coeff[m[:,None]-m[None,:]+2*half_order]
    eigenvalues,W=eigh(eps-np.diag(alpha**2))
    q=np.sqrt(eigenvalues.astype(complex))
    if np.min(abs(q))<1e-10:
        raise ValueError('Layer eigenmode cutoff is excluded from this modal basis.')
    V=W*q;P=np.exp(2j*np.pi*q*height_um/wavelength_um)
    QiW,QtW=qi[:,None]*W,qt[:,None]*W
    matrix=np.block([[V+QiW,(QiW-V)*P],[(V-QtW)*P,-V-QtW]])
    incident=np.zeros(len(m),complex);incident[half_order]=1
    rhs=np.r_[2*qi*incident,np.zeros(len(m),complex)]
    coefficients=solve(matrix,rhs)
    a,b=np.split(coefficients,2)
    r=W@(a+P*b)-incident;t=W@(P*a+b)
    R=qi.real/qi[half_order].real*abs(r)**2
    T=qt.real/qi[half_order].real*abs(t)**2
    return dict(orders=m,alpha=alpha,qi=qi,qt=qt,r=r,t=t,R=R,T=T,
                R_total=float(R.sum()),T_total=float(T.sum()),
                balance_error=float(abs(1-R.sum()-T.sum())),
                solve_residual=float(np.linalg.norm(matrix@coefficients-rhs)/np.linalg.norm(rhs)),
                half_order=int(half_order),cell=cell,modes=dict(W=W,q=q,a=a,b=b))


def staircase_coefficients(values, orders):
    """Exact Fourier coefficients of equal-width complex staircase samples."""
    values=np.asarray(values,complex);orders=np.asarray(orders)
    if values.ndim!=1 or not values.size or not np.all(np.isfinite(values)):
        raise ValueError('Use a finite nonempty complex sample vector.')
    centers=(np.arange(len(values))+.5)/len(values)
    return np.sinc(orders/len(values))*np.sum(values[None,:]*np.exp(-2j*np.pi*orders[:,None]*centers),axis=1)/len(values)


def select_widths(rows, target_phases, minimum_T=.8, phase_offset=0.):
    """Discrete circular-phase selection among accepted rows above a power cut."""
    eligible=[r for r in rows if r['accepted'] and r['T']>=minimum_T]
    if not eligible:raise ValueError('No eligible geometry meets the minimum transmission.')
    complex_t=np.array([complex(r['t_real'],r['t_imag']) for r in eligible])
    desired=np.asarray(target_phases)+phase_offset
    errors=np.angle(complex_t[None,:]*np.exp(-1j*desired[:,None]))
    indices=np.argmin(abs(errors),axis=1)
    return [eligible[j] for j in indices], errors[np.arange(len(indices)),indices]


def angular_spectrum_1d(field, dx_um, wavelength_um, z_um, index=1., propagating_only=False):
    """Forward scalar Helmholtz propagation on a periodic FFT window.

    For z>=0 the chosen root decays evanescent components. This is a scalar
    aperture-field model in a homogeneous medium, not a lens full-wave solve.
    """
    field=np.asarray(field,complex)
    if field.ndim!=1 or not field.size or not np.all(np.isfinite(field)):
        raise ValueError('Use a finite one-dimensional complex field.')
    if not all(np.isfinite(v) for v in [dx_um,wavelength_um,z_um,index]) or min(dx_um,wavelength_um,index)<=0 or z_um<0:
        raise ValueError('Require positive dx, wavelength, index and nonnegative propagation distance.')
    kx=2*np.pi*np.fft.fftfreq(len(field),dx_um)
    k=2*np.pi*index/wavelength_um
    kz=np.sqrt((k*k-kx*kx).astype(complex))
    transfer=np.exp(1j*kz*z_um)
    if propagating_only:transfer[abs(kx)>=k]=0
    return np.fft.ifft(np.fft.fft(field)*transfer)


def rotated_jones(tx,ty,angle_rad):
    """R(theta) diag(tx,ty) R(-theta), in the laboratory x,y basis."""
    c,s=np.cos(angle_rad),np.sin(angle_rad)
    rotation=np.array([[c,-s],[s,c]])
    return rotation@np.diag([tx,ty])@rotation.T


def line_fwhm(x, intensity):
    """Linear-interpolated half-maximum width of the largest sampled peak."""
    x,intensity=np.asarray(x),np.asarray(intensity)
    peak=int(np.argmax(intensity));half=intensity[peak]/2
    left=np.where(intensity[:peak]<half)[0]
    right=np.where(intensity[peak+1:]<half)[0]+peak+1
    if not len(left) or not len(right):return float('nan')
    a,b=left[-1],right[0]
    xl=np.interp(half,intensity[a:a+2],x[a:a+2])
    xr=np.interp(half,intensity[b-1:b+1][::-1],x[b-1:b+1][::-1])
    return float(xr-xl)
