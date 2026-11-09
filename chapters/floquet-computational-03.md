---
title: "Translation symmetry and the Bloch phase"
---

(ch04-section-03)=
# Translation symmetry and the Bloch phase

For one incident plane wave, the driven scattering solution lies in the same Bloch sector as the excitation. A field component can be written

$$
E(x,z)=e^{-ik_{x,i}x}u(x,z),\qquad u(x+\Lambda,z)=u(x,z).
$$

It follows that

$$
E(x+\Lambda,z)=e^{-ik_{x,i}\Lambda}E(x,z).
$$

This is a phase relation between paired lateral boundaries. At normal incidence the multiplier is one. At oblique incidence, an ordinary zero-phase periodic condition generally represents a different excitation.

The boundary mapping direction matters. If a solver defines destination $x+\Lambda$ from source $x$, the multiplier under our convention is $e^{-ik_{x,i}\Lambda}$. Reversing the mapping requires its inverse. Some solvers use a different phasor or built-in phase convention. Verify the actual translated plane wave instead of copying a sign from a screenshot.

:::{dropdown} Derivation: why the driven field inherits the incident phase
Assume a linear, periodic Maxwell problem with one plane-wave excitation and a unique outgoing scattering solution. Translate both fields by $\Lambda$ and remove the known incident phase:

$$
\widetilde{\mathbf E}(x,z)=e^{+ik_{x,i}\Lambda}\mathbf E(x+\Lambda,z),\qquad
\widetilde{\mathbf H}(x,z)=e^{+ik_{x,i}\Lambda}\mathbf H(x+\Lambda,z).
$$

The translated material coefficients are unchanged. The translated incident wave acquires $e^{-ik_{x,i}\Lambda}$, which the prefactor cancels; the outgoing condition is unchanged too. Thus the tilded and original fields solve the same problem. Uniqueness makes them equal, yielding the Bloch relation. Multiplying the field by $e^{+ik_{x,i}x}$ then gives the periodic function $u$ used above.

This argument concerns a driven response, not an arbitrary sum of eigenmodes. At a lossless singularity with a nonunique homogeneous solution, specify the causal response by a limiting-absorption prescription; do not silently assume uniqueness. A finite array, a defect, or an excitation containing several tangential wavevectors also requires a different treatment or a superposition of Bloch sectors.
:::

### Bloch wavevectors differing by a reciprocal vector

Replacing $k_{x,i}$ by $k_{x,i}+\ell G$ leaves the translation multiplier unchanged because $e^{-i\ell G\Lambda}=1$. This is the origin of reciprocal-lattice equivalence. It relabels harmonics; it does not change their physical tangential wavevectors when the labels are shifted consistently. The incident wavevector remains fixed by the physical incidence condition.
