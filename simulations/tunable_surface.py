"""Chapter 7: a passive bias-dependent equivalent impedance and scalar array.

exp(-i omega t), normal incidence, real positive reference impedance, no
transmitted port. L and C are effective surface-circuit values, not extracted
component values for the illustrative patch drawing. No full-wave solver.
"""
from dataclasses import asdict, dataclass
import numpy as np
from scipy.optimize import minimize_scalar

MODEL_VERSION = 'tunable-impedance-1.1'
C0 = 299792458.0


@dataclass(frozen=True)
class Surface:
    inductance_nH: float = 20.0
    capacitance0_pF: float = 0.12
    junction_voltage_V: float = 1.0
    exponent: float = 1.0
    resistance_ohm: float = 25.0
    impedance_ohm: float = 376.730313668
    voltage_max_V: float = 20.0

    def validate(self):
        for name, value in asdict(self).items():
            if not np.isreal(value) or not np.isfinite(value):
                raise ValueError('Surface parameters must be finite real numbers.')
            if value < 0 or (name != 'resistance_ohm' and value == 0):
                raise ValueError('Use positive parameters and nonnegative resistance.')


def real_values(value, name):
    a = np.asarray(value)
    if np.iscomplexobj(a) or not np.all(np.isfinite(a)):
        raise ValueError(name + ' must be finite and real.')
    return a.astype(float)


def capacitance(voltage_V, surface=Surface()):
    surface.validate()
    v = real_values(voltage_V, 'Voltage')
    if np.any((v < 0) | (v > surface.voltage_max_V)):
        raise ValueError('Voltage lies outside the declared tuning interval.')
    return surface.capacitance0_pF * 1e-12 / (1 + v/surface.junction_voltage_V)**surface.exponent


def response(frequency_GHz, voltage_V, surface=Surface()):
    f = real_values(frequency_GHz, 'Frequency')
    if np.any(f <= 0):
        raise ValueError('Frequency must be positive.')
    c = capacitance(voltage_V, surface)
    omega = 2*np.pi*f*1e9
    x = 1/(omega*c) - omega*surface.inductance_nH*1e-9
    z = surface.resistance_ohm + 1j*x
    gamma = (z-surface.impedance_ohm)/(z+surface.impedance_ohm)
    absorbed = 4*surface.resistance_ohm*surface.impedance_ohm / abs(z+surface.impedance_ohm)**2
    return dict(gamma=gamma, reflected=abs(gamma)**2, absorbed=absorbed,
                reactance_ohm=x, capacitance_pF=c*1e12,
                phase_deg=np.where(abs(gamma)>1e-10,np.rad2deg(np.angle(gamma)),np.nan))


def array_positions(elements=32, spacing_wavelength=.5):
    if isinstance(elements, bool) or not isinstance(elements, (int, np.integer)) or elements < 2:
        raise ValueError('Use an integer array size of at least two.')
    if not np.isfinite(spacing_wavelength) or spacing_wavelength <= 0:
        raise ValueError('Spacing must be positive and finite.')
    return (np.arange(elements)-(elements-1)/2)*spacing_wavelength


def unwrapped_phase_deg(gamma, amplitude_floor=1e-10):
    """Unwrap each usable 1D segment independently; retain gaps at zeros."""
    g = np.asarray(gamma, complex)
    if g.ndim != 1 or not np.all(np.isfinite(g)):
        raise ValueError('Use a finite one-dimensional complex response.')
    if not np.isfinite(amplitude_floor) or amplitude_floor <= 0:
        raise ValueError('Use a positive finite amplitude floor.')
    usable = abs(g) > amplitude_floor
    phase = np.full(g.shape, np.nan)
    edges = np.flatnonzero(np.diff(np.r_[False, usable, False]))
    for start, stop in zip(edges[::2], edges[1::2]):
        phase[start:stop] = np.rad2deg(np.unwrap(np.angle(g[start:stop])))
    return phase


def array_field(coefficients, angles_deg, positions_wavelength):
    g = np.asarray(coefficients, dtype=complex)
    x = real_values(positions_wavelength, 'Positions')
    angles = real_values(angles_deg, 'Angles')
    if g.ndim != 1 or x.shape != g.shape or g.size < 2 or not np.all(np.isfinite(g)):
        raise ValueError('Use matching finite coefficient and position vectors.')
    if np.any(abs(angles) > 90):
        raise ValueError('Angles must lie between -90 and 90 degrees.')
    return np.mean(g * np.exp(-2j*np.pi*np.sin(np.deg2rad(angles))[...,None]*x), axis=-1)


def code_array(target_deg=25., bits=4, circuit=False, surface=Surface(), frequency_GHz=10., elements=32, spacing_wavelength=.5):
    if not np.isfinite(target_deg) or abs(target_deg) >= 80:
        raise ValueError('Use a target strictly inside +/-80 degrees.')
    if isinstance(bits, bool) or not isinstance(bits, (int,np.integer)) or not 1 <= bits <= 8:
        raise ValueError('Use 1 to 8 integer control bits.')
    x = array_positions(elements, spacing_wavelength)
    desired = np.exp(2j*np.pi*x*np.sin(np.deg2rad(target_deg)))
    levels = 2**bits
    voltage = np.linspace(0,surface.voltage_max_V,levels)
    states = response(frequency_GHz,voltage,surface)['gamma'] if circuit else np.exp(2j*np.pi*np.arange(levels)/levels)
    chosen = np.argmin(abs(desired[:,None]-states[None,:])**2,axis=1)
    gamma = states[chosen]
    target_metric = float(abs(array_field(gamma,target_deg,x))**2)
    return dict(positions=x, desired=desired, gamma=gamma, indices=chosen,
                voltage_V=voltage[chosen] if circuit else None, target_metric=target_metric)


def feedback_voltage(target, measure, voltage_max=20., grid_size=17):
    """Bounded calibration using only measured complex responses; log every query.

    Coarse search followed by local scalar minimization. Endpoints remain
    candidates. This is not a proof of global optimality for an arbitrary plant.
    """
    if not np.isfinite(target) or not np.isfinite(voltage_max) or voltage_max<=0:
        raise ValueError('Use a finite target and positive voltage bound.')
    if not isinstance(grid_size,int) or grid_size<3:
        raise ValueError('At least three coarse samples are needed.')
    records=[]
    def objective(v):
        measured=complex(measure(float(v)))
        if not np.isfinite(measured): raise ValueError('The measured response is not finite.')
        cost=float(abs(measured-target)**2)
        records.append(dict(voltage_V=float(v),error_squared=cost))
        return cost
    grid=np.linspace(0,voltage_max,grid_size)
    costs=[objective(v) for v in grid]
    best=int(np.argmin(costs))
    bounds=(grid[max(0,best-1)],grid[min(grid_size-1,best+1)])
    minimize_scalar(objective,bounds=bounds,method='bounded',options={'xatol':1e-7,'maxiter':60})
    selected=min(records,key=lambda r:r['error_squared'])
    return dict(selected=selected,queries=records)


def step_voltage(time_s, initial=2., final=14., tau_s=4e-6):
    t=real_values(time_s,'Time')
    if np.any(t<0) or not np.isfinite(tau_s) or tau_s<=0 or not np.isfinite(initial+final):
        raise ValueError('Use nonnegative times and a positive time constant.')
    return final+(initial-final)*np.exp(-t/tau_s)


def periodic_voltage(fraction, low=3., high=14., duty=.5, modulation_Hz=2e4, tau_s=4e-6):
    """Steady periodic RC state. The low command occupies 0 <= t/T < duty."""
    u=real_values(fraction,'Cycle fraction')
    if np.any((u<0)|(u>=1)) or not 0<duty<1 or not np.isfinite(duty):
        raise ValueError('Use fractions in [0,1) and duty strictly between zero and one.')
    if not np.all(np.isfinite([low,high,modulation_Hz,tau_s])) or min(modulation_Hz,tau_s)<=0:
        raise ValueError('Finite states, positive frequency and time constant are required.')
    period=1/modulation_Hz
    a=np.exp(-duty*period/tau_s);b=np.exp(-(1-duty)*period/tau_s)
    start=(high*(1-b)+b*low*(1-a))/(-np.expm1(-period/tau_s))
    middle=low+(start-low)*a
    return np.where(u<duty,low+(start-low)*np.exp(-u*period/tau_s),
                    high+(middle-high)*np.exp(-(u-duty)*period/tau_s))


def binary_harmonics(orders,gamma_a,gamma_b,duty=.5):
    """c_l for Gamma(t)=sum_l c_l exp(-i l Omega t); output is omega0+l*Omega."""
    m=real_values(orders,'Harmonic orders')
    if np.any(m!=np.round(m)) or not 0<duty<1 or not np.all(np.isfinite([gamma_a,gamma_b])):
        raise ValueError('Use integer orders, finite responses and duty in (0,1).')
    return ((gamma_a-gamma_b)*duty*np.sinc(m*duty)*np.exp(1j*np.pi*m*duty)
            +np.where(m==0,gamma_b,0))


def sampled_harmonics(values,orders):
    values=np.asarray(values,dtype=complex)
    m=real_values(orders,'Harmonic orders')
    if values.ndim!=1 or values.size<2 or not np.all(np.isfinite(values)) or np.any(m!=np.round(m)):
        raise ValueError('Use a finite sampled waveform and integer orders.')
    u=(np.arange(values.size)+.5)/values.size
    return np.array([np.mean(values*np.exp(2j*np.pi*order*u)) for order in m])
