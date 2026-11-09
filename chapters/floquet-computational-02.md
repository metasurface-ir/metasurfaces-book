---
title: "Find the pattern that actually repeats"
---

(ch04-section-02)=
# Find the pattern that actually repeats

A translation by a primitive period restores the complete material distribution. Translating by one pitch in a row of different pillars generally replaces one geometry with another. Translating by the complete sequence restores it. For six distinct elements separated by $p=0.5\,\mu\mathrm m$, a possible primitive period is $\Lambda=6p=3\,\mu\mathrm m$.

The word *possible* matters: if the sequence itself has a smaller repeating subset, use that smaller period. A numerical cell may contain several primitive cells for convenience, but its extra order labels do not create new physical scattering mechanisms.

For example, place six identical elements inside a computational cell of length $6p$. The structure still has period $p$. In an expansion using $6p$, the smaller translation symmetry forces nonzero coefficients to occur only at supercell orders $m=6\ell$. Other supercell channels may lie inside the output light cone but have zero amplitude.

:::{tip} A physical demonstration
Draw six different symbols on a strip and repeat the strip. Slide a transparent copy until every symbol matches. Repeat with six identical symbols. The smallest matching translation changes, even though the spacing between adjacent symbols does not.
:::

```{figure} ../assets/chapter-04/period-and-phase.png
:alt: Repeated unequal and identical ridge motifs with element pitch and full repeat marked, together with incident-field phasors at corresponding positions.
:label: fig-ch04-period-phase

Original schematic and incident-phase calculation: $p=0.5\,\mu\mathrm m$, $\Lambda=3\,\mu\mathrm m$, $\lambda_0=1.55\,\mu\mathrm m$, $n_i=1$, and $\theta_i=12^\circ$. Unequal widths illustrate a six-element motif; they are not a solved device. Translation restores the material pattern while increasing phase lag by $k_{x,i}\Lambda$ (phasor rotation $-k_{x,i}\Lambda$). Identical elements also admit the shorter translation $p$.
```

**Predict from the drawing:** if the six elements become identical, which distance changes in the smallest material repeat, and does the incident wave's phase advance across the original $3\,\mu\mathrm m$ distance change?
