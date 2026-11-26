# 7.5 Time variation and frequency channels

Based on the instructor booklet, pages 190–195.

If a boundary coefficient changes during an RF cycle, the field and coefficient multiply in time and convolve in frequency. A traveling modulation also supplies tangential momentum. Compare the exchanged input and output modes with the pump unchanged when testing nonreciprocity. A conversion path alone establishes neither isolation over a band nor gain. Count pump power and other propagating modes.

$$
\Gamma(x,t)=\sum_m a_m e^{im(\Omega t-Kx)},\quad \omega_m=\omega_0+m\Omega,\quad k_{x,m}=k_{x,0}+mK.
$$

## Worked exercise from the reading

A 10 GHz input has $k_x=0.6k_0$. Use $f_m=100$ MHz and $K=0.6k_0$. Find the lower sideband direction and the transverse momentum of the opposite-frequency order under the same pump at normal incidence.

```{dropdown} Show the worked answer
:class: solution

For $m=-1$, the output is 9.9 GHz with $k_x=0$. Starting at 9.9 GHz and $k_x=0$, the $m=+1$ order at 10 GHz has $k_x=+0.6k_0$. The spatially reversed version of the original input would have $-0.6k_0$. A physical comparison also specifies polarization, normalization and leakage paths.
```

[Computational reading](active-computational.md) · [Lab](../labs/07-tunable-lab.md)
