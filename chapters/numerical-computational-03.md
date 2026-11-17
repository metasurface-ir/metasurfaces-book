---
title: "Four different questions about error"
---

# Four different questions about error

For a discrete system $A_h u_h=b_h$ and a reported complex transmission $t_h$, define

$$
\rho_h=\frac{\|A_hu_h-b_h\|_2}{\|b_h\|_2},\qquad
\delta_P=|1-R_h-T_{h,\mathrm{net}}|,\qquad e_t=|t_h-t_{\mathrm{exact}}|.
$$

The residual asks how closely we solved the assembled equations. Power balance checks a conservation identity of the discrete problem. The amplitude error asks how closely that problem predicts a known continuum solution. Model discrepancy asks whether either idealized problem describes a real device. Small values of the first two do not bound the last two.

Keep geometry, material uncertainty, discretization, artificial boundaries, algebraic solution, and observable extraction separate in an error budget. Their effects may be correlated; adding them in quadrature requires a justified statistical model. A missing polarization or a wrong material law survives mesh refinement.
