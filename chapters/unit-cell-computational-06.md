---
title: "Extract phase at stated reference planes"
---

# Extract phase at stated reference planes

A phase is meaningful relative to an excitation and a plane. Suppose an incident monitor is $L_i$ above the ridge and an output monitor $L_t$ below it. If both measured ratios use incident $E_y$ at $z=-L_i$, then

$$
r_{\rm mon}=r\,e^{-2ik_0q_iL_i},\qquad
t_{\rm mon}=t\,e^{-ik_0(q_iL_i+q_tL_t)}.
$$

Removing these homogeneous propagation phases returns the two face-referenced coefficients. The notebook tests this algebra with synthesized monitor offsets; the RCWA calculation itself matches directly at the two interfaces.

The wrapped phase $\arg t$ jumps at $\pm180^\circ$. For a smooth parameter sweep, phase unwrapping can reveal the continuous path. The path can be misleading near $|t|=0$, where phase is poorly defined and numerical noise becomes dominant. Keep amplitude beside every phase plot and use a stated amplitude/power threshold for design.

For comparing a response with a desired phase, use the circular difference

In the notebook lookup, the requested target is phase lag $\Phi_\star$, so the reference coefficient is $e^{-i\Phi_\star}$. The stored phase column is the signed argument $\arg t$; compare it with $-\Phi_\star$, modulo a full turn.

$$
\Delta\phi=\arg\left[t\,e^{+i\Phi_\star}\right].
$$

The direct subtraction $179^\circ-(-179^\circ)$ gives $358^\circ$, while their circular separation is $2^\circ$. For a change in height, even a bare homogeneous propagation path changes phase. Define a common physical comparison plane or a clearly stated background reference before attributing that change entirely to the ridge response.
