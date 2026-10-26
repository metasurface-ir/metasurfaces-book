"""Independent quadrature, limits and identities for the Chapter 8 baseline."""
from pathlib import Path
from dataclasses import asdict, replace
import hashlib, json, sys
import numpy as np
from scipy.integrate import dblquad

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from simulations.communication_link import (Link, C0, KB, aperture, paths, phase_command,
    channel, metrics, noise_power, error_expectation, training)


def validate():
    p=Link(); xyz,d,a=paths(p); g=phase_command(p); h=channel(g,p)
    coherent_error=float(abs(h-a.sum())/a.sum()); assert coherent_error<1e-11
    assert abs(channel(np.zeros_like(g),p)) == 0
    assert abs(channel(g,replace(p,efficiency=0))) == 0
    # Adaptive continuous integration independently checks midpoint amplitude quadrature.
    tx=np.array(p.tx_m); rx=np.array(p.rx_m)
    def kernel(y,x):
        rt=np.linalg.norm(tx-[x,y,0]); rr=np.linalg.norm(rx-[x,y,0])
        return np.sqrt(p.efficiency*tx[2]*rx[2])/(4*np.pi*(rt*rr)**1.5)
    integ,err=dblquad(kernel,-p.side_m/2,p.side_m/2,lambda x:-p.side_m/2,lambda x:p.side_m/2,epsabs=1e-13,epsrel=1e-10)
    quad_error=float(abs(h.real-integ)/integ); assert quad_error<1e-7
    refinements=[]
    for n in (24,48,96,192):
        q=replace(p,samples_side=n); _,_,w=paths(q)
        refinements.append(dict(samples_side=n,relative_error=float(abs(w.sum()-integ)/integ)))
    assert all(b['relative_error']<a['relative_error'] for a,b in zip(refinements,refinements[1:]))
    # Independent nested scalar loop at an off-target point tests phase and geometry.
    q=replace(p,samples_side=12); command=phase_command(q,bits=2); receiver=np.array([7.6,0,12.])
    v=0j; step=q.side_m/q.samples_side
    for iy in range(q.samples_side):
        for ix in range(q.samples_side):
            s=np.array([(ix+.5)*step-q.side_m/2,(iy+.5)*step-q.side_m/2,0])
            rt=np.sqrt(sum((s-tx)**2)); rr=np.sqrt(sum((s-receiver)**2))
            w=step**2*np.sqrt(q.efficiency*tx[2]*receiver[2])/(4*np.pi*(rt*rr)**1.5)
            v+=w*command[iy*q.samples_side+ix]*complex(np.cos(2*np.pi*28e9*(rt+rr)/C0),np.sin(2*np.pi*28e9*(rt+rr)/C0))
    loop_error=float(abs(v-channel(command,q,receiver))/abs(v)); assert loop_error<1e-10
    reverse=replace(p,tx_m=p.rx_m,rx_m=p.tx_m)
    reciprocal_error=float(abs(channel(g,reverse)-h)/abs(h)); assert reciprocal_error<1e-12
    # Broadside far-field plate/radar-equation normalization, constant physical area.
    far=replace(p,tx_m=(0.,0.,1000.),rx_m=(0.,0.,1200.))
    hf=channel(phase_command(far),far)
    analytic=far.side_m**2*np.sqrt(far.efficiency)/(4*np.pi*1000*1200)
    far_error=float(abs(hf/analytic-1)); assert far_error<1e-7
    assert abs(channel(phase_command(replace(far,side_m=far.side_m/2)),replace(far,side_m=far.side_m/2))/hf-.25)<1e-7
    # Scalar triangle bound and coherent reference, not an all-angle power proof.
    rng=np.random.default_rng(8)
    for _ in range(8):
        assert abs(channel(np.exp(1j*rng.uniform(-np.pi,np.pi,len(a))),p))<=a.sum()
    for bits in (1,2,3,4):
        assert abs(channel(phase_command(p,bits=bits),p))<=a.sum()*(1+1e-12)
    # Discontinuous quantized commands need their own sampling check.
    quantized_refinement=[]
    for nside in (48,96,192):
        q=replace(p,samples_side=nside)
        quantized_refinement.append(float(abs(channel(phase_command(q,bits=2),q))**2))
    quantized_spread=float(np.ptp(quantized_refinement)/quantized_refinement[-1])
    assert quantized_spread<.003
    # A frozen design must retain physical propagation phase off its design frequency.
    spectral_error=0.
    for frequency in (25.,31.):
        independent=sum(float(w)*complex(v)*complex(np.cos(2*np.pi*frequency*1e9*s/C0),
                        np.sin(2*np.pi*frequency*1e9*s/C0)) for w,v,s in zip(a,g,d))
        spectral_error=max(spectral_error,float(abs(independent-channel(g,p,frequency_GHz=frequency))/abs(h)))
    assert spectral_error<1e-11
    n=noise_power(p)
    assert abs(10*np.log10(n*1000)-(-173.97518719422808+80+7))<1e-8
    m=metrics(h,p); assert np.isclose(m['net_Mbps'],p.bandwidth_MHz*np.log2(1+10**(-2)*abs(h)**2/n))
    assert metrics(h,p,200,200)['net_Mbps']==0
    # Two independent Gaussian error moments integrated over the phase distribution.
    from scipy.integrate import quad
    sig=.7; moment=quad(lambda e:np.cos(e)*np.exp(-e*e/(2*sig*sig))/(np.sqrt(2*np.pi)*sig),-np.inf,np.inf)[0]
    expected=np.sum(a*a)+moment**2*(a.sum()**2-np.sum(a*a))
    moment_error=float(abs(expected-error_expectation(a,sig))/a.sum()**2); assert moment_error<1e-10
    assert np.isclose(error_expectation(a,0),a.sum()**2)
    assert np.isclose(error_expectation(a,20),np.sum(a*a),rtol=1e-12,atol=0)
    rows=training(p)
    assert all(r['net_Mbps']<=r['gross_Mbps'] for r in rows)
    # Physics checks against an independently sampled continuous-aperture sinc cut.
    u=np.linspace(-.8,.8,601); L=.48
    xm=((np.arange(4096)+.5)/4096-.5)*L
    numerical=np.mean(np.exp(2j*np.pi*xm[:,None]*u[None,:]/(C0/28e9)),axis=0)
    sinc_error=float(np.max(abs(numerical-np.sinc(L*u/(C0/28e9))))); assert sinc_error<2e-6
    invalid=[lambda:aperture(replace(p,side_m=-1)),lambda:aperture(replace(p,efficiency=1.1)),
        lambda:paths(p,rx=(0,0,0)),lambda:paths(p,frequency_GHz=0),lambda:phase_command(p,bits=0),
        lambda:channel(2*g,p),lambda:metrics(h,p,201),lambda:training(p,counts=(201,))]
    for call in invalid:
        try:call()
        except ValueError:pass
        else:raise AssertionError('Invalid input accepted')
    result=dict(status='passed',parameters=asdict(p),
        source_sha256=hashlib.sha256((ROOT/'simulations/communication_link.py').read_text(encoding='utf-8').encode()).hexdigest(),
        checks=dict(coherent_relative=coherent_error,adaptive_quadrature_relative=quad_error,
            independent_loop_relative=loop_error,reciprocity_relative=reciprocal_error,far_field_relative=far_error,
            Gaussian_moment_relative=moment_error,sinc_absolute=sinc_error,invalid_inputs=len(invalid),
            quantized_grid_power_spread=quantized_spread,off_frequency_relative=spectral_error),
        refinements=refinements,
        reference=dict(gain_dB=float(20*np.log10(abs(h))),noise_dBm=float(10*np.log10(n*1000)),
            snr_dB=float(10*np.log10(m['snr'])),gross_Mbps=float(m['net_Mbps']),
            plane_ratio=float(abs(channel(phase_command(p,mode='plane'),p)/h)**2),
            two_bit_ratio=float(abs(channel(phase_command(p,bits=2),p)/h)**2),
            training=rows),
        limits='Scalar aperture approximation only; no vector Maxwell solution or measured device/link validation.')
    out=ROOT/'data/chapter-08';out.mkdir(parents=True,exist_ok=True)
    (out/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result


if __name__=='__main__':print(json.dumps(validate(),indent=2))
