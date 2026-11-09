---
title: "3.4 Parametric sweeps: building a design dictionary"
---

# 3.4 Parametric sweeps: building a design dictionary

Suppose you want to translate an English text into Persian. What do you need? A dictionary! Metasurface design works the same way. Later, when we design a flat lens, the equations may say: “At $x=2$, $y=3$, I need a meta-atom that gives the wave a phase of $120^\circ$.” You must quickly find the appropriate geometry in your design dictionary.

We build it using a **parametric sweep**. Select one geometric parameter: a metal disk radius $r$, a cross-arm width $w$, or a rotation angle $\theta$. Then tell the software: “Vary $r$ from $1$ to $5\,\mathrm{mm}$ in $0.1\,\mathrm{mm}$ increments. Rerun the simulation at each value and record the amplitude and phase at the operating frequency.”

Plot the results against the swept dimension, with phase and amplitude on the vertical axes. A good dictionary has:

- **Complete phase coverage:** the phase curve spans $360^\circ$, leaving no blind region.
- **High, uniform amplitude:** amplitude stays high and as flat as possible. A geometry with the right phase but a sharp amplitude dip reduces the final device efficiency.

The reference table connecting physical dimensions to electromagnetic phase is called a **look-up table (LUT)**. With this dictionary, we have a powerful tool for designing the surface.

```{figure} ../assets/chapter-03/library.png
:alt: Computed complex transmission, power and phase as dielectric ridge width changes.

Figure 3.4. An actual exported response library from the retained ridge calculation. Unlike the source's ideal suggested sketch, useful phase coverage and amplitude must be measured from the data; they are not guaranteed to be perfect. The worked computational pages identify its normalization and reference planes.
```
