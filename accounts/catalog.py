import os


def env(name, default):
    value = os.environ.get(name, "").strip()
    return value or default


LINKED_APPS = [
    {
        "slug": "sabzify",
        "name": "سبزیفای",
        "mark": "س",
        "url": env("SABZIFY_URL", "https://sabzify.ir/"),
        "banner": "فضای سبز را همین‌جا شروع کنید",
        "banner_bg": "#f9c3a5",
        "banner_ink": "#d4530a",
        "kicker": "از سبزیفای",
        "title": "از ثبت درخواست تا تحویل باغ",
        "text": "کار را پیچیده نمی‌کنیم. سه مرحله شفاف دارید و در هر کدام می‌دانید چه اتفاقی می‌افتد.",
        "steps": [
            {"title": "ثبت درخواست", "text": "نوع کار، آدرس و زمان مناسب را می‌نویسید. کد پیگیری همان لحظه ساخته می‌شود."},
            {"title": "بازدید و برآورد", "text": "کارشناس هزینه، زمان اجرا و گیاهان پیشنهادی را شفاف با شما در میان می‌گذارد."},
            {"title": "اجرا و تحویل", "text": "پس از تأیید شما کار شروع می‌شود و در پایان، توصیه نگهداری هم تحویل داده می‌شود."},
        ],
        "stats": [
            {"value": "+۱۲", "label": "سال تجربه"},
            {"value": "۲٬۴۰۰", "label": "پروژه"},
            {"value": "۹۸٪", "label": "رضایت"},
        ],
        "chips": [],
    },
    {
        "slug": "keshtdrip",
        "name": "کشت‌دریپ",
        "mark": "د",
        "url": env("KESHTDRIP_URL", "https://keshtdrip.ir/"),
        "banner": "نوار تیپ را از کارخانه بخرید",
        "banner_bg": "#a6d6e7",
        "banner_ink": "#0a6f96",
        "kicker": "از کشت‌دریپ",
        "title": "خرید نوار تیپ و لوازم آبیاری قطره‌ای",
        "text": "فاصله قطره‌چکان، ضخامت دیواره و طول رول را با ردیف کشت یکی می‌کنید. کالا با قیمت روز و ارسال به سراسر ایران عرضه می‌شود.",
        "steps": [],
        "stats": [],
        "chips": ["گارانتی یک کشت", "ضمانت اصالت", "خرید بدون واسطه", "فروش نقدی و اقساطی"],
    },
    {
        "slug": "keshthamrah",
        "name": "کشت همراه",
        "mark": "ک",
        "url": env("KESHTHAMRAH_URL", "https://keshthamrah.ir/"),
        "banner": "نیروی همان شهر را رزرو کنید",
        "banner_bg": "#f2c6a6",
        "banner_ink": "#b85a14",
        "kicker": "از کشت همراه",
        "title": "سرویس‌دهنده همان منطقه، برای کار همان زمین",
        "text": "نوع خدمت و شهر زمین را مشخص می‌کنید. فقط کسانی پیشنهاد می‌شوند که همان حوزه را کار می‌کنند و در همان شهر فعال‌اند.",
        "steps": [],
        "stats": [
            {"value": "۳۱", "label": "سرویس‌دهنده"},
            {"value": "۱۸", "label": "نوع خدمت"},
            {"value": "۳۲", "label": "شهر"},
        ],
        "chips": ["آبیاری", "ماشین‌آلات", "هرس و باغداری", "کاشت و برداشت", "سمپاشی و تغذیه"],
    },
    {
        "slug": "keshtsarmayeh",
        "name": "حامی کشت",
        "mark": "ح",
        "url": env("KESHTHAMI_URL", "https://keshthami.ir/"),
        "banner": "وام و اعتبار خرید تا ۵ میلیارد",
        "banner_bg": "#c3d3cc",
        "banner_ink": "#0a3b26",
        "kicker": "از حامی کشت",
        "title": "وام کشاورزی و اعتبار خرید نهاده",
        "text": "به پشتوانه محصول، با چک صیادی یا با کشت مشارکتی وام و اعتبار خرید بگیرید؛ بدون معطلی بانکی و با بازپرداخت بعد از برداشت.",
        "steps": [],
        "stats": [
            {"value": "۳", "label": "روش تأمین"},
            {"value": "تا ۵ میلیارد", "label": "سقف اعتبار"},
            {"value": "۳۱", "label": "استان"},
        ],
        "chips": ["پشتوانه محصول", "چک صیادی", "کشت مشارکتی"],
    },
    {
        "slug": "keshtmosharekati",
        "name": "کشت مشارکتی",
        "mark": "م",
        "url": env("KESHTMOSHAREKATI_URL", "https://keshtmosharekati.ir/"),
        "banner": "زمین‌تان را به کشت مشترک بسپارید",
        "banner_bg": "#b9d5c0",
        "banner_ink": "#246336",
        "kicker": "از کشت مشارکتی",
        "title": "زمین شما، سرمایه و تخصص ما",
        "text": "با تأمین سرمایه و نهاده، آزمایش آب و خاک و مدیریت عملیات، ظرفیت زمین به یک کشت مشترک و شفاف تبدیل می‌شود.",
        "steps": [
            {"title": "ثبت اطلاعات زمین", "text": "مشخصات مالک، مساحت، موقعیت، منابع آب و تصاویر زمین ثبت می‌شود."},
            {"title": "بازدید گیاه‌پزشک", "text": "کارشناس ظرفیت‌ها و محدودیت‌های اجرایی زمین را از نزدیک بررسی می‌کند."},
            {"title": "آزمایش آب و خاک", "text": "نتیجه آزمایشگاه در پرونده می‌نشیند و با کد رهگیری دیده می‌شود."},
            {"title": "قرارداد شفاف", "text": "سهم هر طرف پیش از شروع کشت، روی همان پروژه مشخص می‌شود."},
        ],
        "stats": [],
        "chips": [],
    },
]


def sabzify_url(path):
    base = env("SABZIFY_URL", "https://sabzify.ir/").rstrip("/")
    return base + path


SABZIFY_SHOP_URL = sabzify_url("/shop/")

SABZIFY_CATEGORIES = [
    {"lines": ["طراحی", "فضای سبز"], "icon": "design", "url": sabzify_url("/request/?service=design")},
    {"lines": ["روف گاردن"], "icon": "roof", "url": sabzify_url("/request/?service=roof")},
    {"lines": ["هرس درختان"], "icon": "pruning", "url": sabzify_url("/request/?service=pruning")},
    {"lines": ["چمن‌کاری"], "icon": "lawn", "url": sabzify_url("/request/?service=lawn")},
    {"lines": ["کاشت", "گل و گیاه"], "icon": "planting", "url": sabzify_url("/request/?service=planting")},
    {"lines": ["خدمات", "گلخانه"], "icon": "greenhouse", "url": sabzify_url("/services/")},
]

SABZIFY_PRODUCTS = [
    {
        "name": "کود هیومیک اسید",
        "text": "بهبود ساختار خاک و جذب بهتر آب و مواد غذایی برای ریشه.",
        "spec": "بطری ۱ لیتری",
        "price": "۲۲۰٬۰۰۰",
        "badge": "مایع",
        "image": "img/products/humic-acid.png",
        "url": sabzify_url("/shop/humic-acid/"),
    },
    {
        "name": "کود آمینو اسید",
        "text": "محرک رشد برای دوران تنش، جابه‌جایی گلدان و ضعف برگ.",
        "spec": "بطری ۱ لیتری",
        "price": "۲۴۵٬۰۰۰",
        "badge": "مایع",
        "image": "img/products/amino-acid.png",
        "url": sabzify_url("/shop/amino-acid/"),
    },
    {
        "name": "کود 12-12-36",
        "text": "پتاسیم بالا برای گل‌دهی، میوه‌دهی و درشت شدن محصول.",
        "spec": "بسته ۱ کیلوگرمی",
        "price": "۱۸۵٬۰۰۰",
        "badge": "پودر",
        "image": "img/products/npk-12-12-36.png",
        "url": sabzify_url("/shop/npk-12-12-36/"),
    },
    {
        "name": "کود 20-20-20",
        "text": "کود کامل و متعادل برای رشد عمومی برگ، ساقه و ریشه.",
        "spec": "بسته ۱ کیلوگرمی",
        "price": "۱۶۵٬۰۰۰",
        "badge": "پودر",
        "image": "img/products/npk-20-20-20.png",
        "url": sabzify_url("/shop/npk-20-20-20/"),
    },
    {
        "name": "کود 10-52-10",
        "text": "فسفر بالا برای ریشه‌زایی، استقرار نشا و شروع گل‌دهی.",
        "spec": "بسته ۱ کیلوگرمی",
        "price": "۱۹۸٬۰۰۰",
        "badge": "پودر",
        "image": "img/products/npk-10-52-10.jpg",
        "url": sabzify_url("/shop/npk-10-52-10/"),
    },
    {
        "name": "کود کلسیم",
        "text": "ساقه‌های محکم‌تر و برگ‌های سالم‌تر، با کاهش ریزش گل و برگ.",
        "spec": "بسته",
        "price": "۱۹۰٬۰۰۰",
        "badge": "پودر",
        "image": "img/products/calcium.png",
        "url": sabzify_url("/shop/calcium/"),
    },
    {
        "name": "کود جلبک دریایی",
        "text": "رشد بهتر، تحمل بیشتر و برگ‌های پهن‌تر.",
        "spec": "بطری",
        "price": "۲۳۰٬۰۰۰",
        "badge": "مایع",
        "image": "img/products/seaweed.png",
        "url": sabzify_url("/shop/seaweed/"),
    },
]


def keshtdrip_url(path):
    base = env("KESHTDRIP_URL", "https://keshtdrip.ir/").rstrip("/")
    return base + path


KESHTDRIP_SHOP_URL = keshtdrip_url("/shop/")

KESHTDRIP_CATEGORIES = [
    {"lines": ["لوله", "نخدار"], "icon": "layflat", "url": keshtdrip_url("/shop/?category=layflat")},
    {"lines": ["نوار تیپ"], "icon": "tape", "url": keshtdrip_url("/shop/?category=drip-tape")},
    {"lines": ["لوله", "پلی‌اتیلن"], "icon": "pe", "url": keshtdrip_url("/shop/?category=pe-pipe")},
    {"lines": ["اتصالات"], "icon": "fitting", "url": keshtdrip_url("/shop/")},
    {"lines": ["لوله باغی"], "icon": "hose", "url": keshtdrip_url("/shop/?category=equipment")},
    {"lines": ["مه پاش"], "icon": "mist", "url": keshtdrip_url("/shop/?category=equipment")},
]

KESHTDRIP_PRODUCTS = [
    {
        "name": "لوله باغی / رول 200 متری",
        "spec": "قطر ۲۰",
        "price": "۴٬۴۰۰٬۰۰۰",
        "badge": "",
        "image": keshtdrip_url("/static/img/baghi-w480.b5a7ec7db347.webp"),
        "url": keshtdrip_url("/product/KSH-P-00000024/?variant=185"),
    },
    {
        "name": "لوله مه پاش/100 متر",
        "spec": "قطر ۱ اینچ",
        "price": "۱٬۴۹۱٬۰۰۰",
        "badge": "پرفروش",
        "image": keshtdrip_url("/static/img/meh-w480.34b2b2f80b78.webp"),
        "url": keshtdrip_url("/product/KSH-P-00000065/?variant=224"),
    },
    {
        "name": "لوله مه پاش/100 متر",
        "spec": "قطر ۲ اینچ",
        "price": "۱٬۸۰۹٬۰۰۰",
        "badge": "پرفروش",
        "image": keshtdrip_url("/static/img/meh-w480.34b2b2f80b78.webp"),
        "url": keshtdrip_url("/product/KSH-P-00000065/?variant=226"),
    },
    {
        "name": "لوله نخدار/100 متر/1.2 بار",
        "spec": "قطر ۱ اینچ",
        "price": "۱٬۱۲۳٬۲۰۰",
        "badge": "",
        "image": keshtdrip_url("/static/img/nakh-w480.8eee586a3ce5.webp"),
        "url": keshtdrip_url("/product/KSH-P-00000022/?variant=238"),
    },
    {
        "name": "لوله نخدار/100 متر/1.5 بار",
        "spec": "قطر ۶.۵ اینچ",
        "price": "۱۸٬۳۴۵٬۶۰۰",
        "badge": "",
        "image": keshtdrip_url("/static/img/nakh-w480.8eee586a3ce5.webp"),
        "url": keshtdrip_url("/product/KSH-P-00000004/?variant=236"),
    },
    {
        "name": "لوله پلی اتیلن سایز 75",
        "spec": "فشار ۸ بار",
        "price": "۲۲۰٬۰۰۰",
        "badge": "",
        "image": keshtdrip_url("/static/img/pe-75-w480.2339f7181791.webp"),
        "url": keshtdrip_url("/product/KSH-P-00000035/?variant=217"),
    },
]


def keshthamrah_url(path):
    base = env("KESHTHAMRAH_URL", "https://keshthamrah.ir/").rstrip("/")
    return base + path


KESHTHAMRAH_SERVICES_URL = keshthamrah_url("/services/")

KESHTHAMRAH_CATEGORIES = [
    {"lines": ["کاشت و", "برداشت"], "icon": "harvest", "url": keshthamrah_url("/services/planting/")},
    {"lines": ["آبیاری"], "icon": "irrigation", "url": keshthamrah_url("/services/irrigation/")},
    {"lines": ["سمپاشی", "و تغذیه"], "icon": "spraying", "url": keshthamrah_url("/services/protection/")},
    {"lines": ["هرس و", "باغداری"], "icon": "orchard", "url": keshthamrah_url("/services/orchard/")},
    {"lines": ["ماشین‌آلات"], "icon": "machinery", "url": keshthamrah_url("/services/machinery/")},
    {"lines": ["سایر", "خدمات"], "icon": "labor", "url": keshthamrah_url("/services/other/")},
]

KESHTHAMRAH_SERVICES = [
    {
        "name": "برداشت گندم و جو",
        "category": "کاشت و برداشت",
        "price": "۹۵۰٬۰۰۰",
        "icon": "wheat",
        "bg": "#e9f8ef",
        "ink": "#148a45",
        "url": keshthamrah_url("/order/wheat-harvest/"),
    },
    {
        "name": "آبیاری مزرعه",
        "category": "آبیاری",
        "price": "۷۰۰٬۰۰۰",
        "icon": "drop",
        "bg": "#e7f6fb",
        "ink": "#0a6f96",
        "url": keshthamrah_url("/order/classic-irrigation/"),
    },
    {
        "name": "سمپاشی باغ و مزرعه",
        "category": "سمپاشی و تغذیه",
        "price": "۹۰۰٬۰۰۰",
        "icon": "spray",
        "bg": "#f3f8e8",
        "ink": "#3d6b12",
        "url": keshthamrah_url("/order/spraying/"),
    },
    {
        "name": "هرس درختان میوه",
        "category": "هرس و باغداری",
        "price": "۸۸۰٬۰۰۰",
        "icon": "tree",
        "bg": "#eef6ea",
        "ink": "#2f6f4a",
        "url": keshthamrah_url("/order/pruning/"),
    },
    {
        "name": "شخم و دیسک‌زدن",
        "category": "ماشین‌آلات",
        "price": "۱٬۱۰۰٬۰۰۰",
        "icon": "tractor",
        "bg": "#f8efe6",
        "ink": "#b85a14",
        "url": keshthamrah_url("/order/tillage/"),
    },
    {
        "name": "برداشت با کمباین",
        "category": "ماشین‌آلات",
        "price": "۱٬۵۰۰٬۰۰۰",
        "icon": "combine",
        "bg": "#f8efe6",
        "ink": "#b85a14",
        "url": keshthamrah_url("/order/combine/"),
    },
]
