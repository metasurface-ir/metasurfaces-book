# 9.3 Assembly and integration of reconfigurable elements

Instructor booklet, pages 254–260.

A programmable metasurface combines three parts. The RF layer contains patches, slots, and diodes. A continuous or slotted ground separates fields from the rear circuitry, while plated vias provide a reference path. Behind it, bias routing, current buffers, converters, and an FPGA turn commands into cell voltages and currents. The connection and return path can change the patch response.

## 9.3.1 PIN diodes and varactors

In digital coding, a PIN diode conducts under forward bias, for example $5$ to $15\,\mathrm{mA}$. Under reverse bias, for example $0$ to $-5\,\mathrm V$, junction capacitance and leakage matter. A two-state model is

$$
Z_{\rm ON}=R_s+i\omega L_s,\qquad
Z_{\rm OFF}=i\omega L_s+\frac{1}{i\omega C_t+1/R_p},\qquad
f_c=\frac1{2\pi R_s C_t}.
$$

Booklet example ranges are $R_s=0.8$ to $3\,\Omega$, $L_s=0.1$ to $0.5\,\mathrm{nH}$, and $C_t=0.02$ to $0.15\,\mathrm{pF}$. The quantity $f_c$ is a figure of merit. At millimeter wavelengths consider GaAs or another high-$f_c$ diode, then check the package and parasitics, which can erase state contrast even with a high figure of merit.

For continuous tuning use a **varactor** with reverse-bias magnitude $V_R$. Here $C_{j0}$ is zero-bias capacitance, $V_{\rm bi}$ the built-in potential, and $\gamma$ the junction parameter.

$$
C_v=\frac{C_{j0}}{(1+V_R/V_{\rm bi})^\gamma},\qquad Q_v=\frac1{\omega R_s C_v}.
$$

Series resistance can change with bias as well. Changes in resonance and varactor current lead to **phase–amplitude coupling**.

## 9.3.2 High-frequency packaging and attachment

| Method | Structure and limitation |
| --- | --- |
| SMT / reflow | DFN, QFN, 0402, or 0201 packages. Pads and solder paths can become part of the RF geometry. |
| Wire bonding | Bare die, with $15$ to $25\,\mu\mathrm m$ gold or aluminum wire. An example scale is $0.8\,\mathrm{nH/mm}$. Short, parallel, or ribbon bonds can reduce inductance. |
| Flip-chip | An inverted die with micro-bumps around $20$ to $50\,\mu\mathrm m$. Connection inductance can be around $0.05\,\mathrm{nH}$ in examples. Include the return path. |

## 9.3.3 RF and DC bias isolation

RF leakage into bias wiring steals aperture power, can make the wiring radiate, and can bring digital clock noise into the band. A $\lambda_g/4$ line terminated near an RF short presents a large impedance at the patch. A radial stub can provide a virtual RF ground while leaving the DC route available. Choose an RF choke using impedance and self-resonant-frequency data. A high-sheet-resistance line, for example Cr or nichrome, may suit a low-current bias. Check DC voltage drop and settling.

## 9.3.4 Digital control and FPGA drivers

A $32\times32$ panel would otherwise require one pin per $1024$ cells. A serial-in parallel-out (SIPO) shift register, such as a 74HC595 or a high-voltage HV507 driver, receives frames over an interface such as SPI. A common latch prevents intermediate states from reaching the panel. The stated clock rate does not account for settling, cell-to-cell skew, or driver limits. With half of one thousand $10\,\mathrm{mA}$ diodes on, current is about $5\,\mathrm A$. Design rail capacity, heat distribution, thermal vias, and heat sink together.

## Worked problem on integrating a 28 GHz panel

::::{admonition} Try it first
:class: book-exercise

A $32\times32$ panel at $28\,\mathrm{GHz}$ uses one PIN diode per cell for nearly $180^\circ$ phase difference. The diode has $R_s=2\,\Omega,C_t=0.10\,\mathrm{pF},I_f=10\,\mathrm{mA},V_f=0.9\,\mathrm V$ with negligible off leakage. Total connection inductances for SMT, wire bond, and flip-chip are $0.30,0.20,0.05\,\mathrm{nH}$. For the varactor version use $C_{j0}=0.40\,\mathrm{pF},V_{\rm bi}=0.80\,\mathrm V,\gamma=0.5$, and $2$ and $3\,\Omega$ at reverse biases $0$ and $12\,\mathrm V$. The bias line has $Z_0=60\,\Omega,\varepsilon_{\rm eff}=2.8$. A choke has SRF $18\,\mathrm{GHz}$ and a resistive path is $10\,\mathrm{k\Omega}$. Shift clock is $20\,\mathrm{MHz}$, deadline $10\,\mu\mathrm s$, latch and settle time $0.6\,\mu\mathrm s$, and rail $3.3\,\mathrm V$. Evaluate assembly, continuous tuning, bias, loading time, and heat.

```{dropdown} Show the full worked answer

### 1. Assembly screening

$$
f_c=1/(2\pi R_s C_t)\simeq796\,\mathrm{GHz},\qquad
1/(\omega C_t)\simeq56.84\,\Omega.
$$

| Attachment | $\omega L_s$ | $Z_{\rm ON}$ | $Z_{\rm OFF}$ |
| --- | --- | --- | --- |
| SMT | $52.78\,\Omega$ | $2+i52.78\,\Omega$ | $-i4.06\,\Omega$ |
| Wire bond | $35.19\,\Omega$ | $2+i35.19\,\Omega$ | $-i21.65\,\Omega$ |
| Flip-chip | $8.80\,\Omega$ | $2+i8.80\,\Omega$ | $-i48.04\,\Omega$ |

The printed problem omits numeric screening limits. To reproduce its decision, use **illustrative limits** $\lvert Z_{\rm ON}\rvert\le10\,\Omega$ and $\lvert Z_{\rm OFF}\rvert\ge40\,\Omega$. Flip-chip passes with $9.02$ and $48.04\,\Omega$. For SMT, the connection and $C_t$ resonate near $1/(2\pi\sqrt{L_s C_t})=29.1\,\mathrm{GHz}$, making the off impedance small in-band. The final test is $\angle(\Gamma_{\rm ON}/\Gamma_{\rm OFF})$ near $180^\circ$, with adequate amplitudes in both states and a common phase reference. Include pads, solder, vias, and patch.

### 2. Varactor at two biases

$$
C_v(0)=0.40\,\mathrm{pF},\qquad C_v(12)=0.40/\sqrt{1+12/0.80}=0.10\,\mathrm{pF}.
$$

$Q_v$ rises from $7.1$ to $18.9$ because the capacitance decrease outweighs the resistance increase. This is the series-varactor branch quality factor. For the cell, tabulate $V_R$, $\angle\Gamma$, and $\lvert\Gamma\rvert$. For similar phases choose the better amplitude. Near zero bias also test for unintended conduction under RF swing.

### 3. Bias network

$$
\lambda_g=c/(f\sqrt{\varepsilon_{\rm eff}})\simeq6.40\,\mathrm{mm},\qquad
\ell=\lambda_g/4\simeq1.60\,\mathrm{mm},\qquad Z_{\rm in}=iZ_0\tan(\beta\ell).
$$

An RF short at the far end looks open from the patch at design frequency. A radial stub approximates that condition. At $5\%$ higher frequency, neglecting dispersion, $\lvert Z_{\rm in}\rvert\simeq60\lvert\tan(1.05\pi/2)\rvert\simeq762\,\Omega$. This is not a measured isolation in decibels. A choke with $18\,\mathrm{GHz}$ SRF requires in-band data at $28\,\mathrm{GHz}$. The $10\,\mathrm{k\Omega}$ path drops $100\,\mathrm V$ for an on-state PIN, but only $1\,\mathrm{mV}$ for an assumed $0.1\,\mu\mathrm A$ varactor leakage. Check settling.

### 4. Frame loading and heat

$$
t_1=1024/(20\,\mathrm{MHz})+0.6\,\mu\mathrm s=51.8\,\mu\mathrm s,\qquad
t_8=128/(20\,\mathrm{MHz})+0.6\,\mu\mathrm s=7.0\,\mu\mathrm s.
$$

Eight parallel chains of sixteen eight-bit registers meet the timing for a **ready frame**. A latch keeps intermediate patterns off the panel. Computation time and driver skew are separate, and current buffers supply the diodes.

$$
I_{\rm rail}=512(10\,\mathrm{mA})=5.12\,\mathrm A,\qquad
P_{\rm rail}=16.90\,\mathrm W,\quad P_{\rm PIN}=4.61\,\mathrm W,\quad P_{\rm series}=12.29\,\mathrm W.
$$

Most heat is in linear drivers or current limiters. With all cells on, the totals are $10.24\,\mathrm A$ and about $33.8\,\mathrm W$. Test supply, bypassing, and heat sink at the worst allowed pattern and check transient rail droop at the latch. Separate three acceptance tests: mounted-cell response, RF leakage to bias, and supply and temperature stability.
```
::::

[Computational reading](measurement-computational.md) · [Lab](../labs/09-measurement-lab.md)
