## 3.1 Introduction: why a unit cell?

Roll up your sleeves! If you have followed us this far, you have made it through the theoretical foundations, Maxwell's equations, and generalized boundary conditions. We have seen how a phase discontinuity lets metasurfaces steer a beam or focus waves. Now it is time to leave paper and theory and enter the practical world of simulation.

Think back to building a Lego castle. You did not mold one enormous piece of plastic! You assembled hundreds of small, standard pieces into the final shape. Metasurface design follows the same idea. Instead of solving a huge, irregular surface at once using complicated integral equations, we concentrate on designing one building block: the **unit cell**.

Physically, these cells have subwavelength dimensions, typically between $\lambda/10$ and $\lambda/3$ in the source's introductory picture. Spatial sampling suggests that if we control the phase and amplitude on these small blocks, their arrangement can implement the desired phase profile. Our mission in this chapter is to master these little building blocks.

:::{note} A useful picture, with limits
The size range is a design example, not a universal rule. A periodic-cell calculation includes identical neighbors. Assigning different cells to a finite device introduces coupling, edge effects, and sampling errors; the complete device needs an independent check.
:::

```{figure} ../assets/chapter-03/source-array-cell.svg
:alt: A finite patch array on a dielectric slab and a magnified cell with period P and patch width w.

Figure 3.1. From the complete surface to one patch on its substrate. This is an original conceptual drawing; the numerical laboratory uses the dielectric ridge shown in the computational connection below.
```

## 3.2 Choosing the meta-atom geometry: tuning resonators

The first question in a metasurface design class is: “What shape should this unit cell have?” The geometrical elements placed on the substrate are called **meta-atoms**. As a designer, you have countless choices: a square patch, a split-ring resonator (SRR), a cross, or even an H-shaped element.

Why do the shapes differ, and which should we choose? Recall the equivalent circuit in Section 2.16. A geometrical pattern on the substrate behaves approximately as an $LC$ resonator under electromagnetic illumination.

- **Capacitance $C$:** gaps between neighboring metal elements, or inside an element, store electric energy.
- **Inductance $L$:** surface-current paths along the metal store magnetic energy.

Its familiar resonance estimate is

$$
f_r=\frac{1}{2\pi\sqrt{LC}}.
$$

Changing a dimension, such as a cross-arm length, changes $L$ and $C$. The resonance moves, and the phase at our operating frequency changes. This is how geometry controls phase!

We can broadly distinguish two families, chosen according to the application:

### Resonant elements

Patches, disks, and crosses change their response when their dimensions change. This is useful for linear polarization. Sweeping a dimension, such as patch width, can sweep the transmitted or reflected phase from zero to nearly $360^\circ$.

### Geometric-phase elements

Here is an ingenious alternative. With circularly polarized illumination, we may keep the dimensions fixed and rotate an anisotropic element, such as a rectangle or ellipse, through an angle $\theta$. The converted circular-polarization channel acquires a geometric phase of $2\theta$ or $-2\theta$. The source describes the constant amplitude under rotation as an important advantage.

$$
\Delta\Phi=\pm2\theta.
$$

:::{note} What that promise assumes
A single resonance does not guarantee useful full-circle phase coverage at high amplitude. The $LC$ model is an approximation. For geometric phase, the conversion amplitude is rotation-independent only under the appropriate symmetry, illumination, and approximately half-wave response; conversion efficiency can be low. The sign depends on the chosen circular-polarization basis and whether phase means a signed argument or a lag.
:::

```{figure} ../assets/chapter-03/source-geometries.svg
:alt: Patch, disk, cross, split ring and dipole resting on dielectric slabs, with gap and current-path annotations.

Figure 3.2a. Five possible meta-atoms. Gap and current-path annotations identify conceptual capacitive and inductive regions, not extracted circuit values.
```

```{figure} ../assets/chapter-03/source-pb.svg
:alt: Identical rectangular elements on a substrate rotated through zero, forty-five and ninety degrees.

Figure 3.2b. Fixed dimensions, different rotation angles. The geometric-phase relation applies to the converted circular-polarization channel.
```

## 3.3 Reading the scattering parameters

The simulation is finished, and the software gives us a collection of plots. What do we want from a meta-atom? Two things: **amplitude and phase**. They are encoded in the scattering matrix, or S-parameters.

For a transmissive surface we focus on $S_{21}$; for a reflective surface, on $S_{11}$. At the operating frequency, say $10\,\mathrm{GHz}$, inspect two features:

1. **Amplitude.** We want low loss. Dirty glass that passes little light is not useful for a lens! The transmitted or reflected amplitude should be as close as possible to one, or zero decibels. The source uses amplitudes above $0.8$, roughly $-1$ to $-2\,\mathrm{dB}$, as an illustrative acceptable range.
2. **Phase.** This is the wave's steering command. We plot the S-parameter phase against frequency, then read its value at the operating frequency. That phase reshapes the wavefront.

But wait! A single element with a fixed phase of $45^\circ$ is not enough. To construct converging, diverging, or tilted wavefronts, we need a family spanning every angle from zero to $360^\circ$, equivalently $-\pi$ to $+\pi$. How do we obtain that family? The next step provides the answer.

:::{note} Amplitude is not automatically power
For power-normalized ports, $P=|S|^2$ and $20\log_{10}|S|$ is the amplitude in decibels. Thus $0.8$ means $0.64$ power and approximately $-1.94\,\mathrm{dB}$. Raw electric-field coefficients need an impedance/admittance factor. A weak selected channel can also indicate power in reflection, other diffraction orders, or polarization conversion rather than absorption.
:::

## 3.4 Parametric sweeps: building a design dictionary

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

## 3.5 Array design: from building blocks to a surface

Now we reach the exciting part! So far we have studied one cell inside a “room of mirrors,” the periodic boundary conditions. A real metasurface contains hundreds or thousands of meta-atoms arranged side by side.

Array design is like writing a sentence using the words in our dictionary. At every position $(x,y)$, we choose the meta-atom that produces the desired outgoing wave. We first calculate the required phase profile. Let us build two familiar applications.

### Beam steering

Suppose a normally incident wave must leave at $\theta=30^\circ$. The generalized Snell law tells us that a constant phase gradient is needed. The source gives

$$
\phi(x)=\frac{2\pi}{\lambda_0}x\sin\theta.
$$

Here $\lambda_0$ is the free-space wavelength, $x$ is the horizontal meta-atom position, and $\theta$ is the desired deflection angle.

Divide the surface into squares the size of one cell. Insert each square's center coordinate into the formula, then find the corresponding geometry in the LUT. For example, if the requested phase at $x=15\,\mathrm{mm}$ is $120^\circ$ and the LUT maps it to $r=2.5\,\mathrm{mm}$, place that meta-atom there. Continue, step by step, until the entire surface is filled!

:::{important} One time convention, two meanings of phase
Throughout the course the real field uses $e^{+i\omega t}$ and forward propagation uses $e^{-i\mathbf k\cdot\mathbf r}$. For steering toward positive $x$, the positive source profile above is a **phase lag**: $t(x)=A(x)e^{-i\phi(x)}$. Its signed argument is $-\phi(x)$. In the focusing formula below, the positive source profile is instead the **signed argument** of transmission. The source uses the same symbol for both; keeping the equations and distinguishing their meanings avoids reversing the beam or defocusing the lens. These expressions assume normal incidence and propagation into free space.
:::

:::{admonition} Worked exercise: a steering array
:class: tip
A normally illuminated surface steers toward $30^\circ$, with $\lambda_0=30\,\mathrm{mm}$ and cell pitch $p=5\,\mathrm{mm}$. Find the adjacent-cell phase increment, the phases at $x=0,5,10,15\,\mathrm{mm}$, and the position of the $r=2.5\,\mathrm{mm}$ meta-atom if its LUT phase is $90^\circ$.

```{dropdown} Show the worked answer
The phase increment is

$$
\Delta\phi=\frac{2\pi}{\lambda_0}p\sin\theta
=\frac{2\pi}{30}(5)\sin30^\circ
=\frac{2\pi}{30}\times5\times0.5
=\frac{\pi}{6}=30^\circ.
$$

Each cell therefore needs $30^\circ$ more lag than the previous one. Substitution at the four positions gives

$$
\phi(0)=0^\circ,\quad\phi(5)=30^\circ,\quad
\phi(10)=60^\circ,\quad\phi(15)=90^\circ.
$$

The requested $90^\circ$ occurs at $x=15\,\mathrm{mm}$. Place the $r=2.5\,\mathrm{mm}$ meta-atom at that position. The final sequence is $0^\circ,30^\circ,60^\circ,90^\circ$, with $\Delta\phi=30^\circ$. Its signed transmission arguments are the negatives of these lags.
```
:::

### A flat lens: bringing energy to one point

Let us do something even more interesting: focus a plane wave at a focal point a distance $F$ away. A conventional glass lens is thicker in the middle and thinner at the edges. A metalens has a flat thickness and does the work by controlling phase!

Waves leaving the edges travel farther than those leaving the center. Their surface phase must compensate for that path difference. The source describes this as a smaller phase at the edges; the convention note above explains why signed arguments and lags must be distinguished. The hyperbolic phase profile is

$$
\phi(x,y)=\frac{2\pi}{\lambda_0}\left(\sqrt{x^2+y^2+F^2}-F\right).
$$

Insert each coordinate, obtain the needed phase, select the geometry from the dictionary, and place the corresponding meta-atom. The layout resembles concentric rings, with dimensions changing more rapidly toward the edges.

:::{admonition} Worked exercise: a metalens
:class: tip
A metalens focuses a plane wave at $F=40\,\mathrm{mm}$, with $\lambda_0=20\,\mathrm{mm}$. Calculate the phase at $(0,0)$, $(30,0)$ and $(0,30)\,\mathrm{mm}$. Where should an element of radius $r=2.5\,\mathrm{mm}$ be placed if its LUT phase is $180^\circ$?

```{dropdown} Show the worked answer
At the center, $x=y=0$, so

$$
\phi(0,0)=\frac{2\pi}{20}\left(\sqrt{0^2+0^2+40^2}-40\right)
=\frac{2\pi}{20}(40-40)=0\,\mathrm{rad}=0^\circ.
$$

At $(30,0)$, first calculate the path and its excess over the central path:

$$
\sqrt{30^2+40^2}=\sqrt{900+1600}=\sqrt{2500}=50\,\mathrm{mm},
\qquad\Delta l=50-40=10\,\mathrm{mm}.
$$

Therefore

$$
\phi(30,0)=\frac{2\pi}{20}\left(\sqrt{30^2+0^2+40^2}-40\right)
=\frac{2\pi}{20}(10)=\pi\,\mathrm{rad}=180^\circ.
$$

At $(0,30)$, the same calculation gives

$$
\phi(0,30)=\frac{2\pi}{20}\left(\sqrt{0^2+30^2+40^2}-40\right)
=\frac{2\pi}{20}(50-40)=\pi\,\mathrm{rad}=180^\circ.
$$

The two off-axis points have the same radial distance:

$$
\sqrt{x^2+y^2}=30\,\mathrm{mm}.
$$

The $r=2.5\,\mathrm{mm}$ element can therefore be placed at both $(30,0)$ and $(0,30)\,\mathrm{mm}$, and anywhere on the ring

$$
x^2+y^2=(30\,\mathrm{mm})^2.
$$

The final phases are $0^\circ,180^\circ,180^\circ$. Equal phase at equal radius creates the concentric-ring layout. Further rings can repeat the same wrapped phase; the stated ring is not necessarily the only one on a larger aperture.
```
:::

```{figure} ../assets/chapter-03/source-profiles.svg
:alt: Wrapped linear steering lag, radial focusing phase, and variable patch dimensions on a substrate.

Figures 3.5–3.6. Original conceptual phase profiles and placement schematic. Colors encode phase; patch sizes illustrate LUT assignment and are not a validated geometry-to-phase mapping.
```

## 3.6 Simulating the complete array

Once the placement map is ready, usually generated by a short MATLAB or Python script linked to CST or HFSS, it is time for the final test. The simulation setup changes substantially:

1. **Boundary conditions:** the periodic room of mirrors is gone. The array is finite. Surround it with an open domain and absorbing layers, such as PML, so outgoing waves do not return.
2. **Excitation:** instead of Floquet ports, a plane wave or a realistic antenna, such as a horn, illuminates the surface.
3. **Results:** inspect the electric-field distribution in space. Seeing a wave bend or converge to a focus in a two-dimensional near-field plot is one of the pleasures of metasurface design!

```{figure} ../assets/chapter-05/focus.png
:alt: Retained scalar wavefront calculation showing propagation and focusing.

Figure 3.7. The existing course's scalar focusing calculation provides a visual bridge to full-array analysis. It is not a CST/HFSS screenshot or a full-wave finite-array validation. The synthesis chapter and numerical laboratory explain the model's assumptions.
```

The source requests three array illustrations: linear wrapped steering phase and lens phase (Figure 3.5), a placement map with varying element dimensions (Figure 3.6), and field maps showing steering and focusing (Figure 3.7). The original drawings and retained calculated figure above implement these visual connections without inventing commercial-solver results. Compare [beam synthesis](05-metasurface-synthesis.md) and [independent-cell versus supercell predictions](../labs/10-coupling-lab.md) before claiming device performance.
