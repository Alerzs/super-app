import re

_DIGIT_TRANSLATION = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


def normalize_phone(value):
    """Return an Iranian mobile number as 09xxxxxxxxx, or raise ValueError."""
    if value is None:
        raise ValueError("شماره همراه را وارد کنید.")

    text = str(value).translate(_DIGIT_TRANSLATION).strip()
    text = re.sub(r"[\s\-()]+", "", text)
    if text.startswith("+"):
        text = text[1:]
    if text.startswith("0098"):
        text = text[4:]
    elif text.startswith("98"):
        text = text[2:]
    if text.startswith("9") and len(text) == 10:
        text = "0" + text
    if not re.fullmatch(r"09\d{9}", text):
        raise ValueError("شماره همراه باید یک موبایل ایران باشد؛ مثل ۰۹۱۲۳۴۵۶۷۸۹.")
    return text
