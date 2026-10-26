"""Chapter 8: declared scalar aperture channel, not a full-wave RIS solver.

Time convention exp(-i omega t). Outgoing paths have exp(+i k r).
Grid tiles are integration/control samples, not separately normalized antennas.
"""
from dataclasses import dataclass
import numpy as np

C0 = 299792458.
KB = 1.380649e-23


@dataclass(frozen=True)
class Link:
    frequency_GHz: float = 28.
    side_m: float = .48
    samples_side: int = 96
    tx_m: tuple = (-10., 0., 20.)
    rx_m: tuple = (8., 0., 12.)
    efficiency: float = .8
    tx_gain: float = 1.
    rx_gain: float = 1.
    power_dBm: float = 10.
    bandwidth_MHz: float = 100.
    noise_figure_dB: float = 7.
    temperature_K: float = 290.


def aperture(p=Link()):
    scalars = [p.frequency_GHz, p.side_m, p.tx_gain, p.rx_gain,
               p.bandwidth_MHz, p.temperature_K]
    if not all(np.isfinite(scalars)) or min(scalars) <= 0:
        raise ValueError('Frequency, size, gains, bandwidth and temperature must be positive.')
    if not isinstance(p.samples_side, (int, np.integer)) or p.samples_side < 2:
        raise ValueError('Use at least two integration samples per side.')
    if not np.isfinite(p.efficiency) or not 0 <= p.efficiency <= 1:
        raise ValueError('Efficiency must be in [0, 1].')
    if not np.isfinite(p.power_dBm) or not np.isfinite(p.noise_figure_dB) or p.noise_figure_dB < 0:
        raise ValueError('Use finite power and a nonnegative receiver noise figure.')
    x = ((np.arange(p.samples_side)+.5)/p.samples_side-.5)*p.side_m
    xx, yy = np.meshgrid(x, x)
    return np.column_stack([xx.ravel(), yy.ravel(), np.zeros(xx.size)]), (p.side_m/p.samples_side)**2


def paths(p=Link(), rx=None, frequency_GHz=None):
    xyz, da = aperture(p)
    f = p.frequency_GHz if frequency_GHz is None else float(frequency_GHz)
    if not np.isfinite(f) or f <= 0:
        raise ValueError('Positive frequency required.')
    tx = np.asarray(p.tx_m, float)
    rx = np.asarray(p.rx_m if rx is None else rx, float)
    for v in (tx, rx):
        if v.shape != (3,) or not np.all(np.isfinite(v)) or v[2] <= 0:
            raise ValueError('Nodes must be finite xyz points above the aperture.')
        # Conservative teaching-domain restriction, not a universal near-field boundary.
        if np.linalg.norm(v) < max(2*p.side_m, 10*C0/(f*1e9)):
            raise ValueError('Node too close for this restricted scalar model.')
    rt, rr = np.linalg.norm(xyz-tx, axis=1), np.linalg.norm(xyz-rx, axis=1)
    weights = da*np.sqrt(p.tx_gain*p.rx_gain*p.efficiency*(tx[2]/rt)*(rx[2]/rr))/(4*np.pi*rt*rr)
    return xyz, rt+rr, weights


def phase_command(p=Link(), target=None, mode='focus', bits=None):
    xyz, distance, _ = paths(p, target)
    if mode == 'plane':
        t = np.asarray(p.tx_m); r = np.asarray(p.rx_m if target is None else target)
        distance = np.linalg.norm(t)+np.linalg.norm(r)-xyz@(t/np.linalg.norm(t)+r/np.linalg.norm(r))
    elif mode != 'focus':
        raise ValueError('Unknown phase law.')
    # Common phase makes the unquantized target channel real and positive.
    phase = -2*np.pi*p.frequency_GHz*1e9/C0*distance
    if bits is not None:
        if not isinstance(bits, (int, np.integer)) or not 1 <= bits <= 8:
            raise ValueError('Use 1 to 8 phase bits.')
        step = 2*np.pi/2**bits
        phase = step*np.floor(phase/step+.5)
    return np.exp(1j*phase)


def channel(command, p=Link(), rx=None, frequency_GHz=None):
    _, distance, weights = paths(p, rx, frequency_GHz)
    command = np.asarray(command, complex)
    if command.shape != weights.shape or not np.all(np.isfinite(command)) or np.max(abs(command)) > 1+1e-12:
        raise ValueError('One passive complex coefficient per integration sample is required.')
    f = p.frequency_GHz if frequency_GHz is None else frequency_GHz
    return np.sum(weights*command*np.exp(2j*np.pi*f*1e9/C0*distance))


def noise_power(p=Link()):
    aperture(p)
    return KB*p.temperature_K*p.bandwidth_MHz*1e6*10**(p.noise_figure_dB/10)


def metrics(h, p=Link(), pilots=0, coherence=200):
    if not isinstance(pilots, (int, np.integer)) or not isinstance(coherence, (int, np.integer)) or coherence <= 0 or not 0 <= pilots <= coherence:
        raise ValueError('Pilot count must be an integer within the coherence block.')
    if not np.all(np.isfinite(h)):
        raise ValueError('Finite channel required.')
    pr = 10**((p.power_dBm-30)/10)*np.abs(h)**2
    snr = pr/noise_power(p)
    se = np.log2(1+snr)
    return dict(received_W=pr, snr=snr, spectral_efficiency=se,
                net_Mbps=(1-pilots/coherence)*p.bandwidth_MHz*se)


def error_expectation(weights, sigma_rad):
    """Exact ensemble mean for independent, zero-mean Gaussian phase errors."""
    a = np.asarray(weights, float); sigma = np.asarray(sigma_rad, float)
    if np.any(a < 0) or not np.all(np.isfinite(a)) or np.any(sigma < 0) or not np.all(np.isfinite(sigma)):
        raise ValueError('Use nonnegative weights and phase-error deviation.')
    diagonal = np.sum(a*a)
    return diagonal+np.exp(-sigma*sigma)*(a.sum()**2-diagonal)


def training(p=Link(), user_x=8.37, counts=(1,3,5,9,17,33,65), coherence=200):
    rows = []
    user = (user_x, 0., p.rx_m[2])
    for count in counts:
        if not isinstance(count, (int, np.integer)) or not 1 <= count <= coherence:
            raise ValueError('Codebook count must fit the coherence block.')
        targets = np.array([8.]) if count == 1 else np.linspace(4., 12., count)
        gains = np.array([abs(channel(phase_command(p, (x,0.,p.rx_m[2])), p, user))**2 for x in targets])
        i = int(np.argmax(gains)); m = metrics(np.sqrt(gains[i]), p, count, coherence)
        rows.append(dict(count=int(count), selected_x=float(targets[i]), gain=float(gains[i]),
                         gross_Mbps=float(p.bandwidth_MHz*m['spectral_efficiency']), net_Mbps=float(m['net_Mbps'])))
    return rows
