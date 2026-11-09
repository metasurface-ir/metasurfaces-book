---
title: "5.7 Optimization and inverse design"
---

# 5.7 Optimization and inverse design

Trial-and-error geometry tuning becomes expensive for multiband, multi-angle or multifunctional targets. Define a parameter vector and a constrained cost: field mismatch, efficiency penalty and fabrication rules. Scale the terms so their weights have an interpretable meaning.

For differentiable continuous designs, gradient methods are useful but do not guarantee a global optimum. An adjoint method avoids perturbing each pixel separately: solve the forward system, solve an objective-dependent adjoint system, and combine the fields to obtain sensitivities. The often quoted two solves apply to a single scalar objective and excitation/frequency condition; multiple conditions can require more solves. The exact signs, conjugations and prefactors depend on the chosen operator and real-valued objective.

Genetic algorithms use populations, crossover and mutation and are useful for discrete patterns; PSO moves particles using personal and group best locations. They can be expensive and provide no global guarantee. A trained forward surrogate predicts response from geometry. A tandem inverse network evaluates its proposed geometry through a frozen forward model: this addresses conflicting inverse labels but does not remove physical nonuniqueness or surrogate error. GANs and VAEs can propose freeform candidates; neither guarantees optimal bandwidth or efficiency. Finish every route with independent electromagnetic and fabrication checks, including coupling.


$$
\mathbf p=[p_1,\ldots,p_N]^T,\qquad
\min_{\mathbf p}\mathcal L(\mathbf p)
\quad\text{subject to}\quad\mathbf p_{\min}\le\mathbf p\le\mathbf p_{\max}.
$$
$$
\mathcal L=w_1\int_\Omega|E_{\rm sim}(\mathbf p,\mathbf r)-E_{\rm target}(\mathbf r)|^2\,d\mathbf r
+w_2(1-\eta_{\rm eff})+\operatorname{Penalty}(\mathbf p).
$$
$$
A(\mathbf p)u=b,\qquad A^\dagger\lambda=g,
\qquad
\frac{d\mathcal L}{dp_j}=-2\operatorname{Re}\left[\lambda^\dagger\frac{\partial A}{\partial p_j}u\right]
+\left.\frac{\partial\mathcal L}{\partial p_j}\right|_u.
$$


:::{admonition} Worked exercise 1
:class: tip
How do direct and inverse design differ?

```{dropdown} Show the answer


Direct design starts from geometry and evaluates its response; inverse design starts from a target and searches for feasible geometry.
```
:::


:::{admonition} Worked exercise 2
:class: tip
Write the geometric parameter vector for length, width and thickness.

```{dropdown} Show the answer
$$\mathbf p=[L,W,h]^T.$$

Each component must have a specified unit and bound.
```
:::


:::{admonition} Worked exercise 3
:class: tip
Formulate bounded inverse design.

```{dropdown} Show the answer
$$\min_{\mathbf p}\mathcal L(\mathbf p)\quad\text{subject to}\quad\mathbf p_{\min}\le\mathbf p\le\mathbf p_{\max}.$$

Minimize mismatch while respecting geometric bounds and fabrication requirements.
```
:::


:::{admonition} Worked exercise 4
:class: tip
What does a cost function measure?

```{dropdown} Show the answer
$$\mathcal L_{\rm field}=\int_\Omega|E_{\rm sim}-E_{\rm target}|^2\,d\mathbf r.$$

Mismatch between simulated and desired responses, possibly augmented by efficiency and fabrication terms.
```
:::


:::{admonition} Worked exercise 5
:class: tip
What do the weights do?

```{dropdown} Show the answer
$$\mathcal L=w_1\mathcal L_{\rm field}+w_2(1-\eta).$$

They set the relative priorities after the terms are appropriately scaled. Increasing the efficiency weight favors efficiency relative to field error.
```
:::


:::{admonition} Worked exercise 6
:class: tip
Why include a fabrication penalty?

```{dropdown} Show the answer
$$\mathcal L_{\rm total}=\mathcal L_{\rm error}+\operatorname{Penalty}.$$

It penalizes violations such as gaps or traces below the process minimum. Check hard constraints separately when a violation is unacceptable.
```
:::


:::{admonition} Worked exercise 7
:class: tip
Compare GA and PSO.

```{dropdown} Show the answer


GA evolves populations using crossover and mutation; PSO moves particles using personal and group bests. GA often suits binary patterns, while PSO commonly searches continuous dimensions.
```
:::


:::{admonition} Worked exercise 8
:class: tip
What are the input and output of a forward neural surrogate?

```{dropdown} Show the answer
$$[L,W]\ \longmapsto\ S_{21}\quad\text{or}\quad(|S_{21}|,\arg S_{21}).$$

Geometry goes in; complex scattering or amplitude and phase come out. Its accuracy is limited to the validated domain.
```
:::


:::{admonition} Worked exercise 9
:class: tip
Suggest methods for a continuous patch, a binary pattern and fast prediction after training.

```{dropdown} Show the answer


A gradient method or PSO; a genetic algorithm; and a forward surrogate, respectively. Method choice also depends on cost, differentiability and constraints.
```
:::


:::{admonition} Worked exercise 10
:class: tip
Calculate the cost for field error 0.1, efficiency 0.8, and weights 2 and 1.

```{dropdown} Show the answer
$$\mathcal L=2(0.1)+1(1-0.8)=0.2+0.2=0.4.$$

The weighted field mismatch and efficiency penalty each contribute 0.2.
```
:::


:::{admonition} Worked exercise 11
:class: tip
List three stages of simulation-based inverse design.

```{dropdown} Show the answer


Define target, cost and constraints; search the design space; independently validate the final geometry including coupling and fabrication.
```
:::


For this adjoint expression, the source vector is fixed and the state differential is defined by the following equation.

$$\left.d\mathcal L\right|_{\mathbf p}=2\operatorname{Re}(g^\dagger du).$$
