# 8.2 Programmable propagation and near-field focusing

Based on the instructor booklet, pages 204–211.

A reflecting panel can create a virtual line of sight around an obstruction, but it intercepts finite power. Each coefficient includes two distances, angle and polarization factors, and a measured complex state response. Equalize total path phases for a near-field focus. Two users along one ray may see different spherical wavefront curvatures, but measure both focal responses before claiming range discrimination. Train the channel using independent patterns and count pilot overhead. Judge performance with the direct field included coherently.

$$
h=\sum_n B_n\Gamma_n e^{-ik_0(r_{tn}+r_{nr})}+h_d,\quad \phi_n=k_0(r_{tn}+r_{nr})+\phi_0.
$$

## Worked exercise from the reading

::::{admonition} Try it first
:class: book-exercise

In the source's training comparison, 16 grouped patterns take a total of 128 µs. What fraction of a 2 ms coherence interval is lost? What do grouped pilots identify?

:::{dropdown} Show the worked answer

The fraction is $128/2000=6.4\%$. Grouped observations identify group responses when the pattern matrix has sufficient rank. Individual coefficients inside a group remain unresolved.
:::
::::

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
