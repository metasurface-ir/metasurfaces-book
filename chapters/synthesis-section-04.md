---
title: "5.4 Phase calibration and physical cell placement"
---

# 5.4 Phase calibration and physical cell placement

Now connect the wave mathematics to a real metal patch or dielectric element. The locally periodic approximation replaces the actual neighborhood by identical copies. Slowly changing dimensions are a useful heuristic, not a sufficient accuracy criterion. A unit-cell simulation uses phase-linked lateral boundaries and modal ports in the exterior.

Sweep patch length $L$ at fixed period $p$, substrate thickness $h$ and permittivity. Record complex $S_{11}$ or $S_{21}$, magnitude and signed argument. Useful coverage must be evaluated at an amplitude threshold, with adequate sampling near a rapid phase variation. Sensitivity to fabrication follows the phase derivative with respect to geometry. The source mentions roughly 280–300 degrees for one thin single-resonance patch design, and suggests thicker substrates, coupled resonators such as dual rings or Jerusalem crosses, and multilayer stacks. Those numbers and layer spacings are design examples, not guarantees of full phase coverage and high transmission.

Sample the desired aperture; compute its target; choose geometry from the LUT using circular phase error; then verify the complete structure. A phase-lag target must be negated before comparing with a library of signed arguments. Mutual coupling, finite pitch, finite phase states, incidence angle and fabrication all matter. A small focal ratio raises the range of local ray angles, but does not by itself change the incident angle of a normally incident plane wave. Include the appropriate incident and outgoing conditions in the library or an improved model.


$$
S_{11}(L)=|S_{11}(L)|e^{i\psi(L)},\qquad\psi(L)=\arg S_{11}(L).
$$
$$
\delta\psi\simeq\frac{d\psi}{dL}\delta L,\qquad
e_\psi=\arg\left(S\,e^{-i\psi_{\rm target}}\right),\qquad
\psi_{\rm target}=-\Phi_{\rm target}.
$$


:::{admonition} Worked exercise 1
:class: tip
The calibration phases are $[0,45,90,135,180,225,270,315]^\circ$, at patch lengths $[1.0,1.4,1.8,2.2,2.6,3.0,3.4,3.8]\,\mathrm{mm}$. For requested signed phases $[20,70,130,185,240,290,340,15]^\circ$, select the nearest states, dimensions, wrapped errors and mean absolute error. Why may the real array differ, and what final check is needed?

```{dropdown} Show the answer

$$
\psi_{\rm sel}=[0,90,135,180,225,270,0,0]^\circ,
$$
$$
L=[1.0,1.8,2.2,2.6,3.0,3.4,1.0,1.0]\,\mathrm{mm}.
$$
$$
e=\operatorname{wrap}(\psi_{\rm sel}-\psi_{\rm req})
=[-20,20,5,-5,-15,-20,20,-15]^\circ,
\qquad\overline{|e|}=\frac{20+20+5+5+15+20+20+15}{8}=15^\circ.
$$


Compare circular distances, not ordinary subtraction. In particular, 340 degrees is only 20 degrees from zero. Coupling, incidence-angle changes, phase discretization and fabrication perturb the result. Verify the full array: main-beam angle, sidelobes and grating lobes, reflected power/efficiency and actual phase profile. A near-field map is also needed to assess a focus.
```
:::


```{figure} ../assets/chapter-03/source-array-cell.svg
:alt: Conceptual cells on their substrate; this illustration is not the simulated six-ridge device.

Conceptual cells on their substrate; this illustration is not the simulated six-ridge device.
```

