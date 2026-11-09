---
title: "5.2 Specify the wave transformation"
---

# 5.2 Specify the wave transformation

Place the sheet at $z=0$ and describe its incident and desired outgoing fields. Their ratio gives a local scalar target when that approximation is appropriate. Define the phase lag as the outgoing lag minus the incident lag. The source writes a positive exponential for transmission beside this lag difference, which is algebraically inconsistent. Under our fixed positive-time convention, the ratio below uses a negative exponential; the signed transmission argument is the negative of the lag.

For steering, subtract the incident tangential phase from the outgoing one. For a metalens, compensate the extra distance to the focus. For a vortex, an integer charge produces a full $2\pi\ell$ winding; use atan2 rather than a single-quadrant arctangent. An OAM phase label alone does not guarantee extra communication capacity. Two practical obstacles remain: the normal power densities may not match, and locally periodic cells are coupled to their actual neighbors. A steep profile or strong resonance needs a supercell or finite-device check.


$$
E_{\rm inc}(\mathbf r)=A_{\rm inc}e^{-i\phi_{\rm inc}},\qquad
E_{\rm out}(\mathbf r)=A_{\rm out}e^{-i\phi_{\rm out}},\qquad\mathbf r=(x,y).
$$
$$
T(\mathbf r)=\frac{E_{\rm out}}{E_{\rm inc}}
=\frac{A_{\rm out}}{A_{\rm inc}}e^{-i\Phi},\qquad
\Phi=\phi_{\rm out}-\phi_{\rm inc}\pmod{2\pi}.
$$
$$
\Phi(x)=k_0x(\sin\theta_{\rm out}-\sin\theta_{\rm in}),\qquad
\frac{d\Phi}{dx}=k_0(\sin\theta_{\rm out}-\sin\theta_{\rm in}).
$$
$$
\Phi_{\rm lens}(x,y)=k_0\left(F-\sqrt{x^2+y^2+F^2}\right),\qquad
\Phi_{\rm vortex}(r,\varphi)=\ell\varphi,\quad\varphi=\operatorname{atan2}(y,x).
$$

