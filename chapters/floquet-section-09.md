---
title: "4.9 Periodic boundaries and Floquet ports in simulation"
---

# 4.9 Periodic boundaries and Floquet ports in simulation

Now we understand why Chapter 3 used periodic boundaries and Floquet ports.

Periodic boundaries—the room-of-mirrors metaphor—in CST or HFSS numerically impose the phase relation $E(x+p)=E(x)e^{-ik_xp}$ on the unit-cell walls. A Floquet port is a window that can inject or receive energy separately in the Floquet modes $(m,n)$ and provide the amplitude and phase plots extracted in the previous chapter.

:::{note} Supplementary clarification
A solver may use different port, angle and phase-map definitions. Check a translated plane wave and the power normalization before comparing complex coefficients. Evanescent modes may be necessary for boundary matching and convergence even when only open orders carry far-field normal power.
:::
