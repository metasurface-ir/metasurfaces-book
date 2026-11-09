---
title: "Build a realizable phase library"
---

# Build a realizable phase library


The original Chapter 3 library fixes $h=0.60\,\mu\mathrm m$ and spans about $132^\circ$ over widths $0.08$–$0.57\,\mu\mathrm m$. It cannot represent a complete ramp accurately. We keep that library intact and create a new Chapter 5 dataset.

The notebook screens five declared common heights, from 0.60 to $1.80\,\mu\mathrm m$, over the same width domain. The coarse phase span first exceeds a full cycle at $h=1.80\,\mu\mathrm m$. At that height, it computes 161 widths and checks each at $M=24$ versus $32$. A continuous unwrapped span exceeding $360^\circ$ does not by itself guarantee complete usable coverage after applying a transmission threshold.

For each desired sample phase $\phi_j$, retain accepted rows with $T_j\geq0.8$ and minimize circular error:

$$
\Delta\phi_j=\arg\left[t_j e^{-i(\phi_j+\phi_0)}\right].
$$

The global offset $\phi_0$ is free for the ideal beam direction but changes the selected geometries. We search 361 fixed offsets, minimizing mean squared phase error using **unit-cell data only**. The expanded library matches all six sample phases within $1^\circ$ in the saved run. The supercell results are evaluated afterward; they are not used to select the offset or height.

This is a small, transparent discrete synthesis procedure. It is separate from gradient-based geometry optimization, generative design, or surrogate-assisted search. The exported records preserve both successful and limited-library designs.

