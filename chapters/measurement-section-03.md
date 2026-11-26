# 9.3 Packaging, bias isolation and integration

Based on the instructor booklet, pages 254–260.

Model a mounted PIN with its series resistance, lead inductance and off-state capacitance. A surface-mount package, bare die or flip-chip attachment has different RF parasitics and assembly constraints. Route bias through structures that limit RF leakage. A shorted quarter-wave branch transforms to a high input impedance at the design frequency. Verify bias isolation across the band with the actual stack, return currents and control transitions. Shift-register loading and latching must match the array update requirement.

$$
Z_{\rm on}\simeq R_s+i\omega L_s,\quad Z_{\rm off}\simeq i\omega L_s+\frac1{i\omega C_{\rm off}},\quad Z_{\rm in}=iZ_0\tan(\beta\ell).
$$

## Worked exercise from the reading

At 28 GHz, a packaged diode has $R_s=2\,\Omega$ and $L_s=0.30\,\mathrm{nH}$. Calculate its on-state impedance and explain what happens as a shorted bias branch moves off its quarter-wave frequency.

```{dropdown} Show the worked answer
:class: solution

$\omega L_s=2\pi(28\times10^9)(0.30\times10^{-9})=52.8\,\Omega$, so $Z_{\rm on}\simeq2+i52.8\,\Omega$. Near the quarter-wave condition, the magnitude of the shorted branch impedance declines away from the design frequency. Actual loss further limits the peak.
```

[Computational reading](measurement-computational.md) · [Lab](../labs/09-measurement-lab.md)
