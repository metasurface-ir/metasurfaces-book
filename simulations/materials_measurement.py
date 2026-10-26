"""Chapter 9: synthetic materials, tolerances and one-port measurements.

exp(-i omega t); positive material loss and positive propagation phase.
No material sample, fabricated patch or instrument data are represented.
"""
from dataclasses import dataclass, asdict
import numpy as np

C0=299792458.

@dataclass(frozen=True)
class Experiment:
    resonance_GHz: float=10.
    width_mm: float=5.
    epsilon_eff: float=3.
    external_GHz: float=.35
    internal_GHz: float=.12
    width_std_mm: float=.025
    epsilon_std: float=.04
    offset_mm: float=5.
    position_std_mm: float=.05
    noise_rms: float=.002
    standard_phase_std_deg: float=.4
    load_std: float=.002
    tolerance_GHz: float=.12
    seed: int=9

def real(value,name,positive=False):
    a=np.asarray(value)
    if np.iscomplexobj(a) or not np.all(np.isfinite(a)) or (positive and np.any(a<=0)):
        raise ValueError(name+' must be finite and real'+(' and positive' if positive else ''))
    return a.astype(float)

def validate_parameters(p):
    for name,value in asdict(p).items():
        real(value,name)
        if name not in ('offset_mm','seed') and value<0:raise ValueError('Nonnegative parameters required.')
    if min(p.resonance_GHz,p.width_mm,p.epsilon_eff,p.external_GHz,p.tolerance_GHz)<=0:
        raise ValueError('Positive resonance, geometry, permittivity, coupling and tolerance required.')
    if isinstance(p.seed,bool) or not isinstance(p.seed,(int,np.integer)) or p.seed<0:raise ValueError('Nonnegative integer seed required.')

def lorentz(f_GHz,epsilon_inf=2.,strength=1.1,pole_GHz=14.,damping_GHz=1.2):
    f=real(f_GHz,'frequency',True)
    for x in (epsilon_inf,strength,pole_GHz,damping_GHz):real(x,'Lorentz parameter',True)
    return epsilon_inf+strength*pole_GHz**2/(pole_GHz**2-f*f-1j*damping_GHz*f)

def resonance(width_mm,epsilon_eff,p=Experiment()):
    validate_parameters(p)
    w=real(width_mm,'width',True);e=real(epsilon_eff,'effective permittivity',True)
    return p.resonance_GHz*p.width_mm/w*np.sqrt(p.epsilon_eff/e)

def reflection(f_GHz,f0_GHz=None,p=Experiment()):
    validate_parameters(p)
    f=real(f_GHz,'frequency',True);f0=p.resonance_GHz if f0_GHz is None else real(f0_GHz,'resonance',True)
    return -1+2*p.external_GHz/(p.external_GHz+p.internal_GHz-1j*(f-f0))

def reference_factor(f_GHz,offset_mm):
    return np.exp(4j*np.pi*real(f_GHz,'frequency',True)*1e9*real(offset_mm,'offset')*1e-3/C0)

def error_terms(f_GHz):
    f=real(f_GHz,'frequency',True)
    return (.03*np.exp(1j*(.4+.2*(f-10))), .88*np.exp(1j*(.3+.2*(f-10))),
            .07*np.exp(-.8j)*np.ones_like(f))

def measured(gamma,directivity,tracking,source_match):
    g,d,t,s=np.broadcast_arrays(*[np.asarray(x,complex) for x in (gamma,directivity,tracking,source_match)])
    if not all(np.all(np.isfinite(x)) for x in (g,d,t,s)) or np.any(abs(1-s*g)<1e-10):
        raise ValueError('Invalid or singular error box.')
    return d+t*g/(1-s*g)

def calibrate(known,observed):
    """Three distinct known reflections; batched frequency/trial axes allowed."""
    g,m=np.broadcast_arrays(np.asarray(known,complex),np.asarray(observed,complex))
    if g.shape[-1]!=3 or not np.all(np.isfinite(g)) or not np.all(np.isfinite(m)):
        raise ValueError('Three finite standard observations required.')
    matrix=np.stack([np.ones_like(g),g,m*g],axis=-1)
    condition=np.linalg.cond(matrix)
    if np.any(condition>1e8):raise ValueError('Calibration standards are ill-conditioned.')
    solution=np.linalg.solve(matrix,m[...,None])[...,0]
    d,e,s=np.moveaxis(solution,-1,0)
    return d,e+d*s,s,condition

def correct(observed,directivity,tracking,source_match):
    m,d,t,s=np.broadcast_arrays(*[np.asarray(x,complex) for x in (observed,directivity,tracking,source_match)])
    den=t+s*(m-d)
    if not all(np.all(np.isfinite(x)) for x in (m,d,t,s)) or np.any(abs(den)<1e-10):
        raise ValueError('Invalid or singular calibration inverse.')
    return (m-d)/den

def complex_noise(rng,shape,rms):
    real(rms,'noise RMS')
    if rms<0:raise ValueError('Nonnegative noise required.')
    return rms/np.sqrt(2)*(rng.normal(size=shape)+1j*rng.normal(size=shape))

def wilson(successes,count,z=1.959963984540054):
    if isinstance(count,bool) or not isinstance(count,(int,np.integer)) or count<=0 or not 0<=successes<=count:
        raise ValueError('Valid binomial counts required.')
    if not isinstance(successes,(int,np.integer)):raise ValueError('Integer success count required.')
    phat=successes/count;den=1+z*z/count
    center=(phat+z*z/(2*count))/den
    half=z*np.sqrt(phat*(1-phat)/count+z*z/(4*count*count))/den
    return center-half,center+half

def tolerance_samples(rho=0.,bias_mm=0.,count=20000,p=Experiment()):
    validate_parameters(p);real(rho,'correlation');real(bias_mm,'bias')
    if not -1<=rho<=1 or isinstance(count,bool) or not isinstance(count,(int,np.integer)) or count<2:
        raise ValueError('Valid correlation and sample count required.')
    rng=np.random.default_rng(p.seed);u,v=rng.normal(size=(2,count))
    w=p.width_mm+bias_mm+p.width_std_mm*u
    eps=p.epsilon_eff+p.epsilon_std*(rho*u+np.sqrt(1-rho*rho)*v)
    f0=resonance(w,eps,p)
    return f0

def tolerance_linear_std(rho=0.,p=Experiment()):
    validate_parameters(p);real(rho,'correlation')
    if abs(rho)>1:raise ValueError('Correlation outside [-1,1].')
    a=p.resonance_GHz*p.width_std_mm/p.width_mm
    b=p.resonance_GHz*p.epsilon_std/(2*p.epsilon_eff)
    return np.sqrt(a*a+b*b+2*rho*a*b)

def synthetic_sweep(f_GHz,p=Experiment()):
    validate_parameters(p);f=real(f_GHz,'frequency',True)
    truth=reflection(f,p=p);port=truth*reference_factor(f,p.offset_mm)
    d,t,s=error_terms(f);known=np.array([-1.,0.,1.],complex)
    standard=measured(known,d[...,None],t[...,None],s[...,None])
    dc,tc,sc,cond=calibrate(known,standard)
    raw=measured(port,d,t,s)
    at_port=correct(raw,dc,tc,sc)
    recovered=at_port/reference_factor(f,p.offset_mm)
    return dict(truth=truth,raw=raw,at_port=at_port,recovered=recovered,condition=cond)

def uncertain_measurements(count=1000,p=Experiment()):
    """At f0: standard characterization, reading noise and placement uncertainty."""
    validate_parameters(p)
    if isinstance(count,bool) or not isinstance(count,(int,np.integer)) or count<2:raise ValueError('At least two trials required.')
    rng=np.random.default_rng(p.seed)
    known=np.array([-1.,0.,1.],complex)
    phase=rng.normal(0,np.deg2rad(p.standard_phase_std_deg),(count,2))
    actual=np.column_stack([-np.exp(1j*phase[:,0]),complex_noise(rng,count,p.load_std),np.exp(1j*phase[:,1])])
    assert np.max(abs(actual[:,1]))<1,'Load draws outside this passive synthetic population'
    d,t,s=error_terms(p.resonance_GHz)
    observed=measured(actual,d,t,s)+complex_noise(rng,(count,3),p.noise_rms)
    dc,tc,sc,cond=calibrate(known,observed)
    truth=reflection(p.resonance_GHz,p=p)
    placement=rng.normal(0,p.position_std_mm,count)
    raw=measured(truth*reference_factor(p.resonance_GHz,p.offset_mm+placement),d,t,s)+complex_noise(rng,count,p.noise_rms)
    result=correct(raw,dc,tc,sc)/reference_factor(p.resonance_GHz,p.offset_mm)
    return result,cond
