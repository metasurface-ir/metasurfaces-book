---
title: English–Persian electromagnetic glossary
short_title: Bilingual glossary
---

# English–Persian electromagnetic glossary

These working equivalents keep the two editions consistent. They are teaching choices for instructor review; use the English term alongside a Persian term when ambiguity matters. Symbols and code identifiers are shared across editions.

(glossary-core)=
## Core terms

| English | فارسی | Meaning in this book |
| --- | --- | --- |
| Metasurface | فراسطح | A structured surface designed to transform electromagnetic waves |
| Phasor | فازور | Complex peak amplitude with an explicit time convention |
| Wave impedance | امپدانس موج | Specified electric-to-magnetic field ratio |
| Admittance | ادمیتانس | The corresponding magnetic-to-electric response ratio |
| Tangential | مماسی | Along the interface |
| Normal | عمود بر سطح | Along the stated surface normal |
| Polarization | قطبش | The electric-field trajectory at a fixed point |
| Jones vector | بردار جونز | Coherent complex transverse electric components |
| Linear / circular / elliptical | خطی / دایروی / بیضوی | Polarization trajectories under a stated convention |
| Analyzer | تحلیل‌گر قطبش | Projects the field onto its transmission axis |
| Retarder | تأخیرانداز | Introduces a relative component phase |
| Incident / reflected / transmitted | فرودی / بازتابی / عبوری | Incoming and outgoing waves at the defined interface |
| Reflectance / transmittance / absorptance | کسر توان بازتابی / عبوری / جذب‌شده | Normalized powers R, T, A, distinct from field coefficients |
| Evanescent | اوانسنت / میرا | A field decaying in the specified direction |
| Total internal reflection | بازتاب کلی داخلی | Unit reflected power above the lossless high-to-low critical angle |
| Cutoff | آستانهٔ قطع | The longitudinal propagation/decay threshold |
| Reference plane | صفحهٔ مرجع | Plane where a complex amplitude is defined |
| Deembedding | حذف اثر مسیر معلوم | Removes known propagation/fixture contributions |
| Power normalization | بهنجارسازی توان | Scales amplitudes so squared norms represent port power |
| Scattering matrix | ماتریس پراکندگی | Maps specified incoming channels to outgoing channels |
| Reciprocity | تقابل | Source/receiver interchange relation under stated port conventions |
| Passivity | غیرفعال بودن | No generation of net energy by the system |
| Conductance / susceptance | رسانایی / سوسپتانس | Real / imaginary parts of admittance |
| Sheet admittance | ادمیتانس ورقه | Surface current per tangential electric field, in siemens |
| Shunt | شنت | A parallel branch in the equivalent circuit |
| Coherence | همدوسی | Stable phase relations supporting relevant interference terms |
| Coherent perfect absorption | جذب کامل همدوس | Absence of outgoing power for a specified coherent input |
| Unit cell | سلول واحد | Repeated geometry that defines a periodic structure |
| Full-wave simulation | شبیه‌سازی تمام‌موج | A Maxwell solve for the specified geometry and model |
| Source / data / validation | منبع / داده / راستی‌آزمایی | Code or text, recorded results, and evidence supporting a claim |
| FDFD | تفاضل محدود حوزهٔ فرکانس | Spatially discretized frequency-domain boundary-value method |
| Equation residual | باقیماندهٔ معادله | How closely the computed vector solves the assembled equations |
| Model discrepancy | اختلاف مدل | Difference due to the physical approximation, separate from numerical refinement |

Quantitative figure keys: **Incidence angle** = زاویهٔ تابش; **Vacuum wavelength** = طول موج خلأ; **Power fraction** = کسر توان; **Relative phase** = فاز نسبی; **Bare interface** = مرز بدون پوشش; **Quarter-wave film** = لایهٔ ربع‌موج. English plot/table labels are retained with shared numerical outputs; Persian captions and this key explain them.


(glossary-advanced)=
## Periodic models, applications, and learning

| English | فارسی | Meaning in this book |
| --- | --- | --- |
| Bloch phase | فاز بلوخ | Phase gained under translation by a lattice vector |
| Floquet order | مرتبهٔ فلوکه | A spatial harmonic indexed by an integer and a stated exterior medium |
| Reciprocal lattice | شبکهٔ متقابل | Wavevector lattice used to enumerate periodic diffraction channels |
| Open / grazing / closed channel | کانال باز / مماسی / بسته | Propagating, cutoff, or evanescent in the declared medium |
| RCWA | تحلیل دقیق موج کوپل‌شده | Fourier-harmonic solution of a periodic Maxwell model; convergence must be checked |
| Harmonic truncation | قطع هارمونیک‌ها | Finite retained Fourier basis, a numerical control rather than a device parameter |
| Supercell | ابرسلول | A larger repeated sequence containing several local motifs |
| Local periodic approximation | تقریب تناوب محلی | Assigns isolated periodic-cell responses inside a nonuniform sequence |
| Target-order efficiency | بازده مرتبهٔ هدف | Power in the chosen order divided by incident power |
| Observable convergence | همگرایی کمیت مشاهده‌پذیر | Stability of the reported physical quantity under numerical refinement |
| Group delay | تأخیر گروهی | Frequency derivative of a valid unwrapped phase with the stated convention |
| Useful bandwidth | پهنای باند مفید | Connected band satisfying all declared performance constraints |
| Bias / varactor | بایاس / واراکتور | Control voltage / voltage-dependent capacitance element |
| Reachable state | حالت دست‌یافتنی | Complex response achievable within the specified control bounds |
| Codebook / quantization | کدنامه / کوانتش | Allowed discrete commands / mapping a continuous target to those commands |
| Settling time | زمان نشست | Time to enter a declared error band under the stated dynamics |
| Sideband | نوار جانبی | Frequency component offset by an integer modulation frequency |
| Channel gain | بهرهٔ کانال | Received-to-transmitted power ratio for the declared link model |
| Link budget | بودجهٔ پیوند | Consistent accounting of power, gains, losses, and noise |
| SNR / AWGN | نسبت سیگنال به نویز / نویز سفید گاوسی جمع‌شونده | Signal-to-noise ratio / the ideal noise model used in the rate formula |
| Pilot overhead / net rate | سربار پایلوت / نرخ خالص | Training cost / rate after the declared overhead |
| Calibration standard | استاندارد کالیبراسیون | Known response used to estimate a measurement error model |
| Systematic bias / random error | سوگیری نظام‌مند / خطای تصادفی | Persistent shift / variation under the stated sampling model |
| Covariance / correlation | کوواریانس / هم‌بستگی | Joint variation / its normalized measure; not statistical independence |
| Coverage region | ناحیهٔ پوشش | Region with a declared probability interpretation; not automatically a confidence region for a mean |
| Yield / acceptance fraction | بازده ساخت / سهم پذیرش | Fraction meeting a specification under a declared process distribution |
| Surrogate / forward model | مدل جانشین / مدل پیشرو | Approximation of a response map / prediction from specified inputs |
| Inverse design | طراحی وارون | Search for inputs achieving a target subject to bounds and checks |
| Training / validation / held-out test | آموزش / اعتبارسنجی / آزمون کنارگذاشته‌شده | Fit parameters / select choices / evaluate the frozen final choice |
| Data leakage | نشت داده | Test information entering fitting, selection, or preprocessing |
| Baseline / extrapolation | خط مبنا / برون‌یابی | Declared comparison method / prediction outside the sampled domain |
| Regularization / random seed | منظم‌سازی / بذر تصادفی | Constraint or penalty controlling a fit / reproducible pseudorandom initialization |

(glossary-notation)=
## Notation and conventions

The notebook is authoritative for local units and symbol definitions. The same letter can denote different quantities in different chapters. Phase is undefined at zero amplitude; unwrap only connected valid intervals.

| Symbol | Convention and units |
| --- | --- |
| $e^{-i\omega t}$; $e^{i\mathbf{k}\cdot\mathbf{r}}$ | Time/space signs used in the core examples; outgoing fields use the branch defined in each model |
| $f$, $\omega=2\pi f$, $\lambda_0$ | Frequency (Hz or explicitly GHz/THz), angular frequency (rad/s), vacuum wavelength (m or explicitly μm) |
| $\Lambda$, $m$, $k_{x,m}$ | Period (length), integer order, transverse wavenumber (inverse length); declare the incident and output media |
| $r$, $t$; $R$, $T$, $A$ | Complex field ratios versus power fractions. For unequal media or oblique incidence, T is not generally \|t\|² |
| $E$, $H$, $S_z$ | Peak phasors: V/m, A/m, W/m²; mean flux includes the factor 1/2. Tangential-E TM signs follow Chapter 2 |
| $z=0$, $z=h$ | TE ridge/film face references: reflection at entry and transmission at exit; deembed before complex comparisons |
| $M$, $\Delta x$, $N$ | Numerical harmonic half-count, mesh spacing, or sample/element count; meanings and units are local to the notebook |
| $Z_s$, $Y_s$, $\Gamma$ | Effective surface impedance (Ω), admittance (S), complex reflection. Circuit parameters are assigned unless extracted |
| $\lvert h\rvert^2$, dB, dBm | Channel power gain; 10 log10 of a power ratio; power relative to 1 mW. Do not confuse a normalized array metric with efficiency |
| $\sigma$, $\Sigma$, $\rho$ | Standard deviation (units of quantity), covariance (product of units), correlation (dimensionless); state the probability model |
