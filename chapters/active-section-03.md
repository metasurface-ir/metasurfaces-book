# 7.3 Digital, programmable, and coding metasurfaces

Instructor booklet, pages 181–185.

Before 2014, the prevailing approach described metasurfaces in terms of continuous material parameters such as permittivity $\epsilon$ and permeability $\mu$, or a continuous surface impedance $Z_s$. Although analytically precise, this classical approach did not connect directly to digital processing and computer science.

In a pioneering 2014 article, Tie Jun Cui and colleagues introduced coding, digital, and programmable metasurfaces. This approach linked electromagnetic physics with information theory and digital logic. [Cui and colleagues' article](https://doi.org/10.1038/lsa.2014.99)

## 7.3.1 Digital unit cells: one-bit, two-bit, and multibit

The central idea is to map continuous reflection or transmission phases onto discrete states represented as binary digits.

1. **One-bit coding.** The simplest case uses two distinct states with a $180^\circ$ or $\pi$ radian phase difference. Element ‘0’ has $\phi_0=0^\circ$, or a reference phase $\phi_{\rm ref}$, and $|R_0|\approx1$. Element ‘1’ has $\phi_1=180^\circ$, or $\Delta\phi=\pi$ from the reference, and equal magnitude $|R_1|\approx1$. In practice a designed unit cell can obtain this phase difference by switching a PIN diode or changing the reflecting patch dimensions.
2. **Two-bit coding.** To control the wavefront more precisely and avoid unwanted radiation symmetry, the resolution rises to four states with $90^\circ$ or $\pi/2$ steps. Codes ‘00’, ‘01’, ‘10’, and ‘11’ represent $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$.
3. **Multibit coding.** An $N$-bit metasurface divides phase into $2^N$ discrete, equally spaced states:

$$
\phi_m=m\frac{2\pi}{2^N},\qquad m\in\{0,1,\ldots,2^N-1\}.
$$

More bits reduce phase quantization error and can increase main-beam gain, at the cost of a more complex bias network.

## 7.3.2 The coding matrix and array theory for predicting scattering

Consider a two-dimensional array of subwavelength $D_x\times D_y$ unit cells in $M$ rows and $N$ columns. The digital coding matrix represents the state of the entire sheet:

$$
\Gamma=
\begin{bmatrix}
\gamma_{11}&\gamma_{12}&\cdots&\gamma_{1N}\\
\gamma_{21}&\gamma_{22}&\cdots&\gamma_{2N}\\
\vdots&\vdots&\ddots&\vdots\\
\gamma_{M1}&\gamma_{M2}&\cdots&\gamma_{MN}
\end{bmatrix},\qquad\gamma_{mn}\in\{0,1\}.
$$

Each cell's complex reflection coefficient is $R_{mn}=A_{mn}e^{i\phi_{mn}}$. When a normally incident plane wave illuminates the surface, the scattered far field follows from the array factor:

$$
f(\theta,\varphi)=f_e(\theta,\varphi)
\sum_{m=1}^{M}\sum_{n=1}^{N} A_{mn}
e^{i[\phi_{mn}+k_0 x_n\sin\theta\cos\varphi+k_0 y_m\sin\theta\sin\varphi]},
$$

$$
x_n=D_x(n-\tfrac12),\qquad y_m=D_y(m-\tfrac12),\qquad k_0=2\pi/\lambda_0.
$$

Here $f_e$ is the single-element radiation pattern. The indices follow the exercise's convention, with columns along $x$ and rows along $y$. Shifting the origin only changes the overall phase.

## 7.3.3 Wave behaviors for elementary coding sequences

Changing the sequence of codes on the surface can produce different electromagnetic behaviors.

1. **Periodic alternating sequence: deflection and beam splitting.** A symmetric one-bit sequence $\Gamma=[000\ldots111\ldots]$ with $L$ zeros followed by $L$ ones has spatial period $\Lambda=2LD_x$. With ideal balanced opposite coefficients the mean is zero. The Fourier expansion contains spatial harmonics $\pm2\pi/\Lambda$. For propagating first orders, the two symmetric directions satisfy

$$
\sin\theta=\pm\frac{\lambda_0}{\Lambda}=\pm\frac{\lambda_0}{2LD_x}.
$$

2. **Two-bit phase gradient: dominant single-beam steering.** With the unidirectional phase sequence ‘00, 01, 10, 11, …’, the phase pattern breaks reflection symmetry and forms the gradient $d\phi/dx=(\pi/2)/D_x$. For this gradient, the far-field sign used above gives the dominant order at

$$
\sin\theta=-\frac{\lambda_0}{4D_x}.
$$

3. **Pseudo-random sequence: radar cross-section reduction.** With an irregular arrangement of binary codes, reflected waves have irregular phases and can interfere destructively. Concentrated specular energy can spread over the hemisphere as diffuse scattering. The booklet gives $10$ to $20\,\mathrm{dB}$ as illustrative reductions. The actual reduction depends on the code, angle, band, and structure response.

:::{note} Steering-sign correction and the diffraction condition
The printed sign in the second item is positive, but the chapter's array factor and worked solution give a negative angle for a positive gradient. A dominant order does not carry all the incident power.
:::

## 7.3.4 Hardware control architecture and real-time FPGA implementation

To put these ideas into a real system with online control, use the following architecture:

1. **Decision and processing layer.** Tracking or optimization algorithms, such as a genetic algorithm or AI, compute the coding matrix.
2. **High-speed FPGA or SoC distribution layer.** The chip's parallel organization allows new code frames to be loaded at high rates.
3. **Shift registers and drivers.** Deliver control voltages to the diode cathodes and anodes at the back of the surface.

## Problem statement

::::{admonition} Try it first
:class: book-exercise

A programmable reflecting metasurface contains $8\times8$ cells. Centre-to-centre spacing in both $x$ and $y$ is $D=10\,\mathrm{mm}$. A normally incident plane wave illuminates it at $f_0=10\,\mathrm{GHz}$. Columns run along $x$ and rows along $y$. The angle $\theta$ is measured from the normal in the $xz$ plane, positive toward $+x$.

All ideal states have unit reflection magnitude. One-bit codes 0 and 1 have phases $0^\circ$ and $180^\circ$. In the two-bit case, 00, 01, 10, and 11 have phases $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$.

| Pattern | Coding |
| --- | --- |
| A: periodic one-bit | Every row has the column sequence 0,0,1,1,0,0,1,1. |
| B: two-bit gradient | Every row has 00,01,10,11,00,01,10,11. |
| C: pseudo-random one-bit | Scatter 32 zeros and 32 ones over the sheet without repeating a specified periodic block. |

Suppose each cell has two control inputs. An FPGA sends a full frame over a single serial line at a $20\,\mathrm{MHz}$ clock. Simultaneous latching and driver settling take $1\,\mathrm{\mu s}$ after transmission.

1. If a cell's ideal phase is $130^\circ$, which states are selected by one-, two-, and three-bit coding?
2. Use the array factor to find the main beam angles for A and the dominant beam for B. How can B's direction be reversed?
3. In C, what is the reflected field exactly at broadside? Does reduced reflection in that direction mean energy was absorbed?
4. How long does it take to send and apply one frame? What do the processor, FPGA, shift register, and driver do?

```{dropdown} Show the full worked answer

### 1. From continuous phase to a digital code

A $b$-bit metasurface has $2^b$ states. For uniform states the phase step is $360^\circ/2^b$. Select the nearest state on the phase circle.

| Bits | Phase step | Nearest phase to $130^\circ$ | Phase error magnitude |
| --- | --- | --- | --- |
| One | $180^\circ$ | $180^\circ$ | $50^\circ$ |
| Two | $90^\circ$ | $90^\circ$ | $40^\circ$ |
| Three | $45^\circ$ | $135^\circ$ | $5^\circ$ |

Nearest-state rounding has a maximum error of half the phase step. More bits permit a more accurate wavefront, but the cell must realize more states with acceptable phase and amplitude. **The bit count determines the number of phase states. Their arrangement determines the beam pattern.**

### 2. Patterns A and B: why two beams in one case and one dominant beam in the other?

First compute

$$
\lambda_0=\frac{c}{f_0}=30\,\mathrm{mm},\qquad D=\lambda_0/3.
$$

In the $xz$ cut, the geometrical phase difference between adjacent columns is $\psi=k_0D\sin\theta$. The eight rows are identical for A and B, so their array factor reduces to a column sum:

$$
AF(\theta)=8\sum_{q=0}^{7}R_qe^{iq\psi},\qquad \psi=k_0D\sin\theta.
$$

The factor eight comes from the coherent sum of the eight rows. The actual far-field pattern is the array factor times the element pattern. The calculation below is for the ideal array factor.

**Pattern A: periodic one-bit code.** The column reflection coefficients are

$$
R_q=[+1,+1,-1,-1,+1,+1,-1,-1].
$$

The period is four cells, so $\Lambda=4D=40\,\mathrm{mm}$. For the first diffraction orders,

$$
\sin\theta_\pm=\pm\frac{\lambda_0}{\Lambda}=\pm\frac{30}{40}=\pm0.75,
\qquad \theta_\pm\simeq\pm48.6^\circ.
$$

The real coefficients give $AF(-\theta)=AF^*(\theta)$, producing equal magnitudes in symmetric directions. At broadside $\psi=0$ and the sum vanishes. Thus the ideal zero order or specular reflection is suppressed and two symmetric main beams appear.

:::{note} Order angle and finite-array peak
The $48.6^\circ$ value follows from the spatial period. To find the exact peak for eight columns, maximize $|AF|$ itself. Direct maximization of the given eight-column sum gives peaks near $\pm45.0^\circ$. The shift comes from the finite-aperture envelope.
:::

**Pattern B: two-bit phase gradient.** Now

$$
R_q=[1,i,-1,-i,1,i,-1,-i]=e^{iq\pi/2},
\qquad AF(\theta)=8\sum_{q=0}^{7}e^{iq(\pi/2+\psi)}.
$$

The dominant beam requires $\pi/2+k_0D\sin\theta=2\pi\ell$, with $\ell\in\mathbb Z$. For $\ell=0$,

$$
\sin\theta=\frac{-\pi/2}{k_0D}=-\frac{\lambda_0}{4D}=-0.75
\quad\Rightarrow\quad \theta\simeq-48.6^\circ.
$$

Other $\ell$ values give $|\sin\theta|>1$ and are not propagating. A positive $90^\circ$ phase step per column produces a negative beam angle. Reverse the gradient to $-90^\circ$ by repeating 00,11,10,01 to move the dominant beam to $+48.6^\circ$.

**Numerical check.** In the desired direction all 64 contributions add coherently and $|AF|=64$. At the mirror angle $+48.6^\circ$, the terms alternate in sign and $AF=0$. That ideal null at one angle does not eliminate sidelobes or real device losses.

### 3. Pattern C: eliminating broadside reflection versus absorbing energy

At broadside there is no position-dependent phase. The ideal sum is independent of where the signs are placed:

$$
AF(0)=32(+1)+32(-1)=0.
$$

Both A and C have a broadside null, but their scattering differs.

- A's periodic arrangement has distinct spatial harmonics and concentrates most scattering into two directions.
- A suitable aperiodic arrangement in C can spread scattering among more directions. Knowing only the counts of zeros and ones cannot determine peak directions or levels. Insert the **full code matrix** into the array factor.

The null comes from **destructive interference**. Amplitude errors or a departure from $180^\circ$ phase separation can turn it into a nonzero minimum. This calculation cannot specify a fixed reduction in measured reflection in decibels.

### 4. Implementation: from the code matrix to cell voltages

Each frame has two bits for each of 64 cells:

$$
N_{\rm bits}=64\times2=128\,\mathrm{bit}.
$$

The fixed interface still uses 128 bits for a one-bit pattern. Send phases $0^\circ$ and $180^\circ$ as 00 and 10. Sending one bit per cycle gives

$$
t_{\rm send}=\frac{128}{20\times10^6}=6.4\,\mathrm{\mu s},\qquad
t_{\rm update}=6.4+1.0=7.4\,\mathrm{\mu s}.
$$

| Hardware | Task |
| --- | --- |
| Processor or controller | Selects or computes the coding matrix for the requested function. |
| FPGA | Sends the bits in order and commands a simultaneous latch after the frame. |
| Shift register with output register | Stores the new frame while the outputs retain the previous pattern, then updates the outputs together. |
| Drivers | Convert logic codes to appropriate bias voltages or currents. |

Simultaneous latching matters. Updating each output as its bit arrives would expose incomplete patterns and temporarily steer the beam as the frame loads. The $7.4\,\mathrm{\mu s}$ runs from the start of an already prepared frame to settled driver outputs. It excludes computation of the matrix and any extra cell delay.

**Summary.** All three patterns used the same sheet. The periodic binary sequence created two symmetric beams. The two-bit gradient sent a dominant beam to one side. The balanced irregular code canceled broadside reflection through interference. The design chain goes from wave objective to code matrix, cell reflection coefficients, and far-field pattern.
```
::::

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
