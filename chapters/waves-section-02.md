---
title: "2.2 Sources and field lines in unit-cell design"
short_title: "2.2 Sources and field lines in unit-cell design"
---

(ch02-source-02)=
# 2.2 Sources and field lines in unit-cell design

To understand metasurfaces physically and see how they manipulate waves, we need a clear picture of sources and the behavior of electric and magnetic field lines.

According to **electric Gauss law**, the divergence of electric flux density is directly related to electric charge density:

$$
\nabla\cdot\mathbf D=\rho.
$$

Or in integral form:

$$
\oiint_S\mathbf D\cdot d\mathbf s=\iiint_V\rho\,dV.
$$

The net flux through any closed surface equals the electric charge enclosed in its volume. Therefore:

- Positive charges act as **sources of electric field**.
- Negative charges act as **sinks of electric field**.
- In simple terms, electric field lines start on positive charges and end on negative charges.

By contrast, **magnetic Gauss law** states:

$$
\nabla\cdot\mathbf B=0.
$$

Or in integral form:

$$
\oiint_S\mathbf B\cdot d\mathbf s=0.
$$

This relation tells us that the net magnetic flux through any closed surface is always zero. Consequently:

- Unlike electric field lines, magnetic field lines have no starting or ending point and form closed loops.
- This expresses the absence of **magnetic monopoles** in classical physics: there is no isolated magnetic pole acting alone as a source or sink of magnetic field.

### Sources and dipoles in metasurface unit-cell engineering

This fundamental difference between electric and magnetic fields is a cornerstone of metasurface analysis and design:

**1. Electric response: an effective electric dipole.** When an incident electromagnetic wave reaches a unit cell such as a metal patch or narrow strip, the metal's free charges move, forming oppositely signed surface-charge distributions at the element's ends. This separation acts like an effective electric dipole, whose moment is defined by:

$$
\mathbf p=\iiint_V\mathbf r\,\rho(\mathbf r)\,dV.
$$

For a thin planar structure, the distribution is described by a surface charge, $\rho_s$, on the metal or material interface.

**2. Magnetic response: an effective magnetic dipole.** Time-varying induced currents flowing along curved or loop-shaped metal paths, such as an SRR, produce current loops that behave like effective magnetic dipoles. The magnetic dipole moment of the current distribution is calculated as:

$$
\mathbf m=\frac12\iiint_V\mathbf r\times\mathbf J(\mathbf r)\,dV.
$$

For a simple current loop with current $I$ and vector area $\mathbf S$, this reduces to:

$$
\mathbf m=I\mathbf S.
$$

The area vector's direction follows the right-hand rule.

### The unit cell's physical operation, gathered together

In metasurfaces, we view each cell as an element combining induced electric and magnetic dipoles:

- **Charge distributions** determine electric response and polarization.
- **Circulating and loop currents** produce artificial magnetic response.

By changing geometry—patch dimensions, gap widths, dielectric-substrate thickness, element rotation and period—we can adjust these dipoles' amplitudes and phases. This precise local control lets us redesign a wavefront, control reflection and transmission, change polarization, or steer and focus a beam at a desired angle.

