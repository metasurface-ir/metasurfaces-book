---
title: "5.7 Optimization and inverse design"
---

# 5.7 Optimization and inverse design

So far our synthesis has mostly followed a forward, heuristic route: choose a familiar rectangular patch, split ring or cross, simulate it in CST or HFSS, obtain its calibration curve, and assemble cells using local periodicity.

But complicated, multifunctional requirements—multiple bands, several incidence angles or nonlinear phase/amplitude relationships—can defeat manual trial and error or reduce efficiency. Inverse design and optimization algorithms change how we search.

**Traditional route:** specified geometry → electromagnetic simulation → inspect response → manually adjust dimensions, in a time-consuming loop.

**Inverse route:** desired response → optimization or AI → automatic synthesis of a candidate geometry.

### 5.7.1 Write synthesis as an optimization problem

The goal is a geometric parameter vector $\mathbf p=[p_1,p_2,\ldots,p_N]^T$ minimizing a specified cost:

$$
\min_{\mathbf p}\mathcal L(\mathbf p)\quad\text{subject to}\quad\mathbf p_{\min}\le\mathbf p\le\mathbf p_{\max}.
$$

The cost measures the mismatch between simulated fields $E_{\rm sim}$ or scattering parameters $S_{\rm sim}$ and the desired response $E_{\rm target}$:

$$
\mathcal L(\mathbf p)=w_1\int_\Omega\|E_{\rm sim}(\mathbf p,\mathbf r)-E_{\rm target}(\mathbf r)\|^2\,d\mathbf r+w_2(1-\eta_{\rm eff})+\operatorname{Penalty}(\mathbf p).
$$

Here:

- $w_1,w_2$ weight the priorities of different design objectives.
- $\eta_{\rm eff}$ is useful output-power efficiency.
- $\operatorname{Penalty}$ penalizes violations of fabrication rules (DRC), such as slots or lithographic traces below the process minimum.

### 5.7.2 Gradients and the adjoint method

For continuous geometric parameters, the source presents gradient methods as a fast route to an optimum. But computing each partial derivative $\partial\mathcal L/\partial p_i$ by perturbing one variable and repeating the simulation becomes extremely expensive for thousands of pixels—potentially months of work!

The adjoint-state method addresses this bottleneck and resembles backpropagation in neural networks.

1. **Forward simulation:** excite the structure with the original source and record $E_{\rm fwd}$.
2. **Adjoint simulation:** place a virtual source at the output, with amplitude related to response error, and excite the structure to obtain $E_{\rm adj}$.
3. **Extract the gradient:** combine the two fields point by point to obtain sensitivity to material changes across the surface. The source gives the schematic relation

$$
\frac{\partial\mathcal L}{\partial\epsilon(\mathbf r)}\propto\operatorname{Re}\{E_{\rm fwd}(\mathbf r)\cdot E_{\rm adj}(\mathbf r)\}.
$$

Thus, in the source’s single-objective setting, gradients for all pixels or parameters are obtained with only two field solves: a major computational saving. The exact derivative and solve count need the qualifications below.

### 5.7.3 Metaheuristic and stochastic algorithms

When the response landscape is highly nonconvex with many local minima, or variables are discrete—binary metal/no-metal pixels, for example—ordinary gradients can get trapped or be inapplicable. Evolutionary and swarm methods provide alternatives.

**Genetic algorithm (GA).** Encode pixels as binary chromosomes: zero for dielectric and one for copper. Crossover and mutation evolve patterns over generations. The source emphasizes that unexpected, innovative patterns can emerge to meet the target.

**Particle swarm optimization (PSO).** Particles move through geometric parameter space, adjusting their motion according to personal best $p_{\rm best}$ and group best $g_{\rm best}$ experiences.

### 5.7.4 Deep-learning approaches

Deep neural networks can act as very fast surrogate models for numerical simulators. The source describes examples where synthesis after training drops from hours to a fraction of a second.

**Forward network.** Input geometry such as $[L,W]$ and rapidly estimate amplitude, phase or the scattering matrix.

**Inverse and tandem networks.** Desired phase/amplitude goes in and geometry comes out. The difficulty is one-to-many mapping: several geometries can give the same electromagnetic response, creating conflicting training labels. In a tandem architecture, a pretrained, frozen forward network follows the inverse network, so training loss is measured on the predicted physical response. The source says this completely resolves nonuniqueness; the separate note explains the distinction between resolving label conflict and removing physical nonuniqueness.

**Generative models (GANs and VAEs).** These enable freeform design beyond standard squares and circles, producing complex patterns. The source describes them as offering the highest scattering efficiency and bandwidth; these are design aspirations, not a guarantee of global optimality.

:::{admonition} Worked exercise
:class: tip
State the main difference between direct and inverse design.

```{dropdown} Show the worked answer

In direct design, choose a geometry first and simulate its electromagnetic response. If the result is unsuitable, manually modify the geometry. In inverse design, specify the desired response first, then use optimization or AI to find a geometry that can produce it.

```
:::

:::{admonition} Worked exercise
:class: tip
A cell is described by length, width and thickness. Write its geometric parameter vector.

```{dropdown} Show the worked answer

Define the vector as

$$
\mathbf p=\begin{bmatrix}L\\W\\h\end{bmatrix}.
$$

Here $L$ is cell length, $W$ is cell width, and $h$ is the thickness of its metal or dielectric layer.

```
:::

:::{admonition} Worked exercise
:class: tip
Write inverse design as an optimization problem for geometric parameters that realize a desired electromagnetic response.

```{dropdown} Show the worked answer

Collect the geometric parameters into

$$
\mathbf p=\begin{bmatrix}p_1\\p_2\\\vdots\\p_N\end{bmatrix}.
$$

Choose them to minimize cost:

$$
\min_{\mathbf p}\mathcal L(\mathbf p).
$$

Fabrication bounds usually apply, giving

$$
\min_{\mathbf p}\mathcal L(\mathbf p)\quad\text{subject to}\quad\mathbf p_{\min}\le\mathbf p\le\mathbf p_{\max}.
$$

$\mathcal L$ is design error or cost, $\mathbf p_{\min}$ contains minimum allowed geometric values, and $\mathbf p_{\max}$ contains the maximum values. The aim is a geometry with minimal electromagnetic mismatch while respecting fabrication limits.

```
:::

:::{admonition} Worked exercise
:class: tip
What does the cost function measure in inverse design?

```{dropdown} Show the worked answer

It measures the mismatch between simulated and desired responses. Smaller mismatch indicates a better design under the chosen objective. For example, use field error:

$$
\mathcal L=\int_\Omega\|E_{\rm sim}-E_{\rm target}\|^2\,d\mathbf r.
$$

Efficiency and fabrication limits can also be included.

```
:::

:::{admonition} Worked exercise
:class: tip
Explain $w_1,w_2$ in $\mathcal L=w_1\mathcal L_{\rm field}+w_2(1-\eta_{\rm eff})$.

```{dropdown} Show the worked answer

They set relative priorities:

- $w_1$ controls the importance of reducing field or electromagnetic-response error.
- $w_2$ controls the importance of increasing efficiency.

Increasing $w_2$ gives greater priority to efficiency, with other scaling held fixed.

```
:::

:::{admonition} Worked exercise
:class: tip
Why include a penalty term in the cost?

```{dropdown} Show the worked answer

It discourages designs that are unsuitable or impossible to fabricate. If a slot or metal trace is narrower than the process minimum, add a cost:

$$
\mathcal L_{\rm total}=\mathcal L_{\rm error}+\operatorname{Penalty}.
$$

$\mathcal L_{\rm error}$ measures electromagnetic mismatch and Penalty is the additional cost of violating fabrication limits. This guides the search toward designs that perform well and can be made.

```
:::

:::{admonition} Worked exercise
:class: tip
Give one simple difference between GA and PSO.

```{dropdown} Show the worked answer

GA evolves designs through generations, crossover and mutation. PSO moves particles through the design space using their personal and collective best experiences. Typically GA suits discrete variables and binary patterns; PSO is used for numerical, continuous parameters.

```
:::

:::{admonition} Worked exercise
:class: tip
What are the input and output of a forward neural network for metasurfaces?

```{dropdown} Show the worked answer

Input is cell geometry, for example

$$
[L,W].
$$

Output is the electromagnetic response, for example

$$
|S_{21}|,\qquad\arg S_{21}.
$$

More generally, it predicts response amplitude and phase.

```
:::

:::{admonition} Worked exercise
:class: tip
Suggest a method for (a) continuous patch length/width optimization; (b) a binary metal pattern; (c) fast cell-response prediction after training.

```{dropdown} Show the worked answer

(a) A gradient method or PSO. (b) A genetic algorithm. (c) A forward neural network as a surrogate model.

```
:::

:::{admonition} Worked exercise
:class: tip
A cost is $\mathcal L=w_1E_{\rm field}+w_2(1-\eta)$. Calculate it for $w_1=2$, $w_2=1$, $E_{\rm field}=0.1$, $\eta=0.8$.

```{dropdown} Show the worked answer

First,

$$
1-\eta=1-0.8=0.2.
$$

Therefore,

$$
\mathcal L=2(0.1)+1(0.2).
$$

$$
\mathcal L=0.2+0.2.
$$

The result is

$$
\mathcal L=0.4.
$$

A smaller value indicates closer agreement with the selected combined objective.

```
:::

:::{admonition} Worked exercise
:class: tip
List the three main stages of simulation- and optimization-based inverse design.

```{dropdown} Show the worked answer

1. **Define the target and cost:** specify amplitude, phase, efficiency and fabrication limits.
2. **Search the design space:** use gradients, adjoints, GA, PSO or neural models as appropriate.
3. **Validate the final geometry:** simulate the complete structure and compare actual and target responses, accounting for mutual coupling and fabrication limits.

```
:::


:::{admonition} Scientific clarification — separate from the primary reading
:class: note
Gradient methods need differentiability and may converge to local stationary points; neither they nor GA/PSO guarantee the global optimum. A two-solve adjoint statement applies per suitable scalar objective and excitation/frequency setting. Additional independent objectives, sources or frequencies may require additional solves. The exact derivative includes operator/material derivatives, normalization, prefactors and possibly conjugation; the field-overlap expression is schematic, not an implementation recipe.

Tandem training reduces conflicting inverse labels by scoring response, but does not eliminate the physical many-to-one map or surrogate error. Validate every chosen geometry independently. GAN/VAE samples are not guaranteed optimal, feasible or outside the training distribution. Surrogate speed claims concern inference after data generation and training. Normalize the objective terms, separate training/selection/validation data and enforce nonnegotiable fabrication limits as hard constraints when a finite penalty is insufficient.
:::
