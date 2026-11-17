---
title: "۶.۲.۱ المان محدود؛ از فرم قوی تا مجهول یالی"
---

# ۶.۲.۱ المان محدود؛ از فرم قوی تا مجهول یالی

خب، برسیم به غول مهندسی الکترومغناطیس! روش المان محدود، یا FEM، همون آچارفرانسه ما برای حل هندسه پیچیده است. این روش، که در نرم‌افزارهایی مثل HFSS و COMSOL به کار می‌ره، روی تحلیل تغییراتی و مسئله مقدار مرزی بنا شده. بیایید ببینیم زیر کاپوتش چه خبره.

## ۱. استخراج قدم‌به‌قدم فرم قوی

از معادلات کرل و جریان منبع تحمیلی شروع می‌کنیم:

$$
\nabla\times\mathbf E=-i\omega\mathbf B,\qquad\nabla\times\mathbf H=i\omega\mathbf D+\mathbf J_{\rm imp}.
$$

رابطه‌های ماده این‌ها هستند:

$$
\mathbf D=\epsilon_0\overline{\overline\epsilon}_r\mathbf E,\qquad\mathbf B=\mu_0\overline{\overline\mu}_r\mathbf H.
$$

برای اینکه فعلاً درگیر تانسور نشیم، منبع اون‌ها رو به اسکالر مختلط مؤثر کاهش می‌ده. از قانون فارادی، میدان مغناطیسی رو بیرون می‌کشیم:

$$
\mathbf H=-\frac{1}{i\omega\mu_0\mu_r}\nabla\times\mathbf E.
$$

در معکوس تراوایی ضرب می‌کنیم و یک کرل دیگه می‌گیریم:

$$
\mu_r^{-1}\nabla\times\mathbf E=-i\omega\mu_0\mathbf H.
$$

$$
\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)=-i\omega\mu_0\nabla\times\mathbf H.
$$

حالا آمپر–ماکسول رو جای‌گذاری می‌کنیم:

$$
\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)=-i\omega\mu_0(i\omega\epsilon_0\epsilon_r\mathbf E+\mathbf J_{\rm imp}).
$$

با تعریف عدد موج آزاد، نتیجه می‌شه:

$$
k_0^2=\omega^2\mu_0\epsilon_0,\qquad\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E=-i\omega\mu_0\mathbf J_{\rm imp}.
$$

این شد فرم قوی. اما انتظار مشتق کلاسیک مرتبه دوم در همه‌جا، مخصوصاً کنار ناپیوستگی ماده و لبه تیز، دردسرسازه. پس سراغ فرم ضعیف می‌ریم تا نیاز مشتق‌پذیری تقریب رو کمتر کنیم.

## ۲. باقیمانده وزن‌دار و انتگرال‌گیری جزءبه‌جزء

$$
\mathbf R=\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E+i\omega\mu_0\mathbf J_{\rm imp}.
$$

به‌جای صفر کردن باقیمانده در تک‌تک نقطه‌ها، در تابع آزمون ضرب می‌کنیم و روی حجم انتگرال می‌گیریم. منبع در معرفی اولیه، تابع آزمون رو بدون مزدوج نوشته:

$$
\int_V\mathbf W\cdot[\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E],dV=-i\omega\mu_0\int_V\mathbf W\cdot\mathbf J_{\rm imp},dV.
$$

اتحاد برداری و قضیه گاوس، یک کرل رو به تابع آزمون منتقل می‌کنن:

$$
\int_V\mathbf W\cdot\nabla\times\mathbf A,dV=\int_V(\nabla\times\mathbf W)\cdot\mathbf A,dV-\int_{\partial V}(\mathbf W\times\mathbf A)\cdot\hat{\mathbf n},dS.
$$

بعد، منبع فرم زیر رو با این علامت مرزی چاپ کرده. برای پیاده‌سازی، اصلاح جداگانه پایین رو حتماً ببینیم:

$$
\int_V[\mu_r^{-1}(\nabla\times\mathbf W)\cdot(\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf W\cdot\mathbf E],dV+i\omega\mu_0\int_{\partial V}\mathbf W\cdot(\hat{\mathbf n}\times\mathbf H),dS=-i\omega\mu_0\int_V\mathbf W\cdot\mathbf J_{\rm imp},dV.\quad\text{[printed]}
$$

:::{admonition} توضیح علمی تکمیلی؛ جدا از متن منبع
:class: note
برای عمود رو به بیرون، با استفاده از اتحاد بالا و رابطه $\mu_r^{-1}\nabla\times\mathbf E=-i\omega\mu_0\mathbf H$، علامت جمله مرزی در سمت چپ **منفی** می‌شه:

$$
a(\mathbf E,\mathbf W)-i\omega\mu_0\int_{\partial V}\mathbf W^*\cdot(\hat{\mathbf n}\times\mathbf H),dS=-i\omega\mu_0\int_V\mathbf W^*\cdot\mathbf J_{\rm imp},dV.
$$

اینجا $a$ فرم حجمی کرل–کرل منهای جرمه و در آزمون مختلط از $\mathbf W^*$ استفاده می‌کنیم. برای موج خروجی، $\hat{\mathbf n}\times\mathbf H=-Y\mathbf E_t$ است؛ پس سهم ماتریسی مرز، مثبتِ $i\omega\mu_0 B_Y$ می‌شه. تعریف نمادین ادمیتانس در حل بعدی منبع، علامت مخالف داره. جهت عمود، تعریف ادمیتانس و فرم ضعیف رو باید با هم تبدیل کنیم. [اثبات کرل ضعیف MFEM](https://mfem.org/fem_weak_form/) اتحاد انتگرالی رو روشن نشون می‌ده.

برای پیاده‌سازی با عمود رو به بیرون، تعریف مرز و سمت راست اصلاح‌شده رو صریح بنویسیم:

$$
\hat{\mathbf n}\times\mathbf H=-Y\mathbf E_t+\mathbf g_{\rm inc},\qquad[K-k_0^2M+i\omega\mu_0B_Y]\mathbf e=\mathbf f.
$$

$$
f_i=-i\omega\mu_0\int_V\mathbf N_i^*\cdot\mathbf J_{\rm imp}\,dV+i\omega\mu_0\int_{S_{\rm rad}}\mathbf N_{i,t}^*\cdot\mathbf g_{\rm inc}\,dS.
$$
اینجا $B_Y$ ادمیتانس مثبت بار یا موج خروجی رو روی سطح مربوط می‌گیره. پس علامت‌ها رو با هم اصلاح کردیم، نه اینکه فقط یک جمله مرزی رو جدا عوض کنیم.
:::

مزیت روشنه: فقط کرل مرتبه اول باقی می‌مونه، پیوستگی مماسی راحت‌تر جا می‌افته و فیزیک مرز مستقیم وارد انتگرال سطحی می‌شه.

## ۳. اعمال شرط مرزی

روی PEC، مؤلفه مماسی میدان و تابع آزمون صفره. مرز امپدانسی هم کمک می‌کنه لایه رسانای نازک، مثلاً گرافن، رو بدون مش کردن ضخامت اتمی مدل کنیم. منبع رابطه سطحی رو با $Z_s$ این‌طور می‌نویسه:

$$
\int_{S_{\rm IBC}}\mathbf W\cdot(\hat{\mathbf n}\times\mathbf H),dS=\frac1{Z_s}\int_{S_{\rm IBC}}(\hat{\mathbf n}\times\mathbf W)\cdot(\hat{\mathbf n}\times\mathbf E),dS.\quad\text{[source boundary definition]}
$$

برای مرز تشعشعی، بی‌نهایت رو با شرط خروجی از نوع رابین تقریب می‌زنیم. این شرط باید آزموده بشه؛ در هر زاویه، مرز شفاف دقیق نیست.

## ۴. چرا میدان رو روی یال می‌ذاریم؟

نکته امتحانی! تقریب برداری گره‌ای معمول می‌تونه پیوستگی ناموجه در مرز ماده تحمیل کنه و مد کاذب بسازه. نِدِلِک گفت میدان رو به گره نچسبونیم؛ مجهول رو روی یال بذاریم. این‌طوری پیوستگی مماسی حفظ می‌شه و مؤلفه عمودی، آزادی مناسب مرز ماده رو داره.

## ۵. تشکیل دستگاه خلوت

$$
([K]-k_0^2[M]+ik_0[B])\{e\}=\{f\}.
$$

ماتریس سختی، جرم و مرزی ممکنه بزرگ باشن، اما خلوت‌اند؛ چون تابع پایه محلی فقط با همسایه‌ها هم‌پوشانی داره. ضریب جلوی ماتریس مرزی هم به تعریف و بهنجارسازیش بستگی داره. منبع مثال کاواک و مرز امپدانسی گرافن رو می‌زنه و برای حذف مش بسیار ریز لایه نازک، با لحن خودمانی از «هزار برابر سریع‌تر» حرف می‌زنه.

:::{admonition} توضیح علمی تکمیلی؛ جدا از متن منبع
:class: note
المان یالی به کنترل مد کاذب کمک می‌کنه، اما هر فضای تهی یا خطای مدل رو خودکار حذف نمی‌کنه. جایگزینی ورقه نازک هم مدل ماده معتبر می‌خواد؛ مقدار افزایش سرعت به مش، حل‌گر و دقت بستگی داره. اینجا ادعای اجرای نرم‌افزار تجاری FEM نداریم.
:::

:::{admonition} مسئله حل‌شده
:class: tip
یک سلول در راستای $x,y$ دوره‌ایه. حجمش دی‌الکتریک ناهمگن داره، روی $S_{\rm IBC}$ لایه رسانای نازک با $Z_s$ داریم و مرز بالا تشعشعی مرتبه اوله. $\epsilon_r,\mu_r$ اسکالر و $\mathbf J_{\rm imp}$ معلوم‌اند.

1. فرم ضعیف میدان رو با سهم مرز امپدانسی و تشعشعی استخراج کنید.
2. میدان رو با تابع یالی نِدِلِک بسط بدید و درایه ماتریس‌ها رو بنویسید.
3. بگید چرا المان یالی اینجا مناسب‌تره.

```{dropdown} دیدن پاسخ تشریحی کامل

منبع از معادله حاکم شروع می‌کنه، این بار تابع آزمون رو مزدوج می‌گیره و می‌نویسه:

$$
\nabla\times(\mu_r^{-1}\nabla\times\mathbf E)-k_0^2\epsilon_r\mathbf E=-i\omega\mu_0\mathbf J_{\rm imp}.
$$

$$
\int_V\mu_r^{-1}(\nabla\times\mathbf W^*)\cdot(\nabla\times\mathbf E),dV-k_0^2\int_V\epsilon_r\mathbf W^*\cdot\mathbf E,dV+i\omega\mu_0\int_{\partial V}\mathbf W^*\cdot(\hat{\mathbf n}\times\mathbf H),dS=-i\omega\mu_0\int_V\mathbf W^*\cdot\mathbf J_{\rm imp},dV.\quad\text{[printed]}
$$

برای ثبت حل منبع، تعریف‌های نمادین مرزش رو نگه می‌داریم؛ موقع پیاده‌سازی با عمود رو به بیرون، اصلاح بالا رو اعمال کنیم:

$$
\hat{\mathbf n}\times\mathbf H=Y_s\mathbf E_t,\quad Y_s=Z_s^{-1},\qquad\hat{\mathbf n}\times\mathbf H\approx Y_{\rm rad}\mathbf E_t+\mathbf g_{\rm inc}.
$$

قسمت وابسته به میدان مجهول وارد ماتریس مرزی می‌شه و تحریک معلوم به سمت راست می‌ره. اگه ورقه داخل حجم باشه، باید میدان دو طرف و پرش مغناطیسی رو مدل کنیم؛ نمی‌شه همین شرط یک‌طرفه رو بی‌تغییر بهش چسبوند.

$$
\mathbf E_h(\mathbf r)=\sum_{j=1}^{N_e}e_j\mathbf N_j(\mathbf r),\qquad\mathbf W=\mathbf N_i.
$$

$$
[K-k_0^2M+i\omega\mu_0(B_{\rm IBC}+B_{\rm rad})]\mathbf e=\mathbf f.\quad\text{[source symbolic definitions]}
$$

$$
K_{ij}=\int_V\mu_r^{-1}(\nabla\times\mathbf N_i^*)\cdot(\nabla\times\mathbf N_j),dV,\qquad M_{ij}=\int_V\epsilon_r\mathbf N_i^*\cdot\mathbf N_j,dV.
$$

$$
(B_{\rm IBC})_{ij}=\int_{S_{\rm IBC}}Y_s\mathbf N_{i,t}^*\cdot\mathbf N_{j,t},dS,\qquad(B_{\rm rad})_{ij}=\int_{S_{\rm rad}}Y_{\rm rad}\mathbf N_{i,t}^*\cdot\mathbf N_{j,t},dS.
$$

$$
f_i=-i\omega\mu_0\left[\int_V\mathbf N_i^*\cdot\mathbf J_{\rm imp},dV+\int_{S_{\rm rad}}\mathbf N_{i,t}^*\cdot\mathbf g_{\rm inc},dS\right].\quad\text{[source symbolic definitions]}
$$

درجه آزادی یال‌های روبه‌رو رو با فاز فلوکه و جهت درست یال به هم وصل می‌کنیم. تناوب فقط یک ماتریس مرزی مستقل اضافه نیست. در مرز عادی دو ماده، میدان مماسی پیوسته است، اما مؤلفه عمودی الزاماً پیوسته نیست؛ تابع یالی دقیقاً با همین تفاوت سازگاره و به کنترل مد کاذب کمک می‌کنه.

پس دشواری اصلی این مثال، کنار هم گذاشتن علامت جزءبه‌جزء، مدل درست لایه نازک و قید فلوکه روی مرزهای دوره‌ایه.

```
:::
