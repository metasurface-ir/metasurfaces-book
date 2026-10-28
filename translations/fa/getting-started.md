---
title: اجرای کتاب محاسباتی
short_title: نصب و جدول اجرا
---

# اجرای کتاب محاسباتی

(setup-read)=
## مطالعه و کاوش

کتاب منتشرشده خروجی‌های ذخیره‌شده را بدون نصب پایتون نمایش می‌دهد. آزمایشگاه مرورگر را از فصل یا گزینهٔ **باز کردن در زبانهٔ جدید** باز کنید. این ابزارها در سایت میزبانی می‌شوند؛ HTML آن‌ها برای دانلود عرضه نمی‌شود و در بستهٔ منبع پایتون نیست. ویرایش محاسبات پایتون به محیط محلی ژوپیتر نیاز دارد.

(setup-sources)=
## انتخاب فایل‌های منبع

| هدف | فایل مورد نیاز |
| --- | --- |
| اجرای دوبارهٔ تحقیق یک فصل | ZIP کامل منبع را از آزمایشگاه فصل استخراج کنید؛ پوشه‌های `notebooks/`، `simulations/`، `scripts/` و `data/` را نگه دارید |
| اجرای فصل ۴ یا هر دفترچهٔ فصل ۱۰ | دفترچه را از صفحهٔ کتاب و `requirements-labs.txt` را از مخزن بگیرید؛ توابع عددی در خود دفترچه‌اند |
| افزودن محتوا، بازتولید شکل/ابزار مرورگر یا ساخت دو زبان | [مخزن کامل](https://github.com/metasurface-ir/metasurfaces-book) را کلون کنید؛ بسته‌های منبع، ابزارها و قالب‌های انتشار را ندارند |

در بستهٔ منبع، `START-HERE.md` را از ریشهٔ پوشهٔ استخراج‌شده دنبال کنید. دفترچه‌ای که از `simulations/` وارد یا از `data/` می‌خواند به‌تنهایی کافی نیست. بستهٔ فارسی متن ترجمه‌شده را با همان کد اجرایی و خروجی مرجع انگلیسی دارد.

(setup-environment)=
## آماده‌سازی محیط علمی

از Python 3.12 استفاده کنید. در ریشهٔ بسته یا مخزن:

```sh
python -m venv .venv
```

در PowerShell با `.\.venv\Scripts\Activate.ps1` و در macOS/Linux با `source .venv/bin/activate` محیط را فعال کنید. اگر فعال‌سازی PowerShell در دسترس نیست، به‌جای `python` از `.\.venv\Scripts\python.exe` استفاده کنید.

```sh
python -m pip install -r requirements-labs.txt
python -m jupyterlab
```

هستهٔ همین محیط را انتخاب کنید. ویرایش پارامتر را ذخیره کنید، **Restart Kernel and Run All Cells** را بزنید و دفترچهٔ کامل را ذخیره کنید. مثال‌ها با NumPy/SciPy/Matplotlib روی CPU اجرا می‌شوند؛ مقایسهٔ شبکهٔ عصبی scikit-learn نیز می‌خواهد. برای مثال‌های منتشرشده GPU، حل‌گر تجاری یا دادهٔ خارجی لازم نیست. هنگام ذخیرهٔ خروجی انتشار ایستا، ویجت اختیاری را غیرفعال نگه دارید.

برای مقایسهٔ پیاده‌سازی جداگانهٔ RCWA در فصل‌های ۳/۵ و ms-11، فایل `requirements-validation.txt` را از مخزن کامل یا بستهٔ مرتبط نصب کنید. بدون `--grcwa`، ممیزی اجرا نشدن آن مقایسه را صریح ثبت می‌کند. توافق دو پیاده‌سازی RCWA، کنترل با خانوادهٔ عددی مستقل نیست.

(setup-run-matrix)=
## ترتیب دفترچه‌ها، وابستگی و زمان اندازه‌گیری‌شده

مسیرهای زیر نسبت به `notebooks/` هستند. زمان‌ها اندازه‌گیری تقریبی اجرای هستهٔ تازه در ۲۸ اکتبر ۲۰۲۶، Windows، پردازندهٔ Intel Core i3-5005U، Python 3.12 و یک رشتهٔ BLAS هستند. زمان آغاز هسته و رسم را شامل می‌شوند، اما نصب، ممیزی و ساخت سایت را نه؛ تضمین سرعت نیستند. برای ماتریس‌های کوچک، **پیش از** باز کردن ژوپیتر `OPENBLAS_NUM_THREADS=1` و `OMP_NUM_THREADS=1` را تنظیم کنید (PowerShell: `$env:OPENBLAS_NUM_THREADS='1'`؛ پوسته: `export OPENBLAS_NUM_THREADS=1`).

| فصل/آزمایشگاه | دفترچه‌ها به‌ترتیب | ورودی محلی لازم | زمان اندازه‌گیری |
| --- | --- | --- | --- |
| ۱ | `01-first-metasurface-model.ipynb` | `intro_sheet.py` | 20 ثانیه |
| ۲ | `02-waves-and-interfaces.ipynb` | `waves_interfaces.py`، `source_provenance.py` | 22 ثانیه |
| ۴، پیش از حل‌گر فصل ۳ | `04-floquet-orders.ipynb` | مستقل؛ ipywidgets اختیاری | 13 ثانیه |
| ۳ | `03-unit-cell-library.ipynb` | `unit_cell_te.py`؛ کتابخانهٔ فصل ۳ را می‌سازد | 18 ثانیه |
| ۵ | `05-beam-steering.ipynb` سپس `05-wavefront-models.ipynb` | ماژول‌های TE/سنتز و کتابخانهٔ فصل ۳؛ دفترچهٔ دوم کتابخانهٔ فصل ۵ ساخته‌شده توسط اولی را می‌خواند | 13 ثانیه + 7 ثانیه |
| ۶، همراه ۳/۵ | `06-numerical-methods.ipynb` | ماژول‌های عددی/لایه/TE و فایل‌های معیار فصل ۶ در بسته؛ در صورت نیاز با ممیزی فصل ۶ بازسازی شوند | 11 ثانیه |
| ۷ | `07-tunable-metasurfaces.ipynb` | `tunable_surface.py`؛ مدار تخصیص‌یافته، آرایهٔ اسکالر و کنترل مصنوعی | 20 ثانیه |
| ۸ | `08-communication-links.ipynb` | `communication_link.py`؛ مدل اسکالر دهانه/کانال | 16 ثانیه |
| ۹ | `09-fabrication-measurement.ipynb` | `materials_measurement.py`؛ مشاهده‌های مصنوعی تولیدشده | 17 ثانیه |
| ۱۰ | `10-resonant-surrogate.ipynb` سپس `10-neural-comparison.ipynb` | دادهٔ تحلیلی مستقل؛ مقایسه scikit-learn می‌خواهد؛ هر کدام مستقل اجرا می‌شود | 10 ثانیه + 28 ثانیه |
| ms-09/10/11 | `09-dispersion.ipynb` سپس `10-coupling.ipynb` سپس `11-inverse-design.ipynb` | `design_studies.py` و ماژول‌های TE/سنتز؛ هر سه پیش از ممیزی/صدور مشترک اجرا شوند | 57 ثانیه + 18 ثانیه + 27 ثانیه |

برای ترتیب مفهومی، [نقشهٔ پیش‌نیازها](learning-path.md) را بخوانید. پایان موفق اجرا ممکن است شامل بهینه‌ساز ناموفق یا طرح دست‌نیافتنی باشد؛ این نتیجه‌ها و علت توقفشان را نگه دارید.

(setup-validation)=
## راستی‌آزمایی نتیجه و صدور فقط از مخزن کامل

دستور ممیزی را از ریشهٔ بسته/مخزن اجرا کنید. فایل `scripts/validate_*.py` مربوط در بستهٔ کامل آن تحقیق هست. ممیزی مرجع ثابت ممکن است آزمایش عمداً تغییریافته را رد کند؛ معیار پذیرش را صریح بازتعریف کنید و آزمون مرجع را از تحقیق قابل ویرایش جدا نگه دارید.

| تحقیق | ممیزی پس از ذخیرهٔ اجرا | دستور انتشار — فقط مخزن کامل |
| --- | --- | --- |
| ۱ | `python scripts/validate_chapter01.py` | `python scripts/export_chapter01.py` |
| ۲ | `python scripts/validate_chapter02.py` | `python scripts/export_chapter02.py` |
| ۳ | `python scripts/validate_chapter03.py --grcwa` | `python scripts/export_chapter03.py` |
| ۴ | گزاره‌های کنترلی تحلیلی مستقل داخل دفترچه | `python scripts/export_chapter04_figures.py` |
| ۵ | `python scripts/validate_chapter05.py --grcwa` | `python scripts/export_chapter05.py` |
| ۶ | `python scripts/validate_chapter06.py` (دادهٔ معیار را نیز بازتولید می‌کند) | `python scripts/export_chapter06.py` |
| ۷ | `python scripts/validate_chapter07.py` | `python scripts/export_chapter07.py` |
| ۸ | `python scripts/validate_chapter08.py` | `python scripts/export_chapter08.py` |
| ۹ | مقایسهٔ دفترچه و `python scripts/validate_chapter09.py` | `python scripts/export_chapter09.py` |
| ۱۰ | مقایسهٔ کنارگذاشته‌شده، همانی‌ها و وضعیت ثبت‌شدهٔ بهینه‌ساز در دفترچه | `python scripts/export_chapter10_figures.py` |
| ms-09/10/11 | `python scripts/validate_design_studies.py --grcwa` | `python scripts/export_design_studies.py` |

واحد، قرارداد زمانی/فضایی، صفحهٔ مرجع، پارامتر، بذر تصادفی، شواهد همگرایی و محدودیت مدل را نگه دارید. باقیماندهٔ کوچک، جمع توان پایسته یا هش منشأ به‌تنهایی دقت علمی را ثابت نمی‌کند. پیش از جایگزینی مرجع منتشرشده، [روش مشارکت](contributing.md) را بخوانید.

(setup-build)=
## ساخت و پیش‌نمایش هر دو زبان

از **مخزن کامل** با Python 3.12 و Node.js 24/npm در `PATH` استفاده کنید. محیط مجزای `.book-env` را مانند بالا بسازید و فعال کنید، سپس:

```sh
python -m pip install -r requirements.txt
python scripts/validate_translations.py
python scripts/check_notebook_provenance.py
python scripts/build_bilingual.py
python -m http.server 8000 --directory _build/html
```

برای این سرور محلی، `BASE_URL` را خالی بگذارید (PowerShell: `$env:BASE_URL=''`). انگلیسی در `http://localhost:8000/` و فارسی در `http://localhost:8000/fa/` است. GitHub Actions پیشوند انتشار را خودکار تنظیم می‌کند. `jupyter-book start` برای نگارش انگلیسی مفید است؛ سوییچ کامل زبان و خروجی فارسی به ساخت دو‌زبانه نیاز دارند. ساخت، خروجی ذخیره‌شده را نمایش و هویت آن را بررسی می‌کند و همهٔ شبیه‌سازی‌ها را دوباره اجرا نمی‌کند. درخواست ادغام، مجموعهٔ کوچک آزمون تغییر پارامتر را نیز اجرا می‌کند.
