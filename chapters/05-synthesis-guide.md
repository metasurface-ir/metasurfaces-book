---
title: 'Chapter 5: Worked Examples and Learning Path'
short_title: Synthesis worked examples
---

# Chapter 5: Worked Examples and Learning Path

**Question:** which parts of a wavefront design follow from a target formula, and which require a physical scattering calculation?

Use [Chapter 5](05-metasurface-synthesis.md), the [browser lab](../labs/05-synthesis-lab.md), and the two executed notebooks: [beam steering](../notebooks/05-beam-steering.ipynb) and [wavefront models](../notebooks/05-wavefront-models.ipynb). Their execution order matters: the wavefront notebook reads the expanded library produced by the beam notebook.

## Learning path

| Stage | Prediction | Evidence |
| --- | --- | --- |
| 1 | Sign and angle of the desired diffraction order | Phase gradient and Chapter 4 light cones |
| 2 | Whether a unit-cell library covers the target phases | Circular error and transmission threshold |
| 3 | Scattering of the selected geometry sequence | Local estimate versus full-wave order powers |
| 4 | Effect of identical cells and sequence reversal | Symmetry and mirror checks |
| 5 | Width and intensity of a finite scalar focus | Aperture propagation and window/grid refinements |
| 6 | Geometric phase and polarization leakage | Defined Jones/circular basis and retardance |

For a classroom demonstration, write six target phases on a circle. First select only from Chapter 3's partial phase arc, then from the extended library. Compare the resulting geometry sequences before showing either full-wave spectrum. Ask students to predict the identical-cell and reversed-sequence controls.

## Example 1: a six-cell beam direction

For $p=0.65\,\mu\mathrm m$ and six cells, $L=3.90\,\mu\mathrm m$. At normal incidence, a positive $2\pi$ ramp targets $m=+1$. With $\lambda_0=1.55\,\mu\mathrm m$ and output index 1.5,

$$
\sin\theta_{t,+1}=\frac{1.55}{1.5(3.90)},\qquad \theta_{t,+1}\approx15.36^\circ.
$$

Air-side reflection has orders $-2$ through $+2$, while glass-side transmission has $-3$ through $+3$. Their amplitudes cannot be obtained from this angle calculation. The six-ridge RCWA result supplies those amplitudes.

## Example 2: six phase levels and their sinc factor

The staircase with $t_j=e^{2\pi i(j+1/2)/6}$ has $C_{+1}=\operatorname{sinc}(1/6)$, so $|C_{+1}|^2\approx0.9119$. This is a scalar coefficient fraction. The finite interval integration supplies the sinc; a point-source sum would omit that interval shape.

Compare this number with the actual supercell's desired-order power. They refer to different models, and equality is not an acceptance condition. The audit checks the analytical coefficient identity for 2, 3, 4, 6, 8, and 16 levels.

## Example 3: expand a library without hiding transmission constraints

The coarse height screen, using the original width domain, gives phase spans of approximately 132°, 200°, 271°, 341°, and 412° at heights 0.6, 0.9, 1.2, 1.5, and $1.8\,\mu\mathrm m$. These exploratory curves use $M=16$; the accepted $1.8\,\mu\mathrm m$ library is recalculated and checked at higher order.

```{figure} ../assets/chapter-05/coverage.png
:alt: Original and extended common-height transmission phases and powers over the same ridge-width domain.

Increasing a common height expands phase coverage but also changes transmission. Use both quantities in selecting geometries.
```

A full unwrapped cycle does not guarantee every phase at $T\geq0.8$. The six-target selection must still check each circular error. The saved expanded design has errors below $1^\circ$ at all six positions. It uses a common height, so the transmission reference plane is consistent within the sequence.

## Example 4: two denominators for a beam's performance

For the expanded supercell, $T_{+1}\approx0.85536$ and $T_{\rm total}\approx0.91139$. Thus incident-normalized target power is approximately 85.54%, while

$$
\frac{T_{+1}}{T_{\rm total}}\approx93.85\%.
$$

The second number excludes reflected incident power. Reporting it as incident efficiency would change the denominator. The local staircase predicts about 80.27% target power, and its reflected-plus-transmitted estimate is about 0.88225. That imbalance is an approximation error, not absorption in this lossless ridge model.

## Example 5: identical elements and reversal

Six identical ridges preserve the smaller primitive period $p$. In the $6p$ expansion, only orders that are multiples of six can have nonzero amplitudes. At this wavelength none of the nonzero multiples is open, so all open nonzero supercell powers vanish.

For the selected asymmetric sequence, reversing widths mirrors the structure in $x$. At normal incidence the transmitted/reflected order powers exchange $m\leftrightarrow-m$. The strong $+1$ beam becomes a strong $-1$ beam. This is a symmetry check independent of whether the design objective was well chosen.

## Example 6: a scalar line-focus metric

For $D=31.2\,\mu\mathrm m$, $f=30\,\mu\mathrm m$, and output index 1.5, the continuous focusing phase is $-k_t(\sqrt{x^2+f^2}-f)$. The saved scalar FWHM at the design plane is about $0.971\,\mu\mathrm m$ for the continuous aperture, $0.982\,\mu\mathrm m$ for the sampled phase aperture, and $0.985\,\mu\mathrm m$ for the local-library aperture.

The local-library peak squared field is about 0.550 of the continuous reference peak. It includes amplitude reduction and phase/sampling effects. The fraction of modeled line intensity in a fixed window answers another question; it must not be relabeled as a full-wave lens efficiency. The window/grid checks concern propagation of these prescribed fields.

## Example 7: a half-wave element at 30 degrees

With $t_x=1$, $t_y=-1$, and element rotation $\theta=30^\circ$, a state $\mathbf e_+=(1,i)^T/\sqrt2$ converts to $\mathbf e_-$ with phase $+60^\circ$. The opposite input basis state gives phase $-60^\circ$.

If retardance is only $90^\circ$, the ideal lossless retarder converts a fraction $\sin^2(45^\circ)=1/2$. Geometric-phase control and conversion amplitude require separate checks. These ideal Jones coefficients are not the vector response of our TE ridges.

## Report checklist

Preserve target fields, phase/reference conventions, illumination, candidate library, selection objective, geometry sequence, local predictions, all-channel full-wave powers, numerical refinements, and control cases. For focusing/polarization, name the scalar or Jones model and its metrics. Retain lower-performing or infeasible cases when they reveal a limitation.

The [lab](../labs/05-synthesis-lab.md) specifies executed stages and further finite-device, independent-method, and optimization outlines. Chapter 6 will broaden validation methods; Chapter 10 can reuse versioned simulation data for learned design.
