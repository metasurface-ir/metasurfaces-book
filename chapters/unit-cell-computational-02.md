---
title: "Define the electromagnetic experiment"
---

(3-2-define-the-electromagnetic-experiment)=

# Define the electromagnetic experiment

A unit cell describes a structure repeated indefinitely under a specified Bloch excitation. Its response includes interactions with that repeated environment. When every ridge width changes, the entire periodic environment changes along with it.

The reference cell has a ridge centered at $x=0$, width $w$, height $h$, period $\Lambda$, and invariance along $y$. The layer occupies $0<z<h$. Air lies above it at $z<0$ and a homogeneous substrate below at $z>h$. Illumination travels toward positive $z$.

| Quantity | Reference value | Role |
| --- | --- | --- |
| $\Lambda$ | $0.65\,\mu\mathrm m$ | Repeat along $x$ |
| $w$ | $0.08$–$0.57\,\mu\mathrm m$ | Swept ridge width, 50 samples |
| $h$ | $0.60\,\mu\mathrm m$ | Fixed patterned-layer thickness |
| $\lambda_0$ | $1.55\,\mu\mathrm m$ | Free-space wavelength |
| $n_r$, $n_g$ | 2.4, 1.0 | Ridge and gap indices |
| $n_i$, $n_t$ | 1.0, 1.5 | Incident medium and substrate |
| $\theta_i$ | $0^\circ$ | Reference incidence |
| Polarization | TE, $\mathbf E=\hat{\mathbf y}E_y$, $k_y=0$ | Scalar Maxwell reduction |

All indices are positive, real, constant, and nonmagnetic. They define an ideal dielectric model without assigning measured material properties. A research library should use a stated dispersion model and measured or otherwise justified optical constants.

The incident $E_y$ equals one at $z=0$; reflected coefficients are referenced to $z=0$ and transmitted coefficients to $z=h$. Keeping these two reference faces fixed makes the width comparison meaningful.
