---
title: "4.2 Periodic electromagnetic structures and the unit cell"
---

# 4.2 Periodic electromagnetic structures and the unit cell

In metasurface design, we almost always encounter some form of spatial periodicity. A unit cell repeats along one or two axes in the plane and forms a regular array.

If repetition occurs in only one direction, we call the structure one-dimensionally periodic. If it occurs along two in-plane directions, we call it two-dimensionally periodic. For example, a cell repeated with period $p_x$ along $x$ and period $p_y$ along $y$ forms a two-dimensional metasurface array.

The unit cell plays exactly the role of a basic building block, and the entire structure is assembled from its repeated copies. Why does this matter? If the structure is infinitely periodic, we do not need to simulate the whole large array! Mathematics lets us obtain the field behavior throughout an infinite city by looking at just one house. This is where Mr. Floquet enters the story.

```{figure} ../assets/chapter-04/period-and-phase.png
:alt: Original course calculation: geometry and allowed channels, not a prediction of grating efficiency.

Original course calculation: geometry and allowed channels, not a prediction of grating efficiency.
```
