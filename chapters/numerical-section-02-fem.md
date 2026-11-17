---
title: "6.2.1 Finite elements: from strong form to edge unknowns"
---

# 6.2.1 Finite elements: from strong form to edge unknowns

All right, let us meet the electromagnetic engineer’s versatile toolkit: the finite element method. FEM, used in packages such as HFSS and COMSOL, rests on variational analysis and solves boundary-value problems in complicated geometries. Let us look under the hood.

## 1. Derive the strong vector wave equation

Start from the curl equations, with an impressed current source:

$$
\nabla\times\mathbf E=-i\omega\mathbf B,\qquad\nabla\times\mathbf H=i\omega\mathbf D+\mathbf J_{\rm imp}.
$$

The material relations are

$$
\mathbf D=\epsilon_0\overline{\overline\epsilon}_r\mathbf E,\qquad\mathbf B=\mu_0\overline{\overline\mu}_r\mathbf H.
$$

To keep the algebra approachable, the source reduces these tensors to effective complex scalars. Eliminate the magnetic field using Faraday’s law:

$$
\mathbf H=-\frac{1}{i\omega\mu_0\mu_r}\nabla\times\mathbf E.
$$

Multiply by the inverse permeability, then take another curl:

$$
\mu_r^{-1}\nabla\times\mathbf E=-i\omega\mu_0\mathbf H.
$$

$$
\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)=-i\omega\mu_0\nabla\times\mathbf H.
$$

Insert Ampère–Maxwell:

$$
\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)=-i\omega\mu_0(i\omega\epsilon_0\epsilon_r\mathbf E+\mathbf J_{\rm imp}).
$$

With the free-space wavenumber, the result is

$$
k_0^2=\omega^2\mu_0\epsilon_0,\qquad\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E=-i\omega\mu_0\mathbf J_{\rm imp}.
$$

That is the strong form. Directly demanding classical second derivatives everywhere is awkward near material discontinuities and sharp edges. The weak form lowers the differentiability required of the approximation.

## 2. Weighted residuals and integration by parts

$$
\mathbf R=\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E+i\omega\mu_0\mathbf J_{\rm imp}.
$$

Instead of forcing zero residual at every point, multiply by a test field and integrate over the volume. The source initially writes an unconjugated test field:

$$
\int_V\mathbf W\cdot[\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E],dV=-i\omega\mu_0\int_V\mathbf W\cdot\mathbf J_{\rm imp},dV.
$$

The vector identity and divergence theorem move one curl to the test function:

$$
\int_V\mathbf W\cdot\nabla\times\mathbf A,dV=\int_V(\nabla\times\mathbf W)\cdot\mathbf A,dV-\int_{\partial V}(\mathbf W\times\mathbf A)\cdot\hat{\mathbf n},dS.
$$

The printed source then gives the following boundary-sign form. The separate correction immediately below matters for implementation.

$$
\int_V[\mu_r^{-1}(\nabla\times\mathbf W)\cdot(\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf W\cdot\mathbf E],dV+i\omega\mu_0\int_{\partial V}\mathbf W\cdot(\hat{\mathbf n}\times\mathbf H),dS=-i\omega\mu_0\int_V\mathbf W\cdot\mathbf J_{\rm imp},dV.\quad\text{[printed]}
$$

:::{admonition} Scientific clarification — separate from the source
:class: note
For an outward normal, the integration identity and $\mu_r^{-1}\nabla\times\mathbf E=-i\omega\mu_0\mathbf H$ give a **minus** sign on the boundary term on the left:

$$
a(\mathbf E,\mathbf W)-i\omega\mu_0\int_{\partial V}\mathbf W^*\cdot(\hat{\mathbf n}\times\mathbf H),dS=-i\omega\mu_0\int_V\mathbf W^*\cdot\mathbf J_{\rm imp},dV.
$$

Here $a$ is the volume curl–curl minus mass form and complex Galerkin testing uses $\mathbf W^*$. For an outgoing exterior wave, $\hat{\mathbf n}\times\mathbf H=-Y\mathbf E_t$; the resulting matrix boundary contribution is therefore positive $i\omega\mu_0 B_Y$. The source’s later symbolic admittance definition uses the opposite sign. Normal orientation, boundary admittance and weak form must be converted together. [MFEM’s weak-curl derivation](https://mfem.org/fem_weak_form/) provides the integration identity.
:::

The attraction is clear: only first curls remain, tangential continuity fits naturally, and boundary physics enters through surface integrals.

## 3. Boundary conditions

At PEC, tangential electric trial and test traces vanish. An impedance boundary represents a thin conductive layer such as graphene without meshing its atomic thickness. The source writes the surface relation using $Z_s$:

$$
\int_{S_{\rm IBC}}\mathbf W\cdot(\hat{\mathbf n}\times\mathbf H),dS=\frac1{Z_s}\int_{S_{\rm IBC}}(\hat{\mathbf n}\times\mathbf W)\cdot(\hat{\mathbf n}\times\mathbf E),dS.\quad\text{[source boundary definition]}
$$

A radiation boundary approximates infinity with a Robin-type outgoing condition. It is an approximation to be tested, not an exact transparent boundary at every angle.

## 4. Edge elements rather than ordinary nodal fields

Ordinary nodal vector interpolation can enforce inappropriate continuity across material interfaces and permit spurious modes. Nédélec edge elements instead preserve tangential continuity while allowing the normal field behavior required by the material interface.

## 5. Assemble the sparse system

$$
([K]-k_0^2[M]+ik_0[B])\{e\}=\{f\}.
$$

Stiffness, mass and boundary matrices can be large but sparse because local basis functions overlap only nearby elements. The normalization of the boundary matrix determines its displayed prefactor. The source illustrates cavity eigenfrequencies and graphene impedance boundaries, and uses “a thousand times faster” as an enthusiastic example of avoiding a very fine thin-layer mesh.

:::{admonition} Scientific clarification — separate from the source
:class: note
Edge elements help control spurious modes but do not eliminate every nullspace or modeling error automatically. Thin-sheet replacement needs a valid constitutive model; speedup depends on mesh, solver and accuracy. No commercial FEM run is claimed here.
:::

:::{admonition} Worked problem
:class: tip
A cell is periodic in $x,y$ and contains an inhomogeneous dielectric, a thin conducting layer modeled on $S_{\rm IBC}$ by $Z_s$, and a first-order radiation boundary above. Assume scalar $\epsilon_r,\mu_r$ and known $\mathbf J_{\rm imp}$.

1. Derive the electric weak form with impedance and radiation terms.
2. Expand the field in Nédélec edge functions and give volume/boundary matrix entries.
3. Explain why edge elements are suitable.

```{dropdown} Show the complete worked answer

The source starts with the governing equation, tests with the conjugate field, and writes

$$
\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E=-i\omega\mu_0\mathbf J_{\rm imp}.
$$

$$
\int_V\mu_r^{-1}(\nabla\times\mathbf W^*)\cdot(\nabla\times\mathbf E),dV-k_0^2\int_V\epsilon_r\mathbf W^*\cdot\mathbf E,dV+i\omega\mu_0\int_{\partial V}\mathbf W^*\cdot(\hat{\mathbf n}\times\mathbf H),dS=-i\omega\mu_0\int_V\mathbf W^*\cdot\mathbf J_{\rm imp},dV.\quad\text{[printed]}
$$

Keep the source’s symbolic boundary definitions for this transcription; apply the correction above when implementing an outward-normal model:

$$
\hat{\mathbf n}\times\mathbf H=Y_s\mathbf E_t,\quad Y_s=Z_s^{-1},\qquad\hat{\mathbf n}\times\mathbf H\approx Y_{\rm rad}\mathbf E_t+\mathbf g_{\rm inc}.
$$

The unknown-field part enters the boundary matrix; the known incident term enters the right-hand side. An internal sheet requires fields on both sides and a magnetic-field jump, rather than a one-sided boundary imposed without change.

$$
\mathbf E_h(\mathbf r)=\sum_{j=1}^{N_e}e_j\mathbf N_j(\mathbf r),\qquad\mathbf W=\mathbf N_i.
$$

$$
[K-k_0^2M+i\omega\mu_0(B_{\rm IBC}+B_{\rm rad})]\mathbf e=\mathbf f.\quad\text{[source symbolic definitions]}
$$

$$
K_{ij}=\int_V\mu_r^{-1}(\nabla\times\mathbf N_i^*)\cdot(\nabla\times\mathbf N_j),dV,\qquad M_{ij}=\int_V\epsilon_r\mathbf N_i^*\cdot\mathbf N_j,dV.
$$

$$
(B_{\rm IBC})_{ij}=\int_{S_{\rm IBC}}Y_s\mathbf N_{i,t}^*\cdot\mathbf N_{j,t},dS,\qquad(B_{\rm rad})_{ij}=\int_{S_{\rm rad}}Y_{\rm rad}\mathbf N_{i,t}^*\cdot\mathbf N_{j,t},dS.
$$

$$
f_i=-i\omega\mu_0\left[\int_V\mathbf N_i^*\cdot\mathbf J_{\rm imp},dV+\int_{S_{\rm rad}}\mathbf N_{i,t}^*\cdot\mathbf g_{\rm inc},dS\right].\quad\text{[source symbolic definitions]}
$$

Link paired edge degrees of freedom by the Floquet phase, including edge orientations. Periodicity is not merely another independent boundary matrix. Tangential electric continuity is physical at an ordinary material interface, while the normal electric component need not be continuous. Edge functions accommodate precisely that distinction and help control spurious wave modes.

The challenge is combining integration-by-parts signs, the correct thin-layer model and Floquet constraints consistently.

```
:::
