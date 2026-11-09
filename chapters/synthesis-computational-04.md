---
title: "Spatial sampling and phase quantization"
---

# Spatial sampling and phase quantization


Divide one period into $N$ intervals of pitch $p=L/N$. Assign a complex value $t_j$ to interval $j$, whose center is $x_j=(j+1/2)p$. The exact Fourier coefficient of this **staircase field** is

$$
C_m=\operatorname{sinc}\left(\frac{m}{N}\right)
\frac{1}{N}\sum_{j=0}^{N-1}t_j
e^{-2\pi (-i) m(j+1/2)/N},
\qquad \operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.
$$

The sinc factor represents each finite-width interval. A discrete sum without this factor describes a different source model. For ideal samples $t_j=e^{2\pi (-i)(j+1/2)/N}$,

$$
|C_{+1}|^2=\operatorname{sinc}^2(1/N).
$$

For six levels this coefficient fraction is about 0.9119. It is a property of the scalar staircase field, not a full-wave device efficiency. Physical order powers additionally require flux normalization and a consistent scattering solution.

A sufficient local sampling condition for a phase-only target is $p\,\max|d\Phi/dx|<\pi$, which avoids exceeding the phase-gradient Nyquist limit. This alone does not exclude additional physical diffraction channels or prove that a local-response approximation is accurate. Use the actual primitive/supercell period and exterior light cones as well.

