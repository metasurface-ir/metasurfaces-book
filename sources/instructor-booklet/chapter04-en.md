## Introduction: a world of repeating patterns

Welcome to Chapter 4! We have learned how to design our Lego bricks, the meta-atoms, and give them shape in software. A real metasurface, however, contains tens, hundreds, or even millions of them. Does an incident wave see every cell separately? It experiences their collective response. We will look at a repeating structure from the wave's point of view. Floquet's theorem provides a common language for periodic structures and explains how unwanted grating lobes can carry energy away from the desired beam.



## Periodic structures and the unit cell

A unit cell repeated along one in-plane direction forms a one-dimensional periodic structure; repetition along two directions forms a two-dimensional periodic structure. Periods $p_x$ and $p_y$ define a two-dimensional lattice. The unit cell is the basic building block. For an infinitely periodic structure, mathematics lets us infer the fields throughout an entire city from one house: we do not need to simulate the whole array. This is where Floquet enters the story.



## Floquet theorem: the language of periodicity

In a single Bloch excitation sector, neighboring cells have the same field pattern multiplied by a fixed phase factor. Imagine a street lined with identical, equally spaced trees: the scene repeats as you move from tree to tree. For a period $p$, the field at $x+p$ follows the relation below. Here $k_x$ is the tangential wavevector and the exponential is the adjacent-cell phase factor. In two dimensions we may translate along either lattice direction or both. In plain language: repeat the field pattern, but shift its phase! These expressions use $j=i$ and positive harmonic time dependence $e^{+i\omega t}$.


$$
E(x+p)=E(x)e^{-ik_xp}.
$$
$$
E(x+p_x,y+p_y)=E(x,y)e^{-i(k_xp_x+k_yp_y)}.
$$
$$
E(x+p_x,y)=E(x,y)e^{-ik_xp_x},\qquad
E(x,y+p_y)=E(x,y)e^{-ik_yp_y}.
$$


## Tangential wavevector and incidence angle

Picture a plane wave incident at angle $\theta$ from the normal onto the $xy$ plane, with propagation in the $xz$ plane. Its tangential component and adjacent-cell phase lag are given below. Oblique illumination excites neighboring cells with different phases. At $10\,\mathrm{GHz}$, using the source approximation $c=3\times10^8\,\mathrm{m/s}$, the wavelength is $30\,\mathrm{mm}$. For $p=10\,\mathrm{mm}$ and $\theta=30^\circ$, the lag is $60^\circ$. At normal incidence it vanishes. The signed phase change of the field under translation is the negative of this lag. In an incident medium of index $n_i$, replace $k_0$ by $n_i k_0$.


$$
k_0=\frac{2\pi}{\lambda_0},\qquad k_x=k_0\sin\theta,
\qquad\Delta\phi=k_xp=k_0p\sin\theta.
$$
$$
\Delta\phi=\frac{2\pi}{30}(10)\sin30^\circ
=\frac{2\pi}{30}(10)(0.5)=\frac{\pi}{3}=60^\circ.
$$
$$
\theta=0\quad\Longrightarrow\quad\Delta\phi=0.
$$


## Floquet modes and diffraction orders

Floquet's theorem reveals more than the relation between neighbors: the scattered field can be decomposed into spatial branches. A periodic lattice supplies integer multiples of reciprocal-lattice momentum. Each pair $(m,n)$ is a possible energy pathway. Order zero is the specular channel; higher orders can redirect the wave. Allowed pathways are not automatically populated: their amplitudes require a scattering calculation. With the negative spatial exponential used here, the following plus-sign order labeling is obtained by expanding the periodic envelope in negative-exponential Fourier harmonics.


$$
k_{x,m}=k_x+\frac{2\pi m}{p},\qquad m=0,\pm1,\pm2,\ldots
$$
$$
k_{x,m}=k_x+\frac{2\pi m}{p_x},\qquad
k_{y,n}=k_y+\frac{2\pi n}{p_y}.
$$


## Propagating, grazing and evanescent orders

The normal wavevector follows the dispersion relation below for a free-space exterior. A positive radicand permits propagation. A negative one produces an evanescent field that decays away from the surface. The source includes equality in its propagation inequality; equality is the grazing cutoff and must be treated separately because the normal power flux vanishes. For an exterior of index $n_o$, replace $k_0^2$ by $(n_ok_0)^2$. The outgoing evanescent root for positive $z$ has negative imaginary part under our convention.


$$
k_{z,mn}^2=k_0^2-k_{x,m}^2-k_{y,n}^2.
$$
$$
\begin{aligned}
k_{x,m}^2+k_{y,n}^2&<k_0^2 &&\text{propagating},\\
k_{x,m}^2+k_{y,n}^2&=k_0^2 &&\text{grazing cutoff},\\
k_{x,m}^2+k_{y,n}^2&>k_0^2 &&\text{evanescent}.
\end{aligned}
$$
$$
k_z=-i\kappa,\quad\kappa>0,\qquad e^{-ik_zz}=e^{-\kappa z}.
$$


## Grating lobes: unwanted energy pathways

One design task is to keep unwanted Floquet orders from opening. Such unwanted propagating channels are called grating lobes and may reduce desired-beam efficiency. At normal incidence in a one-dimensional free-space lattice, keeping the first orders evanescent gives the inequality below. Designers often choose $p<\lambda_0/2$ or $p<\lambda_0/3$. These are useful scales, not universal homogenization guarantees. At $10\,\mathrm{GHz}$, $p=20\,\mathrm{mm}$ keeps the first orders closed, whereas $p=40\,\mathrm{mm}$ opens them. Opening a channel does not prove that it carries power, and a closed higher order does not rule out absorption. For oblique incidence or a higher-index substrate, test both half-spaces explicitly.


$$
k_{x,m}=\frac{2\pi m}{p},\qquad
\frac{2\pi}{p}>k_0=\frac{2\pi}{\lambda_0}
\quad\Longrightarrow\quad p<\lambda_0.
$$


## Diffraction angles

In free space, substitute $k_{x,m}=k_0\sin\theta_m$ to obtain the grating equation. A real angle requires the right side to lie between minus one and one; the endpoints are grazing. At normal incidence with $p=45\,\mathrm{mm}$ and $\lambda_0=30\,\mathrm{mm}$, the first positive order is allowed at approximately $41.8^\circ$. Order two has a sine of approximately $1.33$ and is evanescent. The negative first order is also allowed by symmetry. A nonzero scattered amplitude still requires the structure to couple into the allowed order.


$$
\sin\theta_m=\sin\theta_i+\frac{m\lambda_0}{p}.
$$
$$
\sin\theta_1=\frac{30}{45}=\frac23,
\qquad\theta_1\simeq41.8^\circ,
\qquad\sin\theta_2=\frac{60}{45}>1.
$$


## Periodic boundaries and Floquet ports

Now the simulation setup in Chapter 3 makes sense. Periodic boundaries implement the neighboring-cell phase relation on opposite cell faces. A Floquet port decomposes input and output into the relevant spatial orders and polarizations. Software such as CST or HFSS can then report modal amplitudes and phases. Check each solver's phasor convention, port normalization, reference plane, and phase-shift direction before comparing its output with the course. Evanescent modes may be necessary for numerical convergence even though they do not form outgoing far-field beams.



## Floquet analysis and generalized Snell law

For a phase-lag profile $\Phi(x)$, generalized Snell law takes the form below. A linear profile $\Phi(x)=\beta_s x$ adds a tangential wavevector $\beta_s$. Floquet analysis instead supplies the discrete reciprocal-lattice increments. They are two views of tangential momentum change: a continuous phase-profile description and the discrete channels of a periodic lattice. For a repeated phase ramp, the complete complex transmission must repeat; a ramp changing by $2\pi q$ over a superperiod selects the corresponding nominal order. Neither description determines coupling efficiency.


$$
n_2\sin\theta_t-n_1\sin\theta_i
=\frac{\lambda_0}{2\pi}\frac{d\Phi}{dx},\qquad t(x)=A(x)e^{-i\Phi(x)}.
$$
$$
\Phi(x)=\beta_sx,\qquad\Delta k_x=\beta_s,
\qquad\Delta k_{x,m}=\frac{2\pi m}{p}.
$$
