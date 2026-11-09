---
title: "4.3 Floquet theorem: the language of periodicity"
---

# 4.3 Floquet theorem: the language of periodicity

Floquet’s theorem is one of the most fundamental tools for analyzing periodic structures. It states that, in a periodic medium or structure, the electromagnetic fields in neighboring cells differ only by a specified phase factor.

In other words, the shape of the field repeats identically in different cells, but its phase changes from one cell to the next.

Let us use a metaphor. Imagine walking down a street lined with exactly identical trees, planted at exactly equal spacings. The scene—the field-amplitude pattern—you see beside the first tree is the same as the scene beside the tenth! What has changed is your spatial position, representing phase, along the street.

### Mathematical statement of Floquet’s theorem

Suppose a structure repeats along $x$ with period $p$. If its electric field at a point is $E(x)$, Floquet’s theorem gives the field in the next cell, at $x+p$, as follows:

$$
E(x+p)=E(x)e^{-ik_xp}.
$$

Here:

- $p$ is the structural period along $x$.
- $k_x$ is the tangential wavevector component along $x$.
- $e^{-ik_xp}$ is the phase factor between neighboring cells.

This relation shouts: “Move from one cell to the next, and the overall field pattern repeats, while its phase turns by an amount $k_xp$!”

If the structure is periodic along both $x$ and $y$, as in a two-dimensional metasurface, the more general relation is:

$$
E(x+p_x,y+p_y)=E(x,y)e^{-i(k_xp_x+k_yp_y)}.
$$

Alternatively, write the translations along each direction separately:

$$
E(x+p_x,y)=E(x,y)e^{-ik_xp_x}.
$$

$$
E(x,y+p_y)=E(x,y)e^{-ik_yp_y}.
$$

In very simple language, Floquet’s theorem tells us: “If the structure repeats, repeat the field too—just shift its phase!”

:::{note} Supplementary clarification
This relation describes the response to one Bloch excitation in a linear periodic structure. The translation proof and its uniqueness assumptions remain in the computational pages. The exponential gives a signed phase change of $-k_xp$; the positive quantity $k_xp$ is its phase lag. The source uses $j$ for the same imaginary unit as $i$.
:::
