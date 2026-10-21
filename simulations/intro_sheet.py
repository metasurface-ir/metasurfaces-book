"""Chapter 1 analytical sheet model; not a geometry or Maxwell solver.

Normal incidence, equal real wave impedance on both sides, one polarization,
only specular ports, exp(-i omega t). All frequencies use THz. Responses are
field ratios with reference planes at the ideal sheet. The unitary two-port
matrix is reciprocal and mirror symmetric by construction.
"""
from dataclasses import dataclass, asdict
import numpy as np

MODEL_VERSION='intro-sheet-1.0'


@dataclass(frozen=True)
class Sheet:
    electric_frequency_THz: float=200.
    magnetic_frequency_THz: float=200.
    electric_strength: float=.25
    magnetic_strength: float=.25

    def validate(self):
        values=np.asarray(list(asdict(self).values()))
        if np.iscomplexobj(values) or not np.all(np.isfinite(values)):
            raise ValueError('Parameters must be finite real values.')
        if min(self.electric_frequency_THz,self.magnetic_frequency_THz)<=0:
            raise ValueError('Resonance frequencies must be positive.')
        if min(self.electric_strength,self.magnetic_strength)<0:
            raise ValueError('Channel strengths must be nonnegative.')


PRESETS={
    'transparent':Sheet(electric_strength=0.,magnetic_strength=0.),
    'electric':Sheet(magnetic_strength=0.),
    'balanced':Sheet(),
    'detuned':Sheet(magnetic_frequency_THz=230.)
}


def allpass_channel(frequency_THz,resonance_THz,strength):
    """C=(d+i a u)/(d-i a u), u=f/f0, d=1-u^2; C=1 for a=0.

    This rational form remains finite at resonance for a>0, unlike first
    evaluating the divergent reactance x=a*u/(1-u^2).
    """
    f=np.asarray(frequency_THz)
    if np.iscomplexobj(f) or not np.all(np.isfinite(f)) or np.any(f<=0):
        raise ValueError('Frequencies must be finite positive real values.')
    if not np.isfinite(resonance_THz) or resonance_THz<=0 or not np.isfinite(strength) or strength<0:
        raise ValueError('Use a positive resonance and a nonnegative strength.')
    if strength==0:return np.ones_like(f,dtype=complex)
    u=f/resonance_THz;d=1-u*u;v=strength*u
    return (d+1j*v)/(d-1j*v)


def response(frequency_THz,sheet=Sheet(),phase_floor=1e-12):
    """Return specular amplitudes, power fractions, and meaningful t phase."""
    sheet.validate()
    if not np.isfinite(phase_floor) or phase_floor<=0:
        raise ValueError('The amplitude phase floor must be positive.')
    ce=allpass_channel(frequency_THz,sheet.electric_frequency_THz,sheet.electric_strength)
    cm=allpass_channel(frequency_THz,sheet.magnetic_frequency_THz,sheet.magnetic_strength)
    r=(ce-cm)/2;t=(ce+cm)/2
    R=abs(r)**2;T=abs(t)**2
    phase=np.where(abs(t)>phase_floor,np.rad2deg(np.angle(t)),np.nan)
    return dict(ce=ce,cm=cm,r=r,t=t,R=R,T=T,phase_deg=phase,
                balance_error=abs(1-R-T))


def channel_group_delay_fs(frequency_THz,resonance_THz,strength):
    """Exact d(arg C)/d(angular frequency), expressed in femtoseconds."""
    allpass_channel(frequency_THz,resonance_THz,strength)  # shared domain checks
    f=np.asarray(frequency_THz)
    if strength==0:return np.zeros_like(f,dtype=float)
    u=f/resonance_THz
    slope=2*strength*(1+u*u)/(resonance_THz*((1-u*u)**2+(strength*u)**2))
    return 1000*slope/(2*np.pi)


def scattering_matrix(frequency_THz,sheet=Sheet()):
    """S maps left/right incoming field amplitudes to left/right outgoing ones."""
    v=response(frequency_THz,sheet)
    return np.stack([np.stack([v['r'],v['t']],axis=-1),
                     np.stack([v['t'],v['r']],axis=-1)],axis=-2)
