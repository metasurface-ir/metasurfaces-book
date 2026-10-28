"""Labs ms-09/10/11: restricted TE ridge studies, with explicit model checks.

Lengths: micrometers. Time convention exp(-i omega t). Fixed real indices
describe structural dispersion only. Numerical controls never change geometry.
"""
from dataclasses import dataclass, asdict, replace
import numpy as np
from scipy.optimize import minimize
from unit_cell_te import Cell, solve_cell, outgoing_q
from metasurface_synthesis import solve_supercell, staircase_coefficients


@dataclass(frozen=True)
class Design:
    widths_um: tuple = (.159625, .2055625, .26375, .355625, .4689375, .1198125)
    pitch_um: float = .65
    height_um: float = 1.8
    wavelength_um: float = 1.55
    n_ridge: float = 2.4
    n_gap: float = 1.
    n_incident: float = 1.
    n_substrate: float = 1.5
    angle_deg: float = 0.

    def solve(self, half_order=96):
        return solve_supercell(**asdict(self), half_order=half_order)


def order_metrics(result, order=1):
    index = np.flatnonzero(result['orders'] == order)
    if len(index) != 1:
        raise ValueError('Requested order is absent from the retained basis.')
    j = index[0]
    return dict(T=float(result['T'][j]), R=float(result['R'][j]),
                t_real=float(result['t'][j].real), t_imag=float(result['t'][j].imag),
                total_T=result['T_total'], total_R=result['R_total'],
                balance_error=result['balance_error'], residual=result['solve_residual'])


def local_prediction(design, orders, half_order=32):
    """Piecewise constant mask from zero-order cell amplitudes at the two faces.

    Each cell is solved in its own infinite identical-neighbor array. The mask
    omits within-cell field variation and neighbor-dependent scattering.
    Its order powers need not sum to one; never renormalize them to hide this.
    """
    p = asdict(design)
    widths = p.pop('widths_um'); p['period_um'] = p.pop('pitch_um')
    cells = [solve_cell(Cell(width_um=w, **p), half_order) for w in widths]
    r = staircase_coefficients([s['r'][half_order] for s in cells], orders)
    t = staircase_coefficients([s['t'][half_order] for s in cells], orders)
    alpha0 = design.n_incident*np.sin(np.deg2rad(design.angle_deg))
    alpha = alpha0 + np.asarray(orders)*design.wavelength_um/(len(widths)*design.pitch_um)
    qi, qt = outgoing_q(design.n_incident, alpha), outgoing_q(design.n_substrate, alpha)
    q0 = float(outgoing_q(design.n_incident, alpha0).real)
    return dict(orders=np.asarray(orders), r=r, t=t, R=qi.real/q0*abs(r)**2, T=qt.real/q0*abs(t)**2)


def spectral_sweep(design, wavelengths, half_order=96, target_order=1):
    rows = []
    for wavelength in wavelengths:
        current = replace(design, wavelength_um=float(wavelength))
        result = current.solve(half_order)
        j = int(np.flatnonzero(result['orders'] == target_order)[0])
        if result['qt'][j].real <= 0:
            raise ValueError('Target order must be open throughout this study.')
        row = order_metrics(result, target_order)
        row.update(wavelength_um=float(wavelength),
                   angle_deg=float(np.rad2deg(np.arcsin(result['alpha'][j]/design.n_substrate))),
                   open_transmission_orders=int(np.count_nonzero(result['qt'].real > 0)))
        rows.append(row)
    return rows


def passband(x, margin, anchor):
    """Connected >=0 margin interval containing an explicitly sampled anchor.

    Linearly interpolate the first failing/pass pair on each side. Return
    clipping flags: reaching a scan endpoint is not a measured band edge.
    A failing anchor returns None, even if a disconnected passband exists.
    """
    x, y = np.asarray(x, float), np.asarray(margin, float)
    if x.ndim != 1 or len(x) < 3 or y.shape != x.shape or not np.all(np.isfinite([x, y])) or np.any(np.diff(x) <= 0):
        raise ValueError('Use matching finite arrays and strictly increasing sample coordinates.')
    matches = np.flatnonzero(np.isclose(x, anchor, atol=1e-12, rtol=0))
    if len(matches) != 1:
        raise ValueError('The anchor must be sampled exactly once.')
    i = int(matches[0])
    if y[i] < 0:
        return None
    left = right = i
    while left > 0 and y[left-1] >= 0: left -= 1
    while right < len(x)-1 and y[right+1] >= 0: right += 1
    def cross(a, b):
        return float(x[a]-y[a]*(x[b]-x[a])/(y[b]-y[a]))
    lo = float(x[0]) if left == 0 else cross(left-1, left)
    hi = float(x[-1]) if right == len(x)-1 else cross(right, right+1)
    return dict(lower_um=lo, upper_um=hi, width_um=hi-lo,
                fractional_wavelength_width=(hi-lo)/anchor,
                frequency_width_THz=299.792458*(1/lo-1/hi),
                left_clipped=left == 0, right_clipped=right == len(x)-1)


def bandwidth(rows, anchor=1.55, efficiency=.8, angle_tolerance_deg=None):
    """Intersect independently interpolated, anchor-connected constraints."""
    x = np.array([r['wavelength_um'] for r in rows])
    margin = np.array([r['T'] for r in rows])-efficiency
    power_band = passband(x, margin, anchor)
    if angle_tolerance_deg is not None:
        if not np.isfinite(angle_tolerance_deg) or angle_tolerance_deg <= 0:
            raise ValueError('Angular tolerance must be positive.')
        i = np.flatnonzero(np.isclose(x, anchor, atol=1e-12, rtol=0))
        if len(i) != 1: raise ValueError('Include the anchor wavelength in the sweep.')
        angle0 = rows[int(i[0])]['angle_deg']
        angular = angle_tolerance_deg-abs(np.array([r['angle_deg'] for r in rows])-angle0)
        angle_band = passband(x, angular, anchor)
        if power_band is None or angle_band is None:
            return None
        lo = max(power_band['lower_um'], angle_band['lower_um'])
        hi = min(power_band['upper_um'], angle_band['upper_um'])
        return dict(lower_um=lo, upper_um=hi, width_um=hi-lo,
                    fractional_wavelength_width=(hi-lo)/anchor,
                    frequency_width_THz=299.792458*(1/lo-1/hi),
                    left_clipped=power_band['left_clipped'] and angle_band['left_clipped'],
                    right_clipped=power_band['right_clipped'] and angle_band['right_clipped'])
    return power_band


def optimize_widths(design=Design(), starts=2, maxfev=1000, half_order=32,
                    bounds=(.08, .57), seed=17):
    """Bounded multi-start Powell search, retaining every queried candidate.

    Only the design wavelength enters the objective. Refinement, off-design
    wavelengths, perturbations, and the independent implementation are held
    out until the selected geometry is frozen. No global optimum is claimed.
    """
    lo, hi = bounds
    w0 = np.asarray(design.widths_um, float)
    if not 0 < lo < hi < design.pitch_um or np.any(w0 < lo) or np.any(w0 > hi):
        raise ValueError('Starting widths and bounds must lie strictly within a pitch.')
    if starts < 1 or maxfev < 1: raise ValueError('Use positive starts and budget.')
    rng = np.random.default_rng(seed)
    history, runs = [], []
    best = dict(T=-np.inf, widths_um=None)
    for run in range(starts):
        initial = w0.copy() if run == 0 else np.clip(w0+rng.normal(0, .025, len(w0)), lo, hi)
        def objective(widths):
            if np.any(widths < lo-1e-12) or np.any(widths > hi+1e-12):
                raise ValueError('Optimizer queried an out-of-bounds design.')
            value = order_metrics(replace(design, widths_um=tuple(widths)).solve(half_order))['T']
            if value > best['T']:
                best.update(T=value, widths_um=widths.tolist())
            history.append(dict(evaluation=len(history)+1, run=run, T=value,
                                best_T=best['T'], widths_um=widths.tolist()))
            return -value
        result = minimize(objective, initial, method='Powell', bounds=[bounds]*len(w0),
                          options=dict(maxfev=maxfev, xtol=2e-4, ftol=2e-5))
        runs.append(dict(run=run, success=bool(result.success), message=str(result.message),
                         evaluations=int(result.nfev), final_T=float(-result.fun)))
    return dict(best=best, runs=runs, history=history, settings=dict(starts=starts,
                maxfev=maxfev, half_order=half_order, bounds_um=list(bounds), seed=seed,
                objective='maximize incident-normalized +1 transmitted power at design wavelength'))


def grcwa_check(design, half_order=48, pixels=8192):
    """Optional separate RCWA implementation, pixel-average permittivity.

    Normal incidence only. Raster refinement is independent of harmonic
    refinement. This is not a second method such as FEM or FDTD.
    """
    if design.angle_deg != 0: raise ValueError('This comparison is normal-incidence only.')
    import grcwa
    period = len(design.widths_um)*design.pitch_um
    obj = grcwa.obj(2*half_order+3, [period, 0], [0, period/1000], 1/design.wavelength_um, 0., 0., verbose=0)
    obj.Add_LayerUniform(0, design.n_incident**2)
    obj.Add_LayerGrid(design.height_um, pixels, 1)
    obj.Add_LayerUniform(0, design.n_substrate**2)
    obj.Init_Setup()
    assert obj.nG == 2*half_order+1 and np.all(obj.G[:, 1] == 0)
    edges = np.linspace(0, period, pixels+1)
    fraction = np.zeros(pixels)
    for j, width in enumerate(design.widths_um):
        center = (j+.5)*design.pitch_um
        fraction += np.maximum(0, np.minimum(edges[1:], center+width/2)-np.maximum(edges[:-1], center-width/2))/(period/pixels)
    obj.GridLayer_geteps(design.n_gap**2+(design.n_ridge**2-design.n_gap**2)*fraction)
    obj.MakeExcitationPlanewave(0, 0, 1, 0)
    R, T = obj.RT_Solve(normalize=1, byorder=1)
    return dict(orders=np.asarray(obj.G[:, 0], int), R=np.asarray(R), T=np.asarray(T))
