---
title: "۶.۲.۴ انتگرال محدود؛ اول توپولوژی، بعد ماده"
---

# ۶.۲.۴ انتگرال محدود؛ اول توپولوژی، بعد ماده

روش FIT که توماس وایلند معرفی کرد، از قانون انتگرالی ماکسول شروع می‌کنه و منبع اون رو از پایه‌های مهم حل‌گر گذرای CST معرفی می‌کنه. اینجا اول سراغ مشتق نمونه نقطه‌ای نمی‌ریم؛ روی یال جهت‌دار و وجه جهت‌دار شبکه اولیه و دوگان جابه‌جاشده انتگرال می‌گیریم.

```{figure} ../assets/chapter-06/integral-unknowns.svg
:alt: سمت چپ، چهار ولتاژ جهت‌دار مسئله FIT رو داریم؛ سمت راست، تکیه‌گاه یک تابع RWG در روش ممان رو می‌بینیم.

سمت چپ، چهار ولتاژ جهت‌دار مسئله FIT رو داریم؛ سمت راست، تکیه‌گاه یک تابع RWG در روش ممان رو می‌بینیم.
```

$$
\oint_{\partial A}\mathbf E\cdot d\mathbf l=-\frac{d}{dt}\int_A\mathbf B\cdot d\mathbf A,\qquad\oint_{\partial\widetilde A}\mathbf H\cdot d\mathbf l=\frac{d}{dt}\int_{\widetilde A}\mathbf D\cdot d\mathbf A+\int_{\widetilde A}\mathbf J\cdot d\mathbf A.
$$

$$
\int_{\partial V}\mathbf D\cdot d\mathbf A=Q_e,\qquad\int_{\partial V}\mathbf B\cdot d\mathbf A=0.
$$

## ۱. مجهول‌های مجتمع

$$
\widehat e_i=\int_{L_i}\mathbf E\cdot d\mathbf l,\quad\widehat b_j=\int_{A_j}\mathbf B\cdot d\mathbf A,\quad\widehat h_i=\int_{\widetilde L_i}\mathbf H\cdot d\mathbf l,\quad\widehat d_j=\int_{\widetilde A_j}\mathbf D\cdot d\mathbf A.
$$

این‌ها ولتاژ یال الکتریکی، شار مغناطیسی وجه اولیه، انتگرال خطی مغناطیسی یال دوگان و شار الکتریکی وجه دوگان‌اند. واحد و جهتشون با نمونه نقطه‌ای میدان فرق داره.

## ۲. ماتریس وقوع و معادله شبکه ماکسول

C یال اولیه رو به گردش وجه وصل می‌کنه، کرل دوگان همین کار رو در شبکه دوگان انجام می‌ده و S شارهای جهت‌دار وجه‌های یک حجم بسته رو جمع می‌کنه. درایه‌ها فقط صفر و مثبت و منفی یک‌اند؛ این‌ها اتصال هندسی‌اند، نه جنس ماده.

$$
C\widehat{\mathbf e}=-\frac d{dt}\widehat{\mathbf b},\quad\widetilde C\widehat{\mathbf h}=\frac d{dt}\widehat{\mathbf d}+\widehat{\mathbf j},\quad S\widehat{\mathbf b}=0,\quad\widetilde S\widehat{\mathbf d}=\mathbf q.
$$

$$
SC=0,\qquad\widetilde S\widetilde C=0,\qquad\widetilde S\widehat{\mathbf j}=-\frac d{dt}\mathbf q.
$$

«مرز یک مرز تهی است»؛ سهم یال مشترک روی سطح بسته خنثی می‌شه. اگه دیورژانس دوگان رو به آمپر اعمال کنیم، پیوستگی بار هم به دست میاد. این هویت‌های توپولوژیک روی شبکه انتخاب‌شده دقیق‌اند.

## ۳. بستن دستگاه با ماتریس ماده

$$
\widehat{\mathbf d}=M_\epsilon\widehat{\mathbf e},\qquad\widehat{\mathbf h}=M_{\mu^{-1}}\widehat{\mathbf b},\qquad\widehat{\mathbf j}=M_\sigma\widehat{\mathbf e}.
$$

در این ماتریس‌ها پارامتر ماده و نسبت مساحت به طول میاد. روی شبکه متعامد مناسب و ماده همسانگرد ساده، ممکنه قطری باشن؛ این ویژگی عمومی هر شبکه و ماده نیست.

| قانون | فرم پیوسته | فرم FIT |
|---|---|---|
| فارادی | $\nabla\times E=-\partial_tB$ | $C\widehat e=-\partial_t\widehat b$ |
| آمپر | $\nabla\times H=\partial_tD+J$ | $\widetilde C\widehat h=\partial_t\widehat d+\widehat j$ |
| گاوس الکتریکی | $\nabla\cdot D=\rho$ | $\widetilde S\widehat d=q$ |
| گاوس مغناطیسی | $\nabla\cdot B=0$ | $S\widehat b=0$ |
| پیوستگی بار | $\nabla\cdot J=-\partial_t\rho$ | $\widetilde S\widehat j=-\partial_tq$ |

## ۴. FIT، FDTD و مرز خمیده

روی شبکه کارتزین منظم، اگه ماده رو به شکل متعارف گسسته کنیم و زمان رو صریح و جابه‌جاشده جلو ببریم، می‌تونیم به همون رابطه یِی برسیم. زاویه نگاه فرق داره: نمونه مشتق در برابر مجهول انتگرالی و ماتریس وقوع. خود FIT هم محدود به زمان نیست و در حوزه فرکانس قابل فرمول‌بندیه.

شبکه مستطیلی معمول، مرز خمیده فلز یا دی‌الکتریک رو پله‌ای می‌کنه. منبع از روش هم‌شکل مرز و PBA در CST می‌گه تا مساحت بریده‌شده بهتر وارد مدل بشه، بدون ریز کردن کل باکس. تحلیل پالس پهن‌باند، المان فعال و زمان‌متغیر، و استخراج فاز و قطبش سلول دوره‌ای هم کاربردهای مهم‌اند.

:::{admonition} توضیح علمی تکمیلی؛ جدا از متن منبع
:class: note
منبع اول می‌گه همه خطای FIT از رابطه ماده میاد، اما در مثال حل‌شده همین جمله رو دقیق‌تر می‌کنه. هویت وقوع دقیق است؛ دقت نهایی هنوز به هندسه، تقریب ماده، زمان‌گام‌برداری، مرز و تفکیک محدود بستگی داره. اسم «مرز کامل» هم به معنی صفر بودن خطای عددی نیست.
:::

:::{admonition} مسئله حل‌شده
:class: tip
وجه مربعی اولیه با ضلع $\Delta=1\,\mathrm{mm}$ در صفحه ایکس–وای و عمود مثبت زد داریم. گردش پادساعت‌گرده؛ جهت مرجع یال ۱ و ۲ موافق و یال ۳ و ۴ مخالف گردشه. ولتاژها در زمان صحیح $[0.30,0.20,0.10,0.05]\,\mathrm V$، شار اولیه $2.00\times10^{-10}\,\mathrm{Wb}$ و گام زمان $1.0\,\mathrm{ps}$ است.

1. گردش و سطر C رو پیدا کنید.
2. شار جدید رو حساب کنید.
3. در خلأ، با مساحت $\Delta^2$ و طول دوگان $\Delta$، انتگرال خطی مغناطیسی رو به دست بیارید.
4. با SC=0 حفظ گاوس مغناطیسی رو توضیح بدید.
5. ارتباط FIT صریح کارتزین با یِی چیه؟ آیا FIT فقط حوزه زمانه؟

```{dropdown} دیدن پاسخ تشریحی کامل

$$
\widehat e_i=\int_{L_i}\mathbf E\cdot d\mathbf l,\qquad(C\widehat{\mathbf e}^{,n})_f=\widehat e_1^n+\widehat e_2^n-\widehat e_3^n-\widehat e_4^n.
$$

$$
(C\widehat{\mathbf e}^{,n})_f=0.30+0.20-0.10-0.05=0.35\,\mathrm V,\qquad C_{f,\{1,2,3,4\}}=[1,1,-1,-1].
$$

این علامت‌ها از جهت میان، نه گذردهی و تراوایی. فارادی در نیم‌گام‌های زمان می‌ده:

$$
C\widehat{\mathbf e}=-\frac{d\widehat{\mathbf b}}{dt},\qquad\frac{\widehat b^{n+1/2}-\widehat b^{n-1/2}}{\Delta t}=-(C\widehat{\mathbf e}^{,n})_f.
$$

$$
\widehat b^{n+1/2}=\widehat b^{n-1/2}-\Delta t(C\widehat{\mathbf e}^{,n})_f=2.00\times10^{-10}-(1.0\times10^{-12})(0.35)=1.9965\times10^{-10}\,\mathrm{Wb}.
$$

کنترل واحد هم می‌گه ولت ضربدر ثانیه برابر وبره. برای انتگرال خطی مغناطیسی، توپولوژی تنها کافی نیست؛ رابطه ماده می‌خوایم:

$$
\widehat h=M_{\mu^{-1}}\widehat b\approx\frac{\widetilde\ell}{\mu_0A}\widehat b,\quad A=\Delta^2,\quad\widetilde\ell=\Delta.
$$

$$
\widehat h^{n+1/2}\approx\frac{\widehat b^{n+1/2}}{\mu_0\Delta}=\frac{1.9965\times10^{-10}}{(4\pi\times10^{-7})(10^{-3})}\approx0.159\,\mathrm A.
$$

$$
\widehat h=\int_{\widetilde L}\mathbf H\cdot d\mathbf l,\qquad H\approx\widehat h/\widetilde\ell\approx159\,\mathrm{A/m}.
$$

واحد انتگرال خطی آمپره، نه آمپر بر متر. تبدیل آخر، یکنواختی تقریبی H روی یال رو فرض کرده؛ کنار مرز ماده و شبکه پیچیده، تقریب ماده دقیق‌تری لازم داریم.

$$
SC=0,\qquad SC\widehat{\mathbf e}=-S\frac{d\widehat{\mathbf b}}{dt}\quad\Longrightarrow\quad\frac d{dt}(S\widehat{\mathbf b})=0.
$$

پس دیورژانس مغناطیسی گسسته‌ای که اول صفر بوده، با به‌روزرسانی سازگار صفر می‌مونه. این حفظ داده اولیه سازگاره؛ شار اولیه غلط رو تعمیر نمی‌کنه. با شبکه منظم، ماتریس ماده متعارف و جهش زمانی، FIT می‌تونه همون یِی رو بده؛ اما فرمول انتگرالی و توپولوژیکش حل حوزه فرکانس هم داره.

```
:::
