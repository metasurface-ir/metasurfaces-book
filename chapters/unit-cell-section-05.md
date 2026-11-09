---
title: "3.5 Array design: from building blocks to a surface"
---

# 3.5 Array design: from building blocks to a surface

Now we reach the exciting part! So far we have studied one cell inside a “room of mirrors,” the periodic boundary conditions. A real metasurface contains hundreds or thousands of meta-atoms arranged side by side.

Array design is like writing a sentence using the words in our dictionary. At every position $(x,y)$, we choose the meta-atom that produces the desired outgoing wave. We first calculate the required phase profile. Let us build two familiar applications.

### Beam steering

Suppose a normally incident wave must leave at $\theta=30^\circ$. The generalized Snell law tells us that a constant phase gradient is needed. The source gives

$$
\phi(x)=\frac{2\pi}{\lambda_0}x\sin\theta.
$$

Here $\lambda_0$ is the free-space wavelength, $x$ is the horizontal meta-atom position, and $\theta$ is the desired deflection angle.

Divide the surface into squares the size of one cell. Insert each square's center coordinate into the formula, then find the corresponding geometry in the LUT. For example, if the requested phase at $x=15\,\mathrm{mm}$ is $120^\circ$ and the LUT maps it to $r=2.5\,\mathrm{mm}$, place that meta-atom there. Continue, step by step, until the entire surface is filled!

:::{important} Signed phase and phase lag
For steering toward positive $x$, the positive source profile above is a **phase lag**: $t(x)=A(x)e^{-i\phi(x)}$. Its signed argument is $-\phi(x)$. In the focusing formula below, the positive source profile is instead the **signed argument** of transmission. The source uses the same symbol for both; keeping the equations and distinguishing their meanings avoids reversing the beam or defocusing the lens. These expressions assume normal incidence and propagation into free space.
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
