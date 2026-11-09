---
title: "1.8 Inside a unit cell: electric and magnetic responses"
short_title: "1.8 Inside a unit cell: electric and magnetic responses"
---

# 1.8 Inside a unit cell: electric and magnetic responses

Now let's use an imaginary microscope to look inside one of these tiny metal cells. What exactly happens when an electromagnetic wave, consisting of electric and magnetic fields, hits it?

### 1. Electric response

The wave's electric field pushes the free charges—electrons—inside the cell's metal and gathers them at its two ends. This charge accumulation creates an electric dipole that acts like a tiny antenna and radiates a new wave.

### 2. Magnetic response: the magic of artificial magnetism!

Here engineering really shines. In nature, materials with a strong magnetic response at high frequencies, such as microwave or optical frequencies, are scarce. Engineers found a trick: shape the unit cell as a ring with a small gap, and the wave's field makes a circulating current flow around it. That rotating current produces a magnetic field. We have created **artificial magnetism** without using any magnetic material!

### 3. Huygens metasurfaces: the complete development

What happens if we design a cell to produce electric and magnetic responses of equal strength at the same time? In this remarkable situation, the surface impedance becomes exactly equal to the impedance of air—free space.

What is the result? The wave reaches the surface and does not even notice a change of environment, so no wave is reflected! One hundred percent of its energy passes through, while its phase changes along the way. These magical surfaces, named in honor of Huygens' principle, are the best candidates for making exceptionally efficient metalenses—transmissive flat lenses.

### 4. Complex coupling: bianisotropy

Sometimes the geometry is so special, as in three-dimensional or chiral structures, that an electric field alone can induce a magnetic response in the cell, or vice versa! This phenomenon, called bianisotropy, gives designers access to more advanced forms of control.

:::{note} The assumptions behind the Huygens picture
Balance includes phase, normalization, illumination and the surrounding media; electric and magnetic quantities with different units cannot simply be set numerically equal. Unit transmission also requires no loss or other outgoing channels. A substrate, higher multipoles, and coupling can modify reflection cancellation. Dielectric displacement-current patterns can produce magnetic-dipole-like responses without a magnetic constituent. Bianisotropy is magnetoelectric cross-coupling, not just directional anisotropy; our scalar symmetric sheet does not model its general form.
:::

### Computational connection: mechanisms and interference

An incident field drives charge, current, and polarization in a structure. An electric-dipole-like response is associated with oscillating electric charge separation. A magnetic-dipole-like response can arise from circulating currents or displacement-current patterns; it does not require a naturally magnetic material at the operating frequency.

The resulting fields interfere with one another and with the incident wave. Suitable electric and magnetic contributions can cancel in one direction and reinforce in another. The [dielectric Huygens-surface work of Decker and colleagues](https://openresearch-repository.anu.edu.au/items/46257eed-cdcb-4814-93fb-868f9c087777) develops this physical idea for specific dielectric structures. Reproducing a paper's device performance requires its geometry, materials, illumination, and numerical or experimental evidence.

Several design mechanisms are useful:

| Mechanism | Main control | Tradeoff or condition |
| --- | --- | --- |
| Resonant response | Geometry/material-dependent resonance | Phase and amplitude vary with frequency and loss |
| Propagation phase | Optical path or guided propagation through an element | Height, index, modal coupling, and dispersion matter |
| Geometric phase | Orientation of an anisotropic response | Depends on polarization channel and conversion amplitude |
| Collective/nonlocal response | Interaction across several elements | A local independent-cell description may fail |

These mechanisms can coexist. A response library from repeated identical cells includes that repeated environment. Assembling different cells changes the environment and requires an additional test. [Chapter 3](03-unit-cell-design.md) builds a library, while [Chapter 5](05-metasurface-synthesis.md) compares its local prediction with the complete repeated structure.


### Our existing analytical sheet model


To separate response reasoning from geometry and solver setup, define a two-port sheet. Port 1 and port 2 represent the specular waves on opposite sides, in equal-impedance media. For a reciprocal, mirror-symmetric response,

$$
\begin{bmatrix}b_1\\b_2\end{bmatrix}
=S\begin{bmatrix}a_1\\a_2\end{bmatrix},\qquad
S=\begin{bmatrix}r&t\\t&r\end{bmatrix}.
$$

The incident amplitudes are $a_1,a_2$ and the outgoing amplitudes $b_1,b_2$, all referenced to the ideal sheet. One-sided incidence sets $a_1=1,a_2=0$. Losslessness for arbitrary incoming fields requires $S^\dagger S=I$, which is stronger than checking only $|r|^2+|t|^2=1$.

Use two unit-magnitude channel functions, $C_e$ and $C_m$:

$$
r=\frac{C_e-C_m}{2},\qquad t=\frac{C_e+C_m}{2}.
$$

The even/odd eigenvalues of $S$ are $C_e$ and $-C_m$. The transparent limit $C_e=C_m=1$ gives $r=0,t=1$. The labels *electric-like* and *magnetic-like* are effective channel coordinates in this teaching model; their numerical values are not retrieved electric or magnetic dipole moments.

For each channel, choose the dimensionless ratio $u=f/f_0$ and strength $a\geq0$:

$$
d=1-u^2,\qquad C(f)=\frac{d+i a u}{d-i a u}.
$$

For $a>0$, the rational expression remains finite at resonance. When $a=0$, define $C=1$ explicitly, including at $f=f_0$. With real frequency and these parameters, $|C|=1$, so the complete scattering matrix is unitary. The notebook verifies this algebra numerically and checks an independent electric-only shunt expression.

This model is deliberately restricted. It has no assigned width, height, material dataset, diffraction, polarization conversion, or absorption. Its value is to make interference and physical consistency inspectable before adding geometry.


### Predict the four limits, then try them


| Case | Parameters / condition | Prediction |
| --- | --- | --- |
| Transparent | Both strengths zero | $r=0$, $t=1$ |
| Electric-like only | Magnetic-like strength zero | Strong reflection at its resonance; transmitted phase undefined when $t=0$ |
| Balanced pair | Identical two channel functions | $r=0$, $t=C_e$, with unit transmitted power and varying phase |
| Detuned pair | Different resonance frequencies | Cancellation generally breaks; reflection and transmission redistribute power |

At the reference $f=200\,\mathrm{THz}$, the free-space wavelength is about $1.499\,\mu\mathrm m$. The electric-only preset has $r=-1,t=0$. The balanced preset has $r=0,t=-1$: zero reflected power and a transmission phase of $180^\circ$ relative to the transparent reference.

```{figure} ../assets/chapter-01/response.png
:alt: Analytical reflected and transmitted powers and meaningful transmission phases for four sheet-response presets.

Power and phase describe complementary parts of the response. The electric-only transmission phase is masked at its exact zero. Perfect balanced matching is imposed by this ideal model.
```

```{figure} ../assets/chapter-01/phasors.png
:alt: Head-to-tail complex channel vectors cancel in reflection and add in transmission for the ideal balanced sheet.

Original complex-plane illustration of the model's channel contributions. These arrows are not separately retrieved dipole radiation fields.
```

Matching the channels over an entire frequency interval is an imposed idealization. Unit transmission in this model does not establish a practical, lossless, broadband Huygens surface or a geometry providing every desired phase.


Try the [browser lab](../labs/01-first-investigation.md) and [executed notebook](../notebooks/01-first-metasurface-model.ipynb). The abstract channel strengths have no assigned fabrication dimensions.

