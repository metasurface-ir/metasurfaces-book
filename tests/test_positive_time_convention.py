"""Independent physical sign checks for the course's exp(+i*omega*t) contract."""
import sys
import unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'simulations'))
from waves_interfaces import interface,te_interface_fields,film
from intro_sheet import response,channel_group_delay_fs
from materials_measurement import lorentz
from tunable_surface import response as circuit,Surface
from unit_cell_te import Cell,solve_cell,sample_ey,deembed_te

class PositiveTimeTests(unittest.TestCase):
    def test_faraday_sign_for_a_forward_field(self):
        wavelength=.6;k0=2*np.pi/wavelength;z=-.2;h=1e-6
        fields=te_interface_fields(.1,z,n1=1,n2=1,angle_deg=0,wavelength_um=wavelength)
        derivative=(te_interface_fields(.1,z+h,n1=1,n2=1,angle_deg=0,wavelength_um=wavelength)['E']-
                    te_interface_fields(.1,z-h,n1=1,n2=1,angle_deg=0,wavelength_um=wavelength)['E'])/(2*h)
        self.assertLess(abs(-derivative-(-1j*k0*fields['Hx_eta0'])),1e-8)
    def test_outgoing_evanescent_root_decays(self):
        q=interface(1.5,1,50)['q2'];self.assertLess(q.imag,0)
        amplitude=abs(np.exp(-1j*q*np.linspace(0,3,20)))
        self.assertTrue(np.all(np.diff(amplitude)<0))
    def test_passive_material_loss_and_index(self):
        epsilon=lorentz(np.linspace(1,30,31));self.assertTrue(np.all(epsilon.imag<0))
        index=np.sqrt(epsilon);self.assertTrue(np.all(index.imag<0))
        self.assertTrue(np.all(-epsilon.imag>0))
        self.assertTrue(np.all(abs(np.exp(-1j*index))<1))
    def test_lumped_reactance_signs(self):
        p=Surface();omega=2*np.pi*10e9;C=p.capacitance0_pF*1e-12
        expected=omega*p.inductance_nH*1e-9-1/(omega*C)
        self.assertAlmostEqual(float(circuit(10,0,p)['reactance_ohm']),expected)
    def test_delay_is_negative_phase_derivative(self):
        step=.001;tp=response(200+step)['t'];tm=response(200-step)['t']
        delay=-1000*np.angle(tp*np.conj(tm))/(4*np.pi*step)
        self.assertGreater(delay,0)
        self.assertAlmostEqual(float(delay),float(channel_group_delay_fs(200,200,.25)),places=6)
    def test_transmission_exit_plane_has_negative_propagation_phase(self):
        t=film(1,1,1,.15,.6)['t'];self.assertLess(abs(t+1j),1e-13)
    def test_bloch_translation_has_negative_phase(self):
        c=Cell(angle_deg=15);v=solve_cell(c,8)
        field=sample_ey(c,v,[.07,.07+c.period_um],[.23])[0]
        multiplier=np.exp(-1j*2*np.pi/c.wavelength_um*c.n_incident*np.sin(np.deg2rad(c.angle_deg))*c.period_um)
        self.assertLess(abs(field[1]-field[0]*multiplier),1e-12)
    def test_reference_plane_removal_inverts_negative_path_phase(self):
        wavelength=1.55;k0=2*np.pi/wavelength;Li=.2;Lt=.3;r=.2+.1j;t=.7-.2j
        rm=r*np.exp(-2j*k0*Li);tm=t*np.exp(-1j*k0*(Li+1.5*Lt))
        rd,td=deembed_te(rm,tm,wavelength,1,1.5,Li,Lt)
        self.assertLess(abs(rd-r)+abs(td-t),1e-14)

if __name__=='__main__':unittest.main()
