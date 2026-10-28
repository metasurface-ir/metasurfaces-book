---
title: واژه‌نامهٔ انگلیسی و فارسی الکترومغناطیس
short_title: واژه‌نامهٔ دو‌زبانه
---

# واژه‌نامهٔ انگلیسی و فارسی الکترومغناطیس

این معادل‌های کاری برای یکدستی دو ویرایش پیشنهاد شده‌اند و برای بازبینی مدرس آماده‌اند. هرجا ابهام وجود دارد، اصطلاح انگلیسی را کنار فارسی بیاورید. نماد و نام متغیر و تابع در دو زبان مشترک است. تعریف تفصیلی فارسی واژه‌های فصل ۲ در [خودآزمایی](chapters/02-waves-review.md) آمده است؛ ستون سوم زیر، تعریف مرجع انگلیسی را برای مقایسه نگه می‌دارد.

(glossary-core)=
## اصطلاح‌های پایه

| English | فارسی | تعریف مرجع انگلیسی |
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
| FDFD | تفاضل محدود حوزهٔ فرکانس | حل مسئلهٔ مرزی حوزهٔ فرکانس با گسسته‌سازی مکانی |
| Equation residual | باقیماندهٔ معادله | میزان برآورده‌شدن معادلات مونتاژشده توسط بردار محاسبه‌شده |
| Model discrepancy | اختلاف مدل | اختلاف ناشی از تقریب فیزیکی، جدا از ریزسازی عددی |


کلید نمودارهای مشترک: **Incidence angle** یعنی زاویهٔ تابش؛ **Vacuum wavelength** طول موج خلأ؛ **Power fraction** کسر توان؛ **Relative phase** فاز نسبی؛ **Bare interface** مرز بدون پوشش؛ **Quarter-wave film** لایهٔ ربع‌موج؛ **Normal flux** شار عمود بر سطح؛ **Decay length** طول افت؛ و **Snapshot** نمای لحظه‌ای است. واحد um یا μm میکرومتر و deg درجه است. برچسب‌های انگلیسی نمودار و جدول عددی از خروجی مرجع مشترک نگه داشته شده‌اند؛ زیرنویس‌ها و متن آموزشی فارسی‌اند.


(glossary-advanced)=
## مدل تناوبی، کاربرد و یادگیری

| English | فارسی | معنا در این کتاب |
| --- | --- | --- |
| Bloch phase | فاز بلوخ | فاز کسب‌شده با انتقال به‌اندازهٔ بردار شبکه |
| Floquet order | مرتبهٔ فلوکه | هارمونیک فضایی با شاخص صحیح و محیط بیرونی مشخص |
| Reciprocal lattice | شبکهٔ متقابل | شبکهٔ بردار موج برای شمارش کانال‌های پراش تناوبی |
| Open / grazing / closed channel | کانال باز / مماسی / بسته | منتشرشونده، در آستانه یا اوانسنت در محیط مشخص |
| RCWA | تحلیل دقیق موج کوپل‌شده | حل مدل تناوبی ماکسول با هارمونیک فوریه؛ همگرایی باید بررسی شود |
| Harmonic truncation | قطع هارمونیک‌ها | پایهٔ فوریهٔ متناهی؛ کنترل عددی و نه پارامتر قطعه |
| Supercell | ابرسلول | دنبالهٔ تکرارشوندهٔ بزرگ‌تر با چند نقش محلی |
| Local periodic approximation | تقریب تناوب محلی | پاسخ سلول تناوبی منفرد را در دنبالهٔ ناهمگن به‌کار می‌برد |
| Target-order efficiency | بازده مرتبهٔ هدف | توان مرتبهٔ انتخاب‌شده تقسیم بر توان فرودی |
| Observable convergence | همگرایی کمیت مشاهده‌پذیر | پایداری کمیت فیزیکی گزارش‌شده با پالایش عددی |
| Group delay | تأخیر گروهی | مشتق فرکانسی فاز گشودهٔ معتبر با قرارداد اعلام‌شده |
| Useful bandwidth | پهنای باند مفید | بازهٔ پیوستهٔ برآورده‌کنندهٔ همهٔ محدودیت‌های عملکرد اعلام‌شده |
| Bias / varactor | بایاس / واراکتور | ولتاژ کنترل / عنصر با ظرفیت وابسته به ولتاژ |
| Reachable state | حالت دست‌یافتنی | پاسخ مختلط قابل دستیابی در کران‌های کنترل مشخص |
| Codebook / quantization | کدنامه / کوانتش | فرمان‌های گسستهٔ مجاز / نگاشت هدف پیوسته به آن‌ها |
| Settling time | زمان نشست | زمان ورود به نوار خطای مشخص در دینامیک اعلام‌شده |
| Sideband | نوار جانبی | مولفهٔ فرکانسی با فاصلهٔ مضرب صحیح فرکانس مدولاسیون |
| Channel gain | بهرهٔ کانال | نسبت توان دریافتی به ارسالی در مدل پیوند اعلام‌شده |
| Link budget | بودجهٔ پیوند | حساب سازگار توان، بهره، افت و نویز |
| SNR / AWGN | نسبت سیگنال به نویز / نویز سفید گاوسی جمع‌شونده | نسبت سیگنال به نویز / مدل نویز ایده‌آل فرمول نرخ |
| Pilot overhead / net rate | سربار پایلوت / نرخ خالص | هزینهٔ آموزش / نرخ پس از سربار اعلام‌شده |
| Calibration standard | استاندارد کالیبراسیون | پاسخ معلوم برای برآورد مدل خطای اندازه‌گیری |
| Systematic bias / random error | سوگیری نظام‌مند / خطای تصادفی | جابه‌جایی پایدار / تغییر در مدل نمونه‌گیری مشخص |
| Covariance / correlation | کوواریانس / هم‌بستگی | تغییر مشترک / معیار بهنجارشدهٔ آن؛ نه استقلال آماری |
| Coverage region | ناحیهٔ پوشش | ناحیه با تفسیر احتمال مشخص؛ لزوماً ناحیهٔ اطمینان میانگین نیست |
| Yield / acceptance fraction | بازده ساخت / سهم پذیرش | سهم برآورده‌کنندهٔ مشخصات در توزیع فرایند اعلام‌شده |
| Surrogate / forward model | مدل جانشین / مدل پیشرو | تقریب نگاشت پاسخ / پیش‌بینی از ورودی مشخص |
| Inverse design | طراحی وارون | جست‌وجوی ورودی برای هدف با کران و کنترل |
| Training / validation / held-out test | آموزش / اعتبارسنجی / آزمون کنارگذاشته‌شده | برازش پارامتر / انتخاب تنظیم / ارزیابی انتخاب نهایی ثابت‌شده |
| Data leakage | نشت داده | ورود اطلاعات آزمون به برازش، انتخاب یا پیش‌پردازش |
| Baseline / extrapolation | خط مبنا / برون‌یابی | روش مقایسهٔ اعلام‌شده / پیش‌بینی بیرون دامنهٔ نمونه‌برداری |
| Regularization / random seed | منظم‌سازی / بذر تصادفی | قید یا جریمهٔ کنترل برازش / آغاز شبه‌تصادفی بازتولیدپذیر |

(glossary-notation)=
## نمادها و قراردادها

واحد و تعریف محلی نماد در دفترچه مرجع است. یک حرف در فصل‌های مختلف ممکن است کمیت متفاوتی باشد. فاز در دامنهٔ صفر تعریف نمی‌شود؛ فقط بازه‌های معتبر متصل را بگشایید.

| نماد | قرارداد و واحد |
| --- | --- |
| $e^{-i\omega t}$; $e^{i\mathbf{k}\cdot\mathbf{r}}$ | علامت زمانی/فضایی هستهٔ مثال‌ها؛ شاخهٔ خروجی در هر مدل تعریف می‌شود |
| $f$, $\omega=2\pi f$, $\lambda_0$ | فرکانس (Hz یا صریحاً GHz/THz)، فرکانس زاویه‌ای (rad/s)، طول موج خلأ (m یا صریحاً μm) |
| $\Lambda$, $m$, $k_{x,m}$ | دوره (طول)، مرتبهٔ صحیح، عدد موج عرضی (معکوس طول)؛ محیط فرودی و خروجی را مشخص کنید |
| $r$, $t$; $R$, $T$, $A$ | نسبت مختلط میدان در برابر کسر توان؛ در محیط نابرابر یا تابش مایل، T عموماً برابر \|t\|² نیست |
| $E$, $H$, $S_z$ | فازور قله: V/m، A/m، W/m²؛ شار میانگین ضریب ۱/۲ دارد. علامت TM بر پایهٔ میدان مماسی مطابق فصل ۲ است |
| $z=0$, $z=h$ | مرجع وجوه توری/لایهٔ TE: بازتاب در ورودی و عبور در خروجی؛ پیش از مقایسهٔ مختلط اثر مسیر را حذف کنید |
| $M$, $\Delta x$, $N$ | نیم‌شمار هارمونیک، فاصلهٔ شبکه یا شمار نمونه/عنصر؛ معنا و واحد در هر دفترچه مشخص است |
| $Z_s$, $Y_s$, $\Gamma$ | امپدانس مؤثر سطح (Ω)، ادمیتانس (S)، بازتاب مختلط؛ پارامتر مدار بدون استخراج، تخصیص‌یافته است |
| $\lvert h\rvert^2$, dB, dBm | بهرهٔ توان کانال؛ 10 log10 نسبت توان؛ توان نسبت به 1 mW. معیار آرایهٔ بهنجارشده را بازده ننامید |
| $\sigma$, $\Sigma$, $\rho$ | انحراف معیار با واحد کمیت، کوواریانس با حاصل‌ضرب واحدها و هم‌بستگی بدون واحد؛ مدل احتمال را بگویید |
