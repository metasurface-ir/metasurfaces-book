---
title: "استخراج مدل فوریهٔ TE محدود"
---

# استخراج مدل فوریهٔ TE محدود

برای گذردهی اسکالر غیرمغناطیسی و $E_y(x,z)$:

$$
\frac{\partial^2E_y}{\partial x^2}+\frac{\partial^2E_y}{\partial z^2}+k_0^2\epsilon_r(x)E_y=0.
$$

$E_y=\sum_m E_m(z)e^{-ik_0\alpha_mx}$ و سری فوریهٔ $\epsilon_r(x)$ را جای‌گذاری و روی هارمونیک‌ها تصویر کنید:

$$
\frac{d^2\mathbf E}{dz^2}+k_0^2(\boldsymbol\epsilon-\mathbf A^2)\mathbf E=0,
\qquad \epsilon_{mn}=\epsilon_{m-n},\quad A_{mn}=\alpha_m\delta_{mn}.
$$

برای مستطیل مرکزی با کسر پرشدگی $f=w/\Lambda$:

$$
\epsilon_\ell=n_g^2\delta_{\ell0}+(n_r^2-n_g^2)f\,\operatorname{sinc}(\ell f),
\qquad \operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.
$$

ضرایب از جمله حد $\ell=0$ تحلیلی‌اند؛ شبکهٔ پیکسلی در حل‌گر دوره نیست. برای مادهٔ حقیقی، ماتریس هرمیتی است و مسئلهٔ ویژه:

$$
(\boldsymbol\epsilon-\mathbf A^2)\mathbf W=\mathbf W\mathbf Q^2.
$$

ریشه‌های $\mathbf Q$ نیز شاخهٔ نامنفی دارند. ماتریس مد مشتق $\mathbf V=\mathbf W\mathbf Q$ است. برای پرهیز از عامل انتقال نمایی رشدکننده، ضرایب رو‌به‌جلو $\mathbf a$ را در وجه بالا و رو‌به‌عقب $\mathbf b$ را در وجه پایین تعریف کنید:

$$
\mathbf E(z)=\mathbf W\left[e^{-ik_0\mathbf Qz}\mathbf a+
e^{-ik_0\mathbf Q(h-z)}\mathbf b\right],\qquad
\mathbf P=e^{-ik_0\mathbf Qh}.
$$

پیوستگی $E_y$ و مشتق عمودی با تراوایی مشترک:

$$
\begin{bmatrix}
\mathbf V+\mathbf Q_i\mathbf W & (\mathbf Q_i\mathbf W-\mathbf V)\mathbf P\\
(\mathbf V-\mathbf Q_t\mathbf W)\mathbf P & -\mathbf V-\mathbf Q_t\mathbf W
\end{bmatrix}
\begin{bmatrix}\mathbf a\\\mathbf b\end{bmatrix}
=\begin{bmatrix}2\mathbf Q_i\mathbf e_0\\\mathbf 0\end{bmatrix}.
$$

$\mathbf Q_i,\mathbf Q_t$ قطری بیرونی و $\mathbf e_0$ تحریک مرتبهٔ صفر است. بازیابی ضرایب:

$$
\mathbf r=\mathbf W(\mathbf a+\mathbf P\mathbf b)-\mathbf e_0,
\qquad \mathbf t=\mathbf W(\mathbf P\mathbf a+\mathbf b).
$$

تابع `solve_cell` این معادلات، `sample_ey` بازسازی داخل و بیرون و `film_reference` مرجع اسکالر جداگانهٔ فرنل و فابری‌پرو را اجرا می‌کنند. برای روش عمومی‌تر [Moharam و Gaylord](https://doi.org/10.1364/JOSA.71.000811) را ببینید.

:::{warning} قطبش جزئی از فرمول‌بندی است
کاهش TE از میدان الکتریکی مماسی پیوسته در مرز عمودی دی‌الکتریک استفاده می‌کند. تغییر برچسب به TM، معادلهٔ ماکسول TM و برخورد فوریه‌ای لازم با حاصل‌ضرب ناپیوستهٔ مواد را پیاده نمی‌کند. حل‌گر برداری عمومی فرمول‌بندی و شاهد همگرایی مستقل می‌خواهد.
:::

```{figure} ../assets/chapter-03/fields.png
:alt: قسمت حقیقی میدان TE و مربع دامنه پیرامون سه ریج تکراری دی‌الکتریک.

بازسازی تمام‌موج سلول مرکزی؛ هارمونیک اوانسنت خروجی در میدان نزدیک سهم دارد. مربع دامنه، توان یا چگالی انرژی نیست.
```
