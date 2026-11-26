# 8.6 Integrated sensing, localization and imaging

Based on the instructor booklet, pages 230–236.

A common waveform can carry data and probe the scene. Round-trip delay gives path length, while coherent element responses provide angle. A separable rectangular aperture has a Kronecker steering vector. In a coded imaging aperture, each mask gives a linear combination of scene cells. Check singular values or column coherence to see whether two candidate locations can be separated. A dynamic metasurface antenna can trade more masks for fewer RF chains.

$$
\tau=2L/c,\qquad \mathbf a=\mathbf a_y\otimes\mathbf a_x,\qquad \mathbf y=\mathbf A\mathbf x+\mathbf n.
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

In the booklet's local angular model the four response factors are $1+8\delta\theta,1-8\delta\theta,1+4\delta\phi,1-4\delta\phi$, all multiplied by the same unknown complex echo $\alpha$. How can a noiseless estimator eliminate $\alpha$?

:::{dropdown} Show the worked answer

Divide each pair difference by its sum. The two ratios are $8\delta\theta$ and $4\delta\phi$. The ratio is undefined at zero echo and becomes unstable at low SNR. The angular approximation is local.
:::
::::

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
