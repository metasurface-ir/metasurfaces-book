---
title: "5.1 From analysis to synthesis"
---

# 5.1 From analysis to synthesis

Hello everyone! So far, we have mostly played the role of an analyst. Someone gave us a structure, unit cell or layer and said: “Work out what this does to an electromagnetic wave. How much does it reflect, and how much does it transmit?” We call this the forward problem, or analysis.

But real engineering reverses the story—and makes it more interesting! A client or problem statement does not normally say “I have this cell.” It says: “I have a normally incident plane wave, and I want this surface to deflect it through 45 degrees,” or “I want that plane wave focused ten centimeters away—a flat lens.”

What is our job now? We must work backward from that final wish and find the structure, dimensions and impedance distribution that could perform the trick. This reverse-engineering process is metasurface synthesis, or solving an inverse problem. To remember the difference, compare the two viewpoints:

| Viewpoint | Analysis / forward | Synthesis / inverse |
| --- | --- | --- |
| Starting point | Cell geometry and material are specified | Incident wave and desired output field |
| Goal | Scattered fields and S-parameters | Optimal cell shape, dimensions and layout |
| Mathematical difficulty | Well-defined, with a unique answer | Often nonunique or ill-posed |
| Tools | Full-wave simulators such as CST/HFSS | Analytical formulation, phase optics and optimization |

### Synthesis roadmap: three steps to a metasurface

When synthesizing a metasurface from scratch, follow these three steps in order:

1. **Wave transformation:** calculate the incident and desired outgoing phases and amplitudes on the surface, and their differences.
2. **Macroscopic response:** determine the local phase shift, transmission/reflection coefficient or surface impedance.
3. **Microscopic implementation:** consult the unit-cell library and place a cell with the required geometrical dimensions at each location.

$$
\text{wave requirements}\ \longrightarrow\ \text{surface response}\ \longrightarrow\ \text{physical implementation}.
$$


:::{admonition} Scientific clarification — separate from the primary reading
:class: note
A forward problem is unique only after geometry, material response, excitation, radiation conditions and a well-posed solution class have been specified. Resonant or exceptional cases need care. An inverse target can have many feasible solutions or none; the word “optimal” requires a stated objective and constraints.
:::
