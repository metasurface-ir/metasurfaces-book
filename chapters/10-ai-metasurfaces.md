---
title: 'Chapter 10: AI and Metasurfaces'
short_title: AI and Metasurfaces
description: Learn forward surrogates, inverse design, and physical validation through a reproducible resonant-sheet example.
---

# Chapter 10: AI and Metasurfaces

**Central question:** when does a learned model help us design a metasurface, and what evidence makes its proposed design credible?

Imagine building a library of unit cells. For every geometry, you solve Maxwell's equations over a frequency band and record complex reflection and transmission. A new specification arrives: a different phase, a broader band, or a different incidence angle. Can we reuse the library to search efficiently? Can we tell when the requested response lies outside what the library supports?

This chapter develops that workflow, from the electromagnetic problem to a learned approximation and back to electromagnetic verification. Start with the physical question; choose a learning method after defining the observable, constraints, and evidence you need.

:::{note} Chapter 10 pilot
The pilot includes this chapter, a [learning path and worked exercises](10-pilot-guide.md), two executed notebooks, and four [computational lab stages](../labs/13-ai-metasurfaces.md). Stage A is runnable with analytical data; Stages B-D specify future full-wave investigations. The examples demonstrate a learning workflow; they do not validate a fabricated geometry or a full-wave metasurface design.
:::

```{figure} ../assets/chapter-10/analytical-sheet.svg
:alt: Ideal sheet model with incident, reflected and transmitted waves, explicitly without an assigned particle geometry.

The executed AI pilot uses an analytical sheet response with an abstract design coordinate. No nanostructure is assigned to that coordinate. This drawing explains the scattering model; a physical ridge or other geometry requires the separate full-wave dataset stages.
```


## 10.1 Learning goals and prerequisites

After this chapter, you should be able to:

1. Write forward prediction, inverse design, and optimization as distinct mathematical problems.
2. Build a dataset whose inputs, outputs, normalization, and split match the intended physical claim.
3. Compare a learned surrogate with a simple baseline on geometries withheld from training.
4. Explain why an accurate average prediction can still yield an unreliable optimized design.
5. Validate a candidate against physical constraints and an independent electromagnetic calculation.

You should be comfortable with complex amplitudes, S parameters, power balance, basic linear algebra, and numerical optimization. Start with the NumPy kernel notebook, then use the scikit-learn comparison notebook. The [pilot guide](10-pilot-guide.md) gives a sequence and readiness checks. Use Chapters 2–4 for the wave, unit-cell, and diffraction prerequisites, Chapter 5 for synthesis, and Chapter 6 for the numerical verification needed before a full-wave dataset study.

## 10.2 Three problems that should be kept distinct

Let $\mathbf{x}$ describe the design: lengths, widths, thicknesses, rotation angles, material choices, or a spatial pattern. Let $\mathbf{c}$ describe the operating conditions: frequency, incident angle, polarization, temperature, or bias. Let $\mathbf{y}$ be the response we want to predict or control.

The electromagnetic **forward problem** is

$$
\mathbf{y}=F(\mathbf{x},\mathbf{c}).
$$

$F$ may be an analytical model, an RCWA calculation, a finite-element model, or an FDTD simulation. A learned surrogate $\widehat F_{\boldsymbol\theta}$ approximates this mapping over a specified domain. The trainable parameters $\boldsymbol\theta$ belong to the model; they are different from the design variables $\mathbf{x}$.

The **inverse-design problem** starts with a desired response $\mathbf{y}^{\star}$ and seeks one or more designs that produce it. One useful formulation is

$$
\mathbf{x}^{\star}=\underset{\mathbf{x}\in\mathcal X}{\operatorname{argmin}}
\left[D\!\left(F(\mathbf{x},\mathbf{c}),\mathbf{y}^{\star}\right)
+\lambda C(\mathbf{x})\right].
$$

$D$ measures the response mismatch, $\mathcal X$ defines admissible designs, and $C$ penalizes an undesirable property such as sensitivity to fabrication errors. Hard constraints, such as a minimum feature size, should remain explicit even if penalties are also used.

A **surrogate-assisted search** replaces expensive calls to $F$ during candidate selection with calls to $\widehat F$. The final candidate still needs evaluation with $F$, and often with a more accurate calculation than the one used to generate the training library.

```{mermaid}
flowchart TD
    A[Define geometry, conditions, and target] --> B[Generate and validate electromagnetic data]
    B --> C[Split by geometry and fit a forward surrogate]
    C --> D[Search for a feasible candidate]
    D --> E[Verify with the electromagnetic model]
    E --> F[Report performance, uncertainty, and cost]
    E -->|Add informative cases when needed| B
```

Early work by [Peurifoy et al.](https://doi.org/10.1126/sciadv.aar4206) illustrates learned forward scattering and inverse search for multilayer particles. That example motivates a computational approach; its performance does not establish accuracy for an unrelated unit-cell family.

:::{tip} Predict before calculating
If the training library contains only normal-incidence data, what supports a claim at $45^\circ$ incidence? Adding an angle input to a network is insufficient unless the training or physical model provides information about angle dependence.
:::

## 10.3 Decide what the model must predict

For a single polarization and a simple two-port unit-cell calculation, useful outputs may include complex $r$ and $t$. For polarization conversion, the output may be a Jones matrix. When several Floquet channels propagate, use the appropriate scattering matrix and preserve the mode ordering.

Intensity alone cannot recover phase. If an application needs wavefront control, training only on $|t|^2$ discards essential information. Conversely, optimizing phase while ignoring a near-zero amplitude can produce an unusable design.

### Complex representations and phase wrapping

A convenient representation is

$$
\mathbf{y}=(\operatorname{Re}t,\operatorname{Im}t,
\operatorname{Re}r,\operatorname{Im}r).
$$

At multiple frequencies, concatenate these quantities in a documented order. A complex transmission loss can be written as

$$
L_t=\frac{1}{N}\sum_{j=1}^{N}|\widehat t_j-t_j|^2.
$$

This expression equals the sum of squared real and imaginary errors. It avoids a discontinuity at a selected phase branch cut. An alternative is to represent phase with sine and cosine, together with a separate amplitude, while ensuring that the predicted sine/cosine pair is normalized when reconstructing phase.

Consider phases $179^\circ$ and $-179^\circ$. Their ordinary numerical difference is $358^\circ$, but their smallest angular separation is $2^\circ$. A circular error is

$$
\Delta\phi=\arg(\widehat t\,t^*).
$$

Report phase errors only where both amplitudes exceed a declared threshold. At a transmission zero, phase is undefined. Do not use a threshold to hide poor amplitude prediction: report amplitude errors and the fraction of excluded samples separately.

### Power normalization matters

For power-normalized propagating modes, the squared magnitude of an S parameter is a power fraction for the corresponding incident mode. An electric-field transmission coefficient between unequal media generally needs an impedance or longitudinal-wavevector factor before it becomes transmitted power. Record the solver's convention and reference planes. Never train on coefficients from incompatible normalizations without reconciling them.

## 10.4 Build a dataset that answers a physical question

Treat each simulation record as evidence with provenance. The following information belongs in the data description:

| Record | Why it matters |
| --- | --- |
| Geometry ID and dimensions with units | Identifies related spectra and permits reconstruction |
| Materials and dispersion model | The same geometry can have a different response with different material data |
| Frequency, angle, polarization, and port basis | Defines the excitation and output channels |
| Boundary conditions, mesh or harmonic order, and solver version | Makes the calculation reproducible |
| Complex response and normalization/reference planes | Preserves amplitude and phase meaning |
| Power balance and convergence evidence | Helps distinguish numerical artifacts from physical trends |
| Data split and provenance | Prevents accidental reuse of test examples during development |

### Split according to the claim

Suppose each geometry contributes 101 frequency samples. If you shuffle all rows and split them at random, the same geometry can appear in training and test sets at nearby frequencies. That experiment can assess interpolation within observed geometries; it does not establish performance on unseen geometries.

For new-geometry prediction, assign complete geometries to training, validation, or test sets. Fit scalers and other preprocessing only on the training set. Use validation data to choose model settings. Reserve the test set for the final evaluation. These practices follow the general guidance on leakage and preprocessing in the [scikit-learn documentation](https://scikit-learn.org/stable/common_pitfalls.html).

State the split's intended difficulty. Randomly held-out geometries within a dense design region test interpolation. A withheld geometric interval, material family, or incidence range tests a different and often harder form of generalization. Report these results separately.

:::{important} A solver label can be wrong
Learning from an unconverged solver can faithfully reproduce numerical error. Check representative resonances, extreme geometries, and difficult incidence conditions before generating a large dataset. A low machine-learning loss does not replace a convergence study.
:::

## 10.5 Start with a baseline you can understand

Before training a large network, try nearest-neighbor retrieval, interpolation, or a simple regression model. These baselines show how much information is already available in the library. Compare methods on the same split, input information, target representation, and error metrics.

### Kernel regression

The starter notebook uses a Gaussian kernel to compare scalar design parameters:

$$
k(g,g')=\exp\left[-\frac{(g-g')^2}{2\ell^2}\right].
$$

For training inputs $g_i$, define $K_{ij}=k(g_i,g_j)$. If the rows of $Y$ contain response spectra, kernel ridge regression solves

$$
(K+\alpha I)A=Y,\qquad
\widehat Y_{\mathrm{new}}=K_{\mathrm{new,train}}A.
$$

Solve the linear system rather than explicitly calculating a matrix inverse. The length scale $\ell$ controls smoothness across the design coordinate; $\alpha>0$ regularizes the fit. We select both on the validation set. Complex outputs can be handled as complex columns here, equivalently using separate real and imaginary targets with the same real kernel. See the [kernel ridge reference](https://scikit-learn.org/stable/modules/kernel_ridge.html) for the broader method.

A neural network replaces this kernel expansion with learned nonlinear transformations. A multilayer perceptron can accept a small parameter vector; a convolutional architecture may suit a pixelated geometry. Architecture alone does not determine performance. Training-data coverage, target choice, regularization, and the evaluation problem remain central.

### A neural surrogate you can inspect

For the scalar design coordinate in our example, standardize the input using the training mean and standard deviation:

$$
\widetilde g=(g-\mu_{\mathrm{train}})/\sigma_{\mathrm{train}}.
$$

One hidden layer and a linear output layer give

$$
\mathbf h=\tanh(W_1\widetilde g+\mathbf b_1),\qquad
\widehat{\mathbf y}=W_2\mathbf h+\mathbf b_2.
$$

Here $\mathbf h$ is a learned feature vector, not an electromagnetic field. For $M$ frequencies, pack the output as $[\operatorname{Re}t_1,\ldots,\operatorname{Re}t_M,\operatorname{Im}t_1,\ldots,\operatorname{Im}t_M]$. With $H$ hidden units, the matrices have shapes $H\times1$ and $2M\times H$. Biases add $H+2M$ parameters. With $M=101$ and $H=32$, the network has $2H+(H+1)2M=6730$ trainable parameters. The 40 training geometries still provide only 40 independently sampled spectra; 101 frequencies do not turn them into 4040 independent geometries.

```{mermaid}
flowchart TD
    G[Design coordinate g] --> S[Scale using training statistics]
    S --> H[Learned tanh hidden units]
    H --> Y[202 real output coordinates]
    Y --> T[101 complex transmission amplitudes]
    T --> V[Evaluate spectral and physical errors]
```

A useful conceptual training objective combines response error and weight regularization:

$$
L(\boldsymbol\theta)=\frac{1}{NM}\sum_{i=1}^{N}\sum_{j=1}^{M}
|\widehat t_{ij}-t_{ij}|^2+\beta\sum_{\ell}\|W_{\ell}\|_F^2.
$$

Backpropagation applies the chain rule to compute derivatives of this loss with respect to weights and biases. The optimizer then updates them. During forward-model training, the design coordinates and reference spectra remain fixed. During an inverse search, the trained weights remain fixed and the candidate design changes. Keeping those two operations separate prevents a common conceptual error.

Software loss conventions matter. Averaging squared error over $2M$ packed real coordinates gives half the mean squared complex error over $M$ frequencies. Libraries also normalize regularization differently. The conceptual $\beta$ above is therefore not a claim that two packages' `alpha` parameters are interchangeable. The notebook selects models using a separately calculated complex RMSE.

Our MLP uses tanh hidden units, linear outputs, L2 regularization, and L-BFGS optimization. It standardizes inputs using training data and reports optimizer warnings. Feature scaling and initialization sensitivity are discussed in the [scikit-learn neural-network guide](https://scikit-learn.org/stable/modules/neural_networks_supervised.html); the [MLPRegressor API](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html) documents the optimizer controls. A maximum-iteration warning means the requested stopping criterion has not been established. It must remain part of the reported evidence.

### Make the comparison fair and interpretable

The [executed comparison](../notebooks/10-neural-comparison.ipynb) uses identical geometry IDs and spectra for nearest retrieval, complex linear interpolation, KRR, and an MLP. KRR has 12 validation candidates; the MLP has six. This is a comparison under declared small search budgets, not an equal-compute competition. Architecture and regularization are chosen on validation data using a fixed initialization. Two additional neural initializations are then evaluated without changing the configuration or selecting a lucky seed.

Linear interpolation is a particularly useful baseline for one smooth design coordinate. It brackets a query between training coordinates and blends their complex spectra. Outside that bracketed region the implementation clips to the closest endpoint and reports how many test coordinates fall outside the training range. Neither interpolation nor a neural network provides evidence for an untested material or geometry family.

Use several complementary metrics: complex-response RMSE, power-fraction error, maximum error over the band, and phase error above the amplitude threshold. Report results per geometry as well as an aggregate; a small average can conceal a failed narrow resonance.

```{figure} ../assets/chapter-10/model-comparison.png
:alt: Analytical transmission spectra and per-design errors for retrieval, linear interpolation, kernel ridge regression, and a neural network.
:label: fig-ch10-comparison

Saved output from the comparison notebook, using the declared 40/20/20 split. This is an analytical teaching experiment; its ranking does not establish a universal best model. The notebook contains the numerical tables, initialization results, and complete code.
```

In the published run, test complex RMSE is approximately $0.0414$ for retrieval, $0.00800$ for interpolation, $0.000353$ for KRR, and $0.0165$ for the primary MLP. The network improves on retrieval but does not beat the two smoother baselines on this task. Across its three initializations, MLP RMSE has mean $0.0232$ and sample standard deviation $0.00732$. This describes training variability on one fixed split, not a confidence interval for performance on other datasets. Three rejected validation configurations emit optimizer warnings; the selected configuration and its repeats finish without warnings. The notebook preserves all of that evidence.

## 10.6 Why inverse design is not simply the forward map reversed

Different geometries can produce nearly the same response. The inverse mapping may therefore be set-valued. An illustrative algebraic example is $y=x^2$: for $y=1$, both $x=-1$ and $x=1$ are valid, but their average $x=0$ fails. A regression model trained to average conflicting inverse labels can therefore return a design that matches none of the valid solutions.

One remedy is to search through a forward surrogate. Another is a **tandem network**: an inverse model $G_{\boldsymbol\phi}$ proposes a geometry, and a fixed, previously trained forward surrogate scores its response:

$$
L_{\mathrm{tandem}}=
D\left(\widehat F_{\boldsymbol\theta}(G_{\boldsymbol\phi}(\mathbf{y}^{\star})),
\mathbf{y}^{\star}\right).
$$

The forward model's weights remain fixed while gradients update the inverse model. [Liu et al.](https://doi.org/10.1021/acsphotonics.7b01377) developed this approach to address non-unique inverse scattering examples. It shifts the training objective toward response consistency, but still inherits forward-model errors. Geometry bounds and manufacturing constraints must also be enforced.

Conditional generative models offer a further possibility: generate several candidate geometries for a target, then filter and verify them. Their diversity is useful only if candidates are feasible and their verified responses satisfy the task. A visually plausible pattern is not evidence of electromagnetic performance.

### Optimization can exploit model errors

Consider a surrogate with small average error but an incorrectly predicted high-efficiency region near a data boundary. An optimizer may select precisely that region. Its search is not a random draw from the test distribution, so average test error can underestimate the risk at the chosen design.

Evaluate several promising candidates with the original model, inspect where the proposed design lies relative to the data, and refine the training set when appropriate. Keep the final test set independent of this adaptation. For costly solvers, active learning can select new simulations based on uncertainty or expected improvement, but compare the total number and cost of simulations with a conventional search.

## 10.7 Physical checks, uncertainty, and verification

For a passive device represented in a complete, compatible power-normalized propagating-port basis, the scattering matrix obeys

$$
S^{\dagger}S\preceq I.
$$

For a lossless device it becomes equality when all outgoing power channels are included. Reciprocity can impose $S=S^{\mathsf T}$ in an appropriately paired modal basis. Do not impose these relations blindly on evanescent amplitudes, truncated channel sets, incompatible normalizations, or active/nonreciprocal systems.

These relations can be used as diagnostics, architectural constraints, or additional training penalties. Satisfying a penalty at a finite set of samples does not prove broadband causality or correctness for unseen geometries. A power-balanced model can still predict the wrong phase or resonance frequency.

Uncertainty estimates also require evaluation. An ensemble's spread or a probabilistic model's variance can be informative, but should be checked against held-out errors and domain shifts. Disagreement and confidence are not automatic guarantees. Distinguish uncertainty in the surrogate from uncertainty in geometry, material data, measurement, and the electromagnetic solver itself.

For a final design, report:

1. Its design vector, constraints, and operating conditions.
2. The surrogate prediction and the independently evaluated response on the same axes.
3. Mesh/harmonic/domain convergence and all-channel power accounting where applicable.
4. Sensitivity to fabrication and material variation.
5. Data-generation, training, search, and verification costs.

If generating the training data costs $N_{\mathrm{data}}C_{\mathrm{EM}}$, then the total learning-assisted cost includes

$$
C_{\mathrm{total}}=N_{\mathrm{data}}C_{\mathrm{EM}}+C_{\mathrm{train}}
+N_{\mathrm{query}}C_{\mathrm{surrogate}}+N_{\mathrm{verify}}C_{\mathrm{EM}}.
$$

Use measured costs appropriate to the actual solver and hardware. A fast prediction may be attractive for repeated design tasks while offering no overall saving for a single design.

## 10.8 Worked model: a synthetic resonant sheet

To practice the workflow without a commercial solver, consider a lossless symmetric two-port model with equal media, power-normalized amplitudes, and time dependence $e^{-i\omega t}$. Define normalized frequency $\Omega=\omega/\omega_{\mathrm{ref}}$, normalized linewidth $\gamma>0$, and detuning $\Delta=\Omega-\Omega_0$:

$$
r=-\frac{\gamma}{\gamma-i\Delta},\qquad
t=1+r=\frac{-i\Delta}{\gamma-i\Delta}.
$$

It follows directly that

$$
R=\frac{\gamma^2}{\gamma^2+\Delta^2},\quad
T=\frac{\Delta^2}{\gamma^2+\Delta^2},\quad R+T=1.
$$

At resonance, $r=-1$ and $t=0$. Far from resonance, transmission approaches unity. For the example, let a dimensionless design coordinate $g\in[0,1]$ control

$$
\Omega_0(g)=0.9+0.2g,\qquad \gamma(g)=0.025+0.02g.
$$

This mapping is deliberately synthetic: $g$ is not a documented pillar radius or fabricated geometry. The notebook samples entire spectra at different $g$, fits a surrogate on one subset, chooses its settings on a validation subset, and evaluates held-out designs. It then searches for a target spectrum and checks the selected candidate against the exact formula.

For a symmetric two-port matrix $S=\begin{pmatrix}r&t\\t&r\end{pmatrix}$, power balance for one incident port is only the diagonal part of $S^\dagger S=I$. The off-diagonal condition is $r^*t+t^*r=0$. Here $r^*t=i\gamma\Delta/(\gamma^2+\Delta^2)$ is purely imaginary, so that condition also holds. The comparison notebook checks both identities. They apply to this model and its specified port basis.

Retrieving an exact training spectrum automatically preserves this model's power balance, even when its resonance is in the wrong place for the requested design. Conversely, a regression can have very small complex error and a nonzero power residual. Accuracy and physical consistency answer different questions; report both.

### Inspect physical consistency in the complex plane

For this reconstructed equal-air electric sheet, the signed quantity

$$
A_{\mathrm{implied}}=1-|\widehat t-1|^2-|\widehat t|^2
=\frac12-2\left|\widehat t-\frac12\right|^2.
$$

vanishes on a circle centered at $1/2$ with radius $1/2$. Its interior corresponds to a passive reconstructed response; its exterior would require gain under these specific assumptions. The comparison notebook plots the frozen predictions in this plane and reports the signed diagnostic over all held-out geometries.

Complex linear interpolation joins lossless training responses by chords inside that disk. It can therefore introduce artificial loss relative to the generator while preserving passivity. Nearest retrieval stays on the lossless circle even when the retrieved resonance is wrong. A small response error, passivity, and losslessness are distinct checks. Projecting onto the circle alone would not establish spectral accuracy, causality, or a realizable geometry.

```{figure} ../assets/chapter-10/passivity-locus.png
:alt: Complex transmission predictions compared with the lossless electric-shunt circle and the signed implied absorption over frequency for one fixed held-out design.

Original calculation from the frozen analytical comparison. The circle and interpolation chord expose artificial loss or implied gain in the reconstructed model. The signed quantity is a surrogate diagnostic, not measured material absorption; the notebook table also covers all held-out geometries.
```

That last step verifies the surrogate against its analytical data generator. It is not independent full-wave or experimental validation. The next lab stage replaces this generator with a converged unit-cell library while preserving the split, metrics, and reporting structure.

**Continue with the [Chapter 10 computational lab](../labs/13-ai-metasurfaces.md).**

For the inverse comparison, retrieval returns an actual library design. Continuous surrogates search 901 coordinates separated by $0.001$. A retrieval objective is flat between changes in the nearest neighbor, so attaching its winning spectrum to an arbitrary coordinate in that interval would be misleading. The notebook makes this distinction explicit and verifies every proposed coordinate with the analytical generator.

```{figure} ../assets/chapter-10/inverse-comparison.png
:alt: Verified transmission spectra of proposed designs and a separate comparison of the neural prediction with analytical verification.
:label: fig-ch10-inverse

Inverse proposals from the comparison notebook. The target lies on the candidate grid, so some verified curves coincide exactly with it. The numerical table in the notebook distinguishes a small predicted mismatch from the actual mismatch after analytical verification.
```

## 10.9 Exercises and research discussion

1. Derive $R+T=1$ for the synthetic model. Explain why phase error is inappropriate at $\Delta=0$.
2. Construct two unit-magnitude complex coefficients at $179^\circ$ and $-179^\circ$. Compare ordinary phase subtraction, circular error, and complex-amplitude error.
3. Design two dataset splits: one for interpolation to new geometries and another for testing a withheld design interval. State exactly what each result would support.
4. A model predicts transmission with 1% mean power error. What additional evidence would you need before using it to design a metalens?
5. Explain how a tandem model can produce a small training loss and still propose an inaccurate design. Suggest a validation procedure.
6. Estimate the break-even number of repeated design tasks for a hypothetical library. Include data generation, failed simulations, retraining, and verification.
7. Propose a fabrication-robust objective such as expected response error plus a variance penalty. Explain how you would sample perturbations and evaluate worst cases separately.
8. Read one paper below and identify the design space, output representation, data generator, split, baseline, inverse objective, and independent verification. Which claims transfer to your proposed metasurface problem?

The [pilot guide](10-pilot-guide.md) includes worked examples for conservation, phase wrapping, data leakage, inverse ambiguity, and computational cost. Use the remaining questions for discussion and independent reports.

## References and further reading

- Peurifoy et al., *Nanophotonic particle simulation and inverse design using artificial neural networks*, Science Advances 4, eaar4206 (2018). [Article](https://doi.org/10.1126/sciadv.aar4206). A forward-surrogate and inverse-search example for multilayer particles.
- Liu et al., *Training Deep Neural Networks for the Inverse Design of Nanophotonic Structures*, ACS Photonics 5, 1365-1369 (2018). [Article](https://doi.org/10.1021/acsphotonics.7b01377); [author preprint](https://arxiv.org/abs/1710.04724). Read for the non-uniqueness problem and tandem construction.
- Malkiel et al., *Plasmonic nanostructure design and characterization via Deep Learning*, Light: Science & Applications 7, 60 (2018). [Article](https://doi.org/10.1038/s41377-018-0060-7). A case study connecting learned design/characterization to experiments.
- Molesky et al., *Inverse design in nanophotonics*, Nature Photonics 12, 659-670 (2018). [Review](https://doi.org/10.1038/s41566-018-0246-9). Broader context for optimization beyond machine learning.
- scikit-learn, [Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) and [Kernel ridge regression](https://scikit-learn.org/stable/modules/kernel_ridge.html). Methodological references for data handling and the starter regression model.

These are foundational readings, not an exhaustive survey of current AI methods. The synthetic teaching model and exercises on this page are original course material.
