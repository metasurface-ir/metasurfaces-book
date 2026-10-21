# Planned computational investigations

The identifiers below preserve the existing course handoff, with a new AI investigation for Chapter 10. The AI pilot includes two executed analytical notebooks, worked exercises, and four detailed lab stages. The other investigations remain proposed. Chapters organize subject matter, while labs organize computational activities.

| Topic ID | Proposed investigation | Related chapter(s) |
| --- | --- | --- |
| ms-01-waves-interfaces | Fresnel amplitudes versus power; a thin-film baseline | 2 |
| ms-02-scattering | Parameterized resonance response and its limits | 1, 2 |
| ms-03-sheet-response | Sheet-response retrieval and consistency | 2, 5 |
| ms-04-floquet-orders | Open diffraction channels and cutoff maps | 4 |
| ms-05-beam-steering | Ideal versus sampled phase profiles | 5 |
| ms-06-polarization | Jones matrices, rotated elements, geometric phase | 2, 5 |
| ms-07-unit-cell | A converged unit-cell response library | 3, 6 |
| ms-08-metalenses | Finite-aperture propagation and focal metrics | 5 |
| ms-09-dispersion | Spectral sweeps and bandwidth metrics | 2, 5 |
| ms-10-coupling | Independent-cell versus supercell predictions | 3, 6 |
| ms-11-inverse-design | Bounded optimization with independent checks | 5, 6, 10 |
| ms-12-research-project | Reproducible project and evidence report | 7, 8, 9, 10 |
| ms-13-ai-metasurfaces | [Learn, design, and verify: analytical starter and full-wave lab outlines](13-ai-metasurfaces.md) | 10 |

## Next investigation after Chapter 10

**Floquet orders: Which beams can leave a metasurface?** Begin with an analytical notebook that maps allowed orders versus period, wavelength, incidence angle, and refractive index. Follow it later with an independently validated full-wave comparison. An allowed order does not determine its power or efficiency.

This first-lab suggestion follows the existing companion lesson draft. We can change it when the instructor supplies the final topic list.

### First-lab implementation brief

Use the handoff conventions: time dependence exp(-i omega t), spatial dependence exp(i k dot r), periodicity along x, and ky = 0. The introductory model assumes homogeneous, isotropic, lossless media with positive refractive indices.

For vacuum wavelength lambda0 and period Lambda, use k0 = 2 pi / lambda0 and kx,m = ni k0 sin(theta_i) + 2 pi m / Lambda. Classify an order as open when abs(kx,m) < no k0, at grazing cutoff when equal, and closed when greater. Use a documented numerical tolerance around cutoff.

The first analytical check will use normal incidence, Lambda = 3 micrometers, lambda0 = 1.55 micrometers, and output index no = 1. The expected open orders are -1, 0, and +1, with first-order angles approximately +/-31.1 degrees. This checks channel geometry only; it provides no simulated efficiency.

Expose wavelength, period, incidence angle, refractive indices, order range, and cutoff tolerance. Include sweeps and analytic checks before adding any full-wave comparison.
