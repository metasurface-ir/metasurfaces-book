---
title: "Validate synthesis at more than one level"
---

# Validate synthesis at more than one level


The final four supercells are compared at $M=144$ and $192$, corresponding to 289 and 385 harmonics. Every reported open-order power and meaningful complex transmission coefficient is checked. The largest saved power change is below $2.4\times10^{-6}$ and the largest open transmitted-amplitude change below $1.4\times10^{-5}$. All-channel power balance is checked separately.

Increasing the number of cells while retaining the same integer $M$ reduces the represented physical Fourier bandwidth. For identical-cell embedding, the audit scales the supercell truncation with the number of primitive cells, compares with the primitive calculation, and verifies the forbidden supercell amplitudes. A mirror-reversed sequence must exchange positive and negative order powers under this normal-incidence, mirror-related geometry.

Three supercells are also compared at matching $M=48$ with the separately developed grcwa implementation. Its cell-averaged raster is refined from 512 to 4096 samples. The fine-raster order-power and zeroth-order complex-transmission differences are below $4\times10^{-6}$ in the saved audit. Both implementations use RCWA; FEM/FDTD and experiment remain distinct future comparisons.

