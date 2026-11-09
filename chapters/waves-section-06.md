---
title: "2.6 Frequency-domain wave analysis"
short_title: "2.6 Frequency-domain wave analysis"
---

(ch02-source-06)=
# 2.6 Frequency-domain wave analysis

As we saw in the phasor discussion, many electromagnetic problems, especially metasurface designs, examine fields at one or several specified operating frequencies. Using $e^{j\omega t}$ turns time derivatives into multiplication by $j\omega$. This simple trick replaces complicated time-domain differential equations with much more familiar algebraic frequency-domain relations.

Under this assumption, the Maxwell curl equations in a linear, homogeneous, isotropic medium become:

$$
\nabla\times\mathbf E=-j\omega\mu\mathbf H,
\qquad
\nabla\times\mathbf H=(\sigma+j\omega\varepsilon)\mathbf E.
$$

Here $\sigma$ is conductivity, $\varepsilon$ permittivity, and $\mu$ permeability. The quantity $\sigma+j\omega\varepsilon$ can be viewed as an effective complex bulk admittivity: it combines conduction current, representing ohmic loss, and displacement current, representing dielectric response.

Frequency-domain analysis is the shared language of reference books and simulation packages such as CST and HFSS. It lets us include substrate and metal losses directly in wave-propagation parameters.

