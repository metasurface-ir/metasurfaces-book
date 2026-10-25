"""Execute independent checks of Chapter 7's declared circuit/control baseline."""
from pathlib import Path
from dataclasses import asdict, replace
import hashlib, json, sys
import numpy as np
from scipy.integrate import solve_ivp

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from simulations.tunable_surface import (Surface,response,capacitance,array_positions,array_field,
    code_array,feedback_voltage,step_voltage,periodic_voltage,binary_harmonics,sampled_harmonics)


def validate():
    p=Surface();voltage=np.linspace(0,20,401);frequency=np.linspace(7,13,241)
    r=response(frequency[:,None],voltage[None,:],p)
    conservation=float(np.max(abs(r['reflected']+r['absorbed']-1)))
    assert conservation<2e-15 and np.max(r['reflected'])<=1+1e-14
    assert np.all(np.diff(capacitance(voltage,p))<0)
    lossless=response(frequency[:,None],voltage[None,:],replace(p,resistance_ohm=0.))
    assert np.max(abs(lossless['reflected']-1))<1e-14
    # Independently solve boundary equations for reflection and total H.
    boundary_error=0.
    for f in (7.,10.,13.):
        for v in (0.,3.,8.,14.,20.):
            c=capacitance(v,p);omega=2*np.pi*f*1e9
            z=p.resistance_ohm+1j/(omega*c)-1j*omega*p.inductance_nH*1e-9
            refl,h=np.linalg.solve(np.array([[1.,-z],[1.,p.impedance_ohm]],complex),[-1.,1.])
            boundary_error=max(boundary_error,float(abs(refl-response(f,v,p)['gamma'])))
            assert abs((1-abs(refl)**2)-p.resistance_ohm*p.impedance_ohm*abs(h)**2)<1e-14
    assert boundary_error<1e-14
    vr=p.junction_voltage_V*((p.capacitance0_pF*1e-12*(2*np.pi*10e9)**2*p.inductance_nH*1e-9)**(1/p.exponent)-1)
    critical=response(10.,vr,replace(p,resistance_ohm=p.impedance_ohm))
    assert abs(critical['gamma'])<1e-14 and np.isnan(critical['phase_deg'])
    x=array_positions();ideal=np.exp(2j*np.pi*x*np.sin(np.deg2rad(25.)))
    assert abs(array_field(ideal,25.,x)-1)<1e-14
    cases={str(bits):code_array(bits=bits) for bits in range(1,5)}
    assert all(c['target_metric']<=1+1e-14 for c in cases.values())
    circuit=code_array(circuit=True)
    assert np.all((circuit['voltage_V']>=0)&(circuit['voltage_V']<=20))
    assert circuit['target_metric']<=float(np.mean(abs(circuit['gamma'])))**2+1e-14
    # Symmetry check: mirror the aperture and reverse the observation direction.
    angles=np.linspace(-80,80,401)
    assert np.max(abs(array_field(circuit['gamma'][::-1],angles,x)-array_field(circuit['gamma'],-angles,x)))<1e-13
    # Uniform phase-error integral: a benchmark, not a finite-device efficiency.
    quantization_error=0.
    for levels in (2,4,8,16):
        error=(np.arange(50000)+.5)/50000*2*np.pi/levels-np.pi/levels
        quantization_error=max(quantization_error,float(abs(np.mean(np.exp(1j*error))-np.sinc(1/levels))))
    assert quantization_error<2e-10
    plant=replace(p,capacitance0_pF=p.capacitance0_pF*1.12)
    target=complex(response(10.,8.,p)['gamma'])
    feedback=feedback_voltage(target,lambda v:response(10.,v,plant)['gamma'])
    assert abs(feedback['selected']['voltage_V']-9.08)<1e-5
    assert feedback['selected']['error_squared']<1e-14
    assert all(0<=r['voltage_V']<=20 for r in feedback['queries'])
    t=np.linspace(0,24e-6,301)
    ode=solve_ivp(lambda t,y:(14-y)/4e-6,[0,t[-1]],[2.],t_eval=t,rtol=1e-11,atol=1e-12)
    ode_error=float(np.max(abs(ode.y[0]-step_voltage(t))))
    assert ode.success and ode_error<2e-9
    samples=16384;u=(np.arange(samples)+.5)/samples;orders=np.arange(-12,13)
    ga,gb=response(10.,[3.,14.],p)['gamma']
    square=np.where(u<.5,ga,gb)
    analytic=binary_harmonics(orders,ga,gb)
    numerical=sampled_harmonics(square,orders)
    harmonic_error=float(np.max(abs(numerical-analytic)));assert harmonic_error<1e-6
    waveform=response(10.,periodic_voltage(u),p)['gamma']
    coeff=sampled_harmonics(waveform,orders)
    fft=np.fft.ifft(waveform)[orders%samples]*np.exp(1j*np.pi*orders/samples)
    fft_error=float(np.max(abs(coeff-fft)));assert fft_error<1e-13
    parseval_error=float(abs(np.sum(abs(np.fft.ifft(waveform))**2)-np.mean(abs(waveform)**2)))
    assert parseval_error<1e-14
    # Ensure one complete periodic RC cycle returns to its initial state.
    eps=1e-10
    assert abs(periodic_voltage([0.])[0]-periodic_voltage([1-eps])[0])<1e-7
    invalid=[lambda:response(0.,0.),lambda:response(10.,-1.),lambda:response(10.,21.),
             lambda:response(10.,0.,replace(p,resistance_ohm=-1)),lambda:code_array(bits=0),
             lambda:array_positions(1),lambda:step_voltage([-1.]),lambda:periodic_voltage([1.]),
             lambda:binary_harmonics([.5],1,-1)]
    for call in invalid:
        try:call()
        except ValueError:pass
        else:raise AssertionError('An invalid input was accepted.')
    source=ROOT/'simulations/tunable_surface.py'
    result=dict(status='passed',model='passive equivalent impedance; scalar array; synthetic feedback; adiabatic envelope',
        source_sha256=hashlib.sha256(source.read_text(encoding='utf-8').encode()).hexdigest(),parameters=asdict(p),
        checks=dict(power_balance=conservation,boundary_solution=boundary_error,quantization_integral=quantization_error,
                    RC_ODE=ode_error,binary_harmonics=harmonic_error,FFT_parity=fft_error,Parseval=parseval_error,invalid_inputs=len(invalid)),
        reference=dict(resonant_voltage_V=float(vr),phase_span_deg=float(abs(np.diff(np.rad2deg(np.unwrap(np.angle(response(10.,voltage)['gamma'])))) .sum())),
                       ideal_quantized_target_metric={k:c['target_metric'] for k,c in cases.items()},
                       circuit_target_metric=circuit['target_metric'],feedback_voltage_V=feedback['selected']['voltage_V'],
                       feedback_queries=len(feedback['queries']),voltage_settle_2percent_us=float(-4*np.log(.02))))
    out=ROOT/'data/chapter-07';out.mkdir(parents=True,exist_ok=True)
    (out/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result


if __name__=='__main__':print(json.dumps(validate(),indent=2))
