---
title: "3.3 Reading the scattering parameters"
---

# 3.3 Reading the scattering parameters

The simulation is finished, and the software gives us a collection of plots. What do we want from a meta-atom? Two things: **amplitude and phase**. They are encoded in the scattering matrix, or S-parameters.

For a transmissive surface we focus on $S_{21}$; for a reflective surface, on $S_{11}$. At the operating frequency, say $10\,\mathrm{GHz}$, inspect two features:

1. **Amplitude.** We want low loss. Dirty glass that passes little light is not useful for a lens! The transmitted or reflected amplitude should be as close as possible to one, or zero decibels. The source uses amplitudes above $0.8$, roughly $-1$ to $-2\,\mathrm{dB}$, as an illustrative acceptable range.
2. **Phase.** This is the wave's steering command. We plot the S-parameter phase against frequency, then read its value at the operating frequency. That phase reshapes the wavefront.

But wait! A single element with a fixed phase of $45^\circ$ is not enough. To construct converging, diverging, or tilted wavefronts, we need a family spanning every angle from zero to $360^\circ$, equivalently $-\pi$ to $+\pi$. How do we obtain that family? The next step provides the answer.

:::{note} Amplitude is not automatically power
For power-normalized ports, $P=|S|^2$ and $20\log_{10}|S|$ is the amplitude in decibels. Thus $0.8$ means $0.64$ power and approximately $-1.94\,\mathrm{dB}$. Raw electric-field coefficients need an impedance/admittance factor. A weak selected channel can also indicate power in reflection, other diffraction orders, or polarization conversion rather than absorption.
:::
