---
title: "A phase gradient does not set efficiency"
---

# A phase gradient does not set efficiency


For one TE plane wave, normal power flux is proportional to $n\cos\theta\,|E_y|^2$. If all incident power were transmitted into one desired wave with no reflection or other channels, its electric-field ratio would have to satisfy

$$
\left|\frac{E_t}{E_i}\right|=
\sqrt{\frac{n_i\cos\theta_i}{n_t\cos\theta_t}}.
$$

A unit-amplitude phase-only field does not generally have that flux. Complete passive scattering must account for impedances, all outgoing channels, and the local/collective response. The [work on perfect reflection/refraction by Asadchy and colleagues](https://arxiv.org/abs/1605.02044) develops the physical constraints beyond prescribing a phase gradient.

One synthesis route starts directly from the boundary fields. For a surface normal $\hat{\mathbf n}$ directed from region 1 to region 2,

$$
\hat{\mathbf n}\times(\mathbf H_2-\mathbf H_1)=\mathbf J_s,\qquad
\hat{\mathbf n}\times(\mathbf E_2-\mathbf E_1)=-\mathbf M_s.
$$

These equivalent electric and magnetic surface currents describe the field jumps. Turning them into a realizable sheet requires a constitutive response consistent with passivity, reciprocity where applicable, and sufficient information about both illuminations/polarizations. This chapter's implemented route instead selects dielectric geometries from a library and verifies their full scattering; it does not retrieve a general bianisotropic susceptibility tensor.

