"""Independently evaluate Chapter 6 worked arithmetic; no full-wave run is implied."""
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def evaluate():
    eps, mu, sigma, dz, dt = 4 * 8.854e-12, 4 * np.pi * 1e-7, .02, 1e-3, 3.3e-12
    a = sigma * dt / (2 * eps)
    ca, cb = (1-a)/(1+a), dt/(eps*dz)/(1+a)
    h = .004-dt/(mu*dz)*(.6)
    e = ca*2.5-cb*(.0036-.0028)
    assert abs(h-.002424366063)<1e-11 and abs(e-2.421)<.001
    Z = np.array([[50+20j,10-5j,5+2j],[10-5j,45+18j,8-4j],[5+2j,8-4j,40+15j]])
    V = np.array([1,.8*np.exp(-1j*np.pi/6),.4*np.exp(1j*np.pi/4)])
    I = np.linalg.solve(Z,V)
    printed = np.array([.01735-.00854j,.00856-.00819j,.00555+.00513j])
    residual = float(np.linalg.norm(Z@I-V)/np.linalg.norm(V))
    printed_residual = float(np.linalg.norm(Z@printed-V)/np.linalg.norm(V))
    assert residual<1e-14 and printed_residual>.16
    circulation = .30+.20-.10-.05
    flux = 2e-10-1e-12*circulation
    hint = flux/(mu*dz)
    assert np.isclose(flux,1.9965e-10,rtol=1e-14,atol=0)
    order = np.arange(-2,3)
    q = .5+.75*order
    assert np.allclose(q,[-1,-.25,.5,1.25,2])
    phase = -110+360*(2*10*np.cos(np.pi/6)/30)
    assert abs(phase-97.846096908)<1e-8
    r,t = -.30j,.60-.20j
    z = np.sqrt(((1+r)**2-t*t)/((1-r)**2-t*t))
    if z.real<0:z=-z
    interface = (z-1)/(z+1)
    propagation = t/(1-r*interface)
    kd = 2*np.pi/30*6
    n = 1j*np.log(propagation)/kd
    r_back = interface*(1-propagation**2)/(1-interface**2*propagation**2)
    t_back = propagation*(1-interface**2)/(1-interface**2*propagation**2)
    assert abs(r_back-r)<1e-14 and abs(t_back-t)<1e-14 and n.imag<0
    gamma = np.exp(-1j*2*np.pi/3)
    zs = 377*(1+gamma)/(1-gamma)
    shortcut = 377/np.tan(np.angle(gamma)/2)
    assert abs(zs.real)<1e-12 and abs(zs.imag-shortcut)<1e-12
    # A purely electric shunt must satisfy both t=1+r and its two-port formula.
    sheet_y = .004+.002j
    sheet_t = 2/(2+377*sheet_y)
    sheet_r = sheet_t-1
    recovered_y = 2/377*(1/sheet_t-1)
    printed_y = 2/377*(1-sheet_t-sheet_r)/sheet_t
    assert abs(recovered_y-sheet_y)<1e-14 and abs(printed_y-2*sheet_y)<1e-14
    pair=lambda v:[float(v.real),float(v.imag)]
    return dict(scope='Arithmetic/linear algebra of textbook problems; not a FEM/FDTD/FIT/MoM device simulation',
        fdtd=dict(Ca=ca,Cb_with_spatial_step=cb,H_new_A_per_m=h,E_new_V_per_m=e),
        mom=dict(currents_A=[pair(v) for v in I],magnitudes_mA=(abs(I)*1000).tolist(),phases_deg=np.angle(I,deg=True).tolist(),relative_residual=residual,printed_relative_residual=printed_residual,dense_matrix_bytes_50000=16*50000**2),
        fit=dict(circulation_V=circulation,flux_Wb=flux,magnetic_line_integral_A=hint),
        rcwa=dict(orders=order.tolist(),normalized_kx=q.tolist()),
        periodic=dict(surface_phase_deg=phase),
        retrieval=dict(z=pair(z),interface_r=pair(interface),internal_T=pair(propagation),n_branch_zero=pair(n),epsilon=pair(n/z),mu=pair(n*z),reflection_roundtrip_error=abs(r_back-r),transmission_roundtrip_error=abs(t_back-t),grounded_Z_ohm=pair(zs),electric_shunt_check='passed'),
        limitations=['One-frequency slab roundtrip is not proof of homogenization or unique branch selection','FDTD values use two separately prescribed neighboring H states','MoM matrix is a supplied three-unknown teaching system'])


if __name__ == '__main__':
    result=evaluate()
    path=ROOT/'data/chapter-06/textbook-checks.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
