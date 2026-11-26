# 9.2 Fabrication and deposition

Based on the instructor booklet, pages 248–254.

Printed boards are practical for microwave patterns and multilayer routing, but registration, roughness and minimum gaps matter. Optical lithography uses a mask and transfer process. Electron-beam writing achieves small features at low throughput, while nanoimprint trades master fabrication for replication. Deposition and etching set material, thickness, sidewalls and roughness. Measure the fabricated geometry and propagate its uncertainty through the response.

$$
f_0=\frac1{2\pi\sqrt{LC}},\qquad C\propto g^{-1}\implies f_0/f_{00}\simeq\sqrt{g/g_0}.
$$

## Worked exercise from the reading

For $g_0=3.0\,\mu\mathrm m$, use the source's geometric model to find the allowable gap for a resonance shift within ±3%. Does a ±0.5 µm process meet it?

```{dropdown} Show the worked answer
:class: solution

Squaring the frequency limits gives $3(0.97)^2\le g\le3(1.03)^2$, or approximately 2.823–3.183 µm. A symmetric tolerance must be about ±0.177 µm or tighter. The ±0.5 µm process fails this screening model.
```

[Computational reading](measurement-computational.md) · [Lab](../labs/09-measurement-lab.md)
