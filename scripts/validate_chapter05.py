"""Audit Chapter 5 full-wave supercells and scalar/Jones model limits.

python scripts/validate_chapter05.py --grcwa
The optional comparison needs requirements-validation.txt, and uses a separate
RCWA implementation rather than an independent FEM/FDTD method.
"""
import argparse
from dataclasses import replace
import hashlib
import importlib.metadata
import json
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'simulations'))
from unit_cell_te import Cell,solve_cell
from metasurface_synthesis import solve_supercell,staircase_coefficients,angular_spectrum_1d,rotated_jones,line_fwhm


def external_supercell(widths,height,M,pixels):
    import grcwa
    pitch=.65;period=pitch*len(widths)
    obj=grcwa.obj(2*M+3,[period,0],[0,period/1000],1/1.55,0.,0.,verbose=0)
    obj.Add_LayerUniform(0,1.);obj.Add_LayerGrid(height,pixels,1);obj.Add_LayerUniform(0,1.5**2)
    obj.Init_Setup()
    assert obj.nG==2*M+1 and np.all(obj.G[:,1]==0)
    edges=np.linspace(0,period,pixels+1);dx=period/pixels
    fraction=np.zeros(pixels)
    for j,w in enumerate(widths):
        center=(j+.5)*pitch
        fraction+=np.maximum(0,np.minimum(edges[1:],center+w/2)-np.maximum(edges[:-1],center-w/2))/dx
    obj.GridLayer_geteps(1+(2.4**2-1)*fraction)
    obj.MakeExcitationPlanewave(0,0,1,0)
    R,T=obj.RT_Solve(normalize=1,byorder=1)
    E,_=obj.Solve_FieldFourier(2,0)
    return dict(alpha=np.asarray(obj.kx)*1.55/(2*np.pi),R=np.asarray(R),T=np.asarray(T),t0=complex(E[1][0]))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--grcwa',action='store_true');args=parser.parse_args()
    data=json.loads((ROOT/'data/chapter-05/beam-steering.json').read_text())
    wave=json.loads((ROOT/'data/chapter-05/wavefront-models.json').read_text())
    for name,digest in data['metadata']['source_sha256'].items():
        assert hashlib.sha256((ROOT/'simulations'/name).read_bytes()).hexdigest()==digest
    assert wave['source_sha256']==data['metadata']['source_sha256']['metasurface_synthesis.py']
    assert len(data['extended_library'])==161 and all(r['accepted'] for r in data['extended_library'])
    assert all(max(r['delta_T'],r['delta_R'])<1e-4 for c in data['cases'] for r in c['orders'])
    assert all(r['delta_complex_t']<1e-4 for c in data['cases'] for r in c['orders'] if r['transmission_open'])
    primitive=solve_cell(replace(Cell(),height_um=1.8),12)
    repeated=solve_supercell([.325]*6,height_um=1.8,half_order=72)
    embedding_error=max(abs(primitive['t'][12]-repeated['t'][72]),abs(primitive['r'][12]-repeated['r'][72]))
    forbidden=abs(repeated['orders'])%6!=0
    forbidden_error=max(np.max(abs(repeated['t'][forbidden])),np.max(abs(repeated['r'][forbidden])))
    assert embedding_error<1e-10 and forbidden_error<1e-10
    cases={c['name']:c for c in data['cases']}
    reversed_orders={r['m']:r for r in cases['reversed']['orders']}
    mirror=max(max(abs(r['T']-reversed_orders[-r['m']]['T']),abs(r['R']-reversed_orders[-r['m']]['R'])) for r in cases['expanded']['orders'])
    assert mirror<1e-10
    quantization=[]
    for N in [2,3,4,6,8,16]:
        target=np.exp(2j*np.pi*(np.arange(N)+.5)/N)
        coefficient=staircase_coefficients(target,np.array([1]))[0]
        error=abs(abs(coefficient)**2-np.sinc(1/N)**2)
        assert error<1e-12
        quantization.append(dict(levels=N,coefficient_fraction=float(abs(coefficient)**2),error=float(error)))
    x=np.linspace(-4,4,8001)
    gaussian_error=abs(line_fwhm(x,np.exp(-x*x))-2*np.sqrt(np.log(2)))
    assert gaussian_error<1e-6
    plane=np.exp(2j*np.pi*3*np.arange(1024)/1024)
    dx=.1;wavelength=1.55;index=1.5;z=30.
    k=2*np.pi*index/wavelength;kx=2*np.pi*3/(1024*dx)
    propagated=angular_spectrum_1d(plane,dx,wavelength,z,index)
    propagation_error=float(np.max(abs(propagated-plane*np.exp(1j*np.sqrt(k*k-kx*kx)*z))))
    assert propagation_error<1e-10
    jones_error=0.
    for sigma in [-1,1]:
        incident=np.array([1,1j*sigma])/np.sqrt(2);converted=np.conj(incident)
        for theta in np.linspace(0,np.pi,91):
            jones_error=max(jones_error,float(abs(np.vdot(converted,rotated_jones(1,-1,theta)@incident)-np.exp(2j*sigma*theta))))
    assert jones_error<1e-12
    report=dict(status='passed',source_sha256=data['metadata']['source_sha256'],library_rows=161,
                primitive_embedding_complex_error=float(embedding_error),
                forbidden_supercell_amplitude=float(forbidden_error),mirror_order_power_error=float(mirror),
                quantized_ramp=quantization,scalar_plane_wave_error=propagation_error,gaussian_fwhm_error=float(gaussian_error),jones_error=jones_error,
                full_wave_refinement=dict(half_orders=[144,192],max_open_order_power_change=max(max(r['delta_T'],r['delta_R']) for c in data['cases'] for r in c['orders']),max_open_complex_t_change=max(r['delta_complex_t'] for c in data['cases'] for r in c['orders'] if r['transmission_open'])),
                model_limits=['1D lossless TE infinite periodic supercells','Scalar line focusing is not a full-wave lens','Jones polarization model is independent of the TE ridge','No fabricated-device or independent FEM/FDTD validation'])
    if args.grcwa:
        comparisons=[]
        for name in ['limited','expanded','reversed']:
            c=cases[name];ours=solve_supercell(c['widths_um'],height_um=c['height_um'],half_order=48)
            refinements=[]
            for pixels in [512,4096]:
                other=external_supercell(c['widths_um'],c['height_um'],48,pixels)
                mapping=np.array([np.argmin(abs(ours['alpha']-v)) for v in other['alpha']])
                assert np.max(abs(ours['alpha'][mapping]-other['alpha']))<1e-10
                dp=max(np.max(abs(ours['T'][mapping]-other['T'])),np.max(abs(ours['R'][mapping]-other['R'])))
                dt=abs(ours['t'][48]-other['t0'])
                refinements.append(dict(raster_pixels=pixels,max_order_power_error=float(dp),complex_t0_error=float(dt)))
            assert refinements[-1]['max_order_power_error']<1e-4 and refinements[-1]['complex_t0_error']<1e-4
            comparisons.append(dict(case=name,refinements=refinements))
        report['independent_implementation']=dict(package='grcwa',version=importlib.metadata.version('grcwa'),half_order=48,tolerance=1e-4,cases=comparisons,interpretation='Separate RCWA implementation with raster refinement; same numerical method family.')
    else:report['independent_implementation']=dict(status='not run; use --grcwa')
    (ROOT/'data/chapter-05/validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
