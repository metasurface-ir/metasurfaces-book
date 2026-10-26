"""Independent physical limits, calibration algebra and sampling checks."""
from pathlib import Path
from dataclasses import asdict,replace
import json,hashlib,sys
import numpy as np
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from simulations.materials_measurement import (Experiment,C0,lorentz,resonance,reflection,reference_factor,
    error_terms,measured,calibrate,correct,synthetic_sweep,tolerance_samples,tolerance_linear_std,
    uncertain_measurements,wilson)

def validate():
    p=Experiment();f=np.linspace(8,12,401);g=reflection(f,p=p)
    absorption=4*p.external_GHz*p.internal_GHz/((p.external_GHz+p.internal_GHz)**2+(f-10)**2)
    balance=float(np.max(abs(abs(g)**2+absorption-1)));assert balance<2e-15
    # Independent steady-state coupled-mode boundary/energy equations.
    mode=np.sqrt(2*p.external_GHz)/(p.external_GHz+p.internal_GHz-1j*(f-10))
    assert np.max(abs(-1+np.sqrt(2*p.external_GHz)*mode-g))<1e-15
    assert np.max(abs(abs(g)**2+2*p.internal_GHz*abs(mode)**2-1))<2e-15
    assert abs(reflection(10,p=replace(p,internal_GHz=p.external_GHz)))<1e-15
    assert np.max(abs(abs(reflection(f,p=replace(p,internal_GHz=0)))**2-1))<2e-15
    swapped=reflection(f,p=replace(p,external_GHz=p.internal_GHz,internal_GHz=p.external_GHz))
    assert np.max(abs(abs(swapped)**2-abs(g)**2))<1e-15
    halfwidth=p.external_GHz+p.internal_GHz
    assert abs((1-abs(reflection(10+halfwidth,p=p))**2)/absorption[200]-.5)<1e-14
    eps=lorentz(np.linspace(.01,100,3000));assert np.min(eps.imag)>0
    index=np.sqrt(eps);assert np.min(index.imag)>0 and np.max(abs(index*index-eps))<1e-13
    # Independent oscillator real/imaginary expressions.
    den=(14**2-f*f)**2+(1.2*f)**2
    assert np.max(abs(lorentz(f)-(2+1.1*14**2*(14**2-f*f)/den+1j*1.1*14**2*1.2*f/den)))<2e-15
    rng=np.random.default_rng(27);random_g=rng.uniform(0,.95,500)*np.exp(1j*rng.uniform(-np.pi,np.pi,500))
    d,t,s=error_terms(10.);std=np.array([-1.,0.,1.],complex)
    observed=measured(std,d,t,s);dc,tc,sc,cond=calibrate(std,observed)
    term_error=float(max(abs(dc-d),abs(tc-t),abs(sc-s)));assert term_error<1e-14
    roundtrip=float(np.max(abs(correct(measured(random_g,d,t,s),dc,tc,sc)-random_g)));assert roundtrip<1e-14
    # Independent geometric multiple-reflection series validates the forward box.
    series=d+t*random_g*sum((s*random_g)**q for q in range(16))
    series_error=float(np.max(abs(series-measured(random_g,d,t,s))));assert series_error<1e-14
    sweep=synthetic_sweep(f,p);recovery=float(np.max(abs(sweep['recovered']-sweep['truth'])));assert recovery<1e-14
    held=1j*np.ones_like(f);df,tf,sf=error_terms(f)
    recovered=correct(measured(held,df,tf,sf),*calibrate(std,measured(std,df[:,None],tf[:,None],sf[:,None]))[:3])
    assert np.max(abs(recovered-held))<1e-14
    assert np.max(abs(reference_factor(f,5)*reference_factor(f,-5)-1))<1e-15
    phase_slope=np.polyfit(f*1e9,np.unwrap(np.angle(reference_factor(f,5))),1)[0]
    assert abs(phase_slope-4*np.pi*.005/C0)<1e-23
    derivative_errors=[]
    for h in (.001,.0005):
        dw=(resonance(5+h,3,p)-resonance(5-h,3,p))/(2*h)
        de=(resonance(5,3+h,p)-resonance(5,3-h,p))/(2*h)
        derivative_errors.append(float(max(abs(dw+2),abs(de+10/6))))
    assert derivative_errors[1]<derivative_errors[0]<1e-6
    stats={}
    for rho in (-.6,0.,.6):
        draws=tolerance_samples(rho,count=100000,p=p);sd=float(np.std(draws,ddof=1));linear=float(tolerance_linear_std(rho,p))
        assert abs(sd/linear-1)<.015
        stats[str(rho)]=dict(sample_std_GHz=sd,linear_std_GHz=linear)
    assert wilson(0,100)[0]>=-1e-16 and wilson(100,100)[1]<=1+1e-15
    z=1.959963984540054;lo,hi=wilson(50,100)
    assert abs(lo+hi-1)<1e-15 and lo<.5<hi
    # 95% chi-square(2) ellipse threshold from independent radial integration.
    radius=np.sqrt(-2*np.log(.05));coverage=quad(lambda r:r*np.exp(-r*r/2),0,radius)[0]
    assert abs(coverage-.95)<1e-13
    # Independent Gaussian quadrature for the fixed-placement averaging floor.
    phase_std=4*np.pi*p.resonance_GHz*1e9*p.position_std_mm*1e-3/C0
    gamma0=reflection(p.resonance_GHz,p=p)
    floor_quad=quad(lambda z:abs(gamma0*(np.exp(1j*phase_std*z)-1))**2*np.exp(-z*z/2)/np.sqrt(2*np.pi),-10,10,epsabs=1e-14)[0]
    floor_closed=2*abs(gamma0)**2*(-np.expm1(-phase_std**2/2))
    assert abs(floor_quad-floor_closed)<1e-15
    exact_draws,_=uncertain_measurements(50,replace(p,noise_rms=0,standard_phase_std_deg=0,load_std=0,position_std_mm=0))
    assert np.max(abs(exact_draws-gamma0))<1e-14
    draws,conditions=uncertain_measurements(2000,p);assert np.all(np.isfinite(draws))
    invalid=[lambda:lorentz(0),lambda:resonance(-1,3),lambda:tolerance_samples(1.2),
        lambda:calibrate([1,1,1],[.1,.2,.3]),lambda:correct(1,0,0,0),lambda:reflection(0),
        lambda:wilson(101,100),lambda:uncertain_measurements(1)]
    for call in invalid:
        try:call()
        except ValueError:pass
        else:raise AssertionError('Invalid input accepted')
    result=dict(status='passed',parameters=asdict(p),
        source_sha256=hashlib.sha256((ROOT/'simulations/materials_measurement.py').read_text(encoding='utf-8').encode()).hexdigest(),
        checks=dict(power_balance=balance,error_term_recovery=term_error,random_inverse=roundtrip,
            independent_scattering_series=series_error,calibrated_surface=recovery,derivative_errors=derivative_errors,
            ellipse_probability=coverage,averaging_floor_quadrature_error=abs(floor_quad-floor_closed),
            invalid_inputs=len(invalid)),
        reference=dict(resonant_gamma=float(reflection(10).real),resonant_absorption=float(absorption[200]),
            loaded_Q=p.resonance_GHz/(2*(p.external_GHz+p.internal_GHz)),
            roundtrip_phase_deg_5mm=float(np.rad2deg(4*np.pi*10e9*.005/C0)),
            position_phase_std_deg=float(np.rad2deg(4*np.pi*10e9*.00005/C0)),
            tolerance=stats,calibration_condition=float(cond),
            complex_measurement_rms=float(np.sqrt(np.mean(abs(draws-reflection(10))**2)))),
        limits='Synthetic models and synthetic measurements only; no fabricated device or instrument validation.')
    out=ROOT/'data/chapter-09';out.mkdir(exist_ok=True,parents=True)
    (out/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result

if __name__=='__main__':print(json.dumps(validate(),indent=2))
