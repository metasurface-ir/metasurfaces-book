# 8.5 Space-time modulation in a communication link

Based on the instructor booklet, pages 223–229.

A traveling pump shifts the frequency and transverse momentum of each harmonic together. Program the complex coefficient of a selected sideband to encode symbols. Its phase can track pump phase in the first order. Finite switching rates, control skew, spurious sidebands and leakage into the receive band all affect system performance. A duplex link needs a budget for residual self-interference at the receiver.

$$
f_m^{\rm out}=f_0+m f_{\rm pump},\quad k_{x,m}=k_{x,0}+mK,\quad a_1=0.25e^{i\varphi_b}.
$$

```{figure} ../assets/chapter-08/space-time-sidebands.svg
:alt: Incident wave, mounted unit cell and outgoing sidebands

Original teaching schematic for Figure 8–5. Arrow directions and lengths are schematic.
```

## Worked exercise from the reading

For a normal 10 GHz input, use a 200 MHz pump and $K=0.70k_0$. Find the upper sideband angle and show the QPSK symbols available from four pump phases.

```{dropdown} Show the worked answer
:class: solution

The upper sideband is at 10.2 GHz, hence $\sin\theta=0.70/1.02$ and $\theta\simeq43.3^\circ$. Pump phases $0,\pi/2,\pi,3\pi/2$ yield $0.25\{1,i,-1,-i\}$. Their equal modeled magnitudes do not account for frequency-dependent hardware loss.
```

[Computational reading](communications-computational.md) · [Lab](../labs/08-communications-lab.md)
