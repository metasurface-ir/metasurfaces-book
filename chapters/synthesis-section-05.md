---
title: "5.5 Amplitude synthesis and power management"
---

# 5.5 Amplitude synthesis and power management

Phase is only half the story. Low sidelobes, Taylor or Chebyshev tapering, and holography require amplitude control. For a passive, power-normalized two-channel model, reflected power, transmitted power and absorption sum to one. If diffraction or polarization conversion opens extra ports, include them in the sum.

There are three routes to a smaller selected amplitude: dissipate energy using resistive loading; redirect it between reflection and transmission; or convert it into the orthogonal polarization. Resistive sheets or lumped resistors make the design convenient but heat the material. A lossless splitter redirects power rather than losing it. An ideal rotated half-wave plate produces a co-polarized linear amplitude proportional to $\cos2\theta$ and a cross-polarized amplitude proportional to $\sin2\theta$; a sign change also changes phase.

Changing one patch dimension generally changes amplitude and phase together. Two geometric coordinates, for example length and slot width, provide more freedom but do not guarantee independence. Build a two-dimensional complex-response library and minimize an amplitude/phase error with a wrapped phase difference. Check feasibility and coupling in the final device.


$$
|S_{11}|^2+|S_{21}|^2+A=1,\qquad A\ge0.
$$
$$
\mathcal E(L,W)=w_A\left(|S_{21}(L,W)|-|S_{21,\rm target}|\right)^2
+w_\psi\left[\arg\left(e^{i(\arg S_{21}-\psi_{\rm target})}\right)\right]^2,
\quad (L_{mn},W_{mn})=\operatorname*{arg\,min}_{L,W}\mathcal E.
$$


:::{admonition} Worked exercise 1
:class: tip
A lossless cell has $|S_{11}|=0.6$. Find its transmission amplitude and power. The target amplitudes at three positions are $[0.8,0.6,0.3]$ with signed target phases $[30,120,210]^\circ$. What reflection amplitude supports transmission 0.3 without loss? Why use two geometric variables, and how would you select them? Finally compute absorption for $|S_{11}|=0.5$, $|S_{21}|=0.4$.

```{dropdown} Show the answer

$$
|S_{21}|=\sqrt{1-0.6^2}=0.8,\qquad T=0.64,\quad R=0.36.
$$
$$
|S_{11}|=\sqrt{1-0.3^2}=\sqrt{0.91}\simeq0.954,\qquad T=0.09,\quad R=0.91.
$$
$$
A=1-0.5^2-0.4^2=1-0.25-0.16=0.59.
$$


The original cell provides the target amplitude 0.8, but its phase must also be checked. Transmission amplitude 0.3 leaves 91% reflected power. Sweep both length and slot width, save complex responses, compare amplitude and circular phase error, choose a feasible pair and verify the full array. One variable usually changes both amplitude and phase, so it does not supply independent control. Resistive loading converts 59% of input power into heat in the final example.
```
:::

