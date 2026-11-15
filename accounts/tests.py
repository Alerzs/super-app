from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .phones import normalize_phone


class PhoneNormalizationTests(SimpleTestCase):
    def test_persian_digits(self):
        self.assertEqual(normalize_phone("۰۹۱۲۳۴۵۶۷۸۹"), "09123456789")

    def test_country_code_and_spaces(self):
        self.assertEqual(normalize_phone("+98 912 345 6789"), "09123456789")

    def test_rejects_incomplete_number(self):
        with self.assertRaises(ValueError):
            normalize_phone("0912")


class AccountFlowTests(TestCase):
    def setUp(self):
        self.password = "Safe-pass-1840"
        self.raw_phone = "۰۹۱۲۱۱۱۲۲۳۳"

    def register(self):
        return self.client.post(
            reverse("register"),
            {
                "phone": self.raw_phone,
                "first_name": "علیرضا",
                "last_name": "آزمایش",
                "password1": self.password,
                "password2": self.password,
            },
        )

    def test_login_page_keeps_the_portal_name(self):
        response = self.client.get(reverse("login"))
        self.assertContains(response, "ورود | کشتیار")
        self.assertNotContains(response, "testserver")

    def test_home_lists_five_sites_and_local_stylesheet(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "سبزیفای")
        self.assertContains(response, "کشت‌دریپ")
        self.assertContains(response, "کشت همراه")
        self.assertContains(response, "حامی کشت")
        self.assertContains(response, "کشت مشارکتی")
        self.assertContains(response, "از ثبت درخواست تا تحویل باغ")
        self.assertContains(response, "گارانتی یک کشت")
        self.assertContains(response, "سرویس‌دهنده همان منطقه")
        self.assertContains(response, "وام کشاورزی و اعتبار خرید نهاده")
        self.assertContains(response, "زمین شما، سرمایه و تخصص ما")
        self.assertContains(response, "https://sabzify.ir/")
        self.assertContains(response, "https://keshtdrip.ir/")
        self.assertContains(response, "https://keshthamrah.ir/")
        self.assertContains(response, "https://keshthami.ir/")
        self.assertContains(response, "https://keshtmosharekati.ir/")
        self.assertContains(response, "خدمات فضای سبز با سبزیفای")
        self.assertContains(response, "طراحی")
        self.assertContains(response, "روف گاردن")
        self.assertContains(response, "هرس درختان")
        self.assertContains(response, "خدمات")
        self.assertContains(response, "https://sabzify.ir/request/?service=design")
        self.assertContains(response, "https://sabzify.ir/request/?service=roof")
        self.assertContains(response, "https://sabzify.ir/request/?service=pruning")
        self.assertContains(response, "https://sabzify.ir/services/")
        self.assertContains(response, "لوازم آبیاری با کشت‌دریپ")
        self.assertContains(response, "لوله")
        self.assertContains(response, "نوار تیپ")
        self.assertContains(response, "اتصالات")
        self.assertContains(response, "https://keshtdrip.ir/shop/?category=layflat")
        self.assertContains(response, "https://keshtdrip.ir/shop/?category=drip-tape")
        self.assertContains(response, "https://keshtdrip.ir/shop/?category=pe-pipe")
        self.assertContains(response, "کودهای سبزیفای")
        self.assertContains(response, "کود هیومیک اسید")
        self.assertContains(response, "کود جلبک دریایی")
        self.assertContains(response, "https://sabzify.ir/shop/")
        self.assertContains(response, "https://sabzify.ir/shop/humic-acid/")
        self.assertContains(response, "/static/img/products/humic-acid.png")
        self.assertContains(response, "پربازدیدترین محصولات")
        self.assertContains(response, "لوله باغی / رول 200 متری")
        self.assertContains(response, "https://keshtdrip.ir/product/KSH-P-00000024/?variant=185")
        self.assertContains(response, "https://keshtdrip.ir/shop/")
        self.assertContains(response, "خدمات کشاورزی با کشت همراه")
        self.assertContains(response, "https://keshthamrah.ir/services/planting/")
        self.assertContains(response, "https://keshthamrah.ir/services/irrigation/")
        self.assertContains(response, "https://keshthamrah.ir/services/protection/")
        self.assertContains(response, "https://keshthamrah.ir/services/orchard/")
        self.assertContains(response, "https://keshthamrah.ir/services/machinery/")
        self.assertContains(response, "https://keshthamrah.ir/services/other/")
        self.assertNotContains(response, "برداشت گندم و جو")
        self.assertContains(response, "app.css")
        self.assertContains(response, 'dir="rtl"')
        self.assertNotContains(response, "cdn.tailwindcss.com")

    def test_register_login_profile_and_app_links(self):
        response = self.register()
        self.assertRedirects(response, reverse("home"))

        home = self.client.get(reverse("home"))
        self.assertContains(home, "علیرضا")
        self.assertContains(home, "https://sabzify.ir/")
        self.assertContains(home, "https://keshtmosharekati.ir/")

        profile = self.client.get(reverse("profile"))
        self.assertContains(profile, "09121112233")
        self.client.post(reverse("profile"), {"first_name": "علی", "last_name": "رضایی"})
        user = get_user_model().objects.get(phone="09121112233")
        self.assertEqual(user.get_full_name(), "علی رضایی")

        changed = self.client.post(
            reverse("password_change"),
            {
                "old_password": self.password,
                "new_password1": "Newer-pass-1841",
                "new_password2": "Newer-pass-1841",
            },
        )
        self.assertRedirects(changed, reverse("password_change_done"))

        self.client.post(reverse("logout"))
        self.assertRedirects(
            self.client.get(reverse("profile")),
            f"{reverse('login')}?next={reverse('profile')}",
        )
        logged_in = self.client.post(
            reverse("login"),
            {"username": "+989121112233", "password": "Newer-pass-1841"},
        )
        self.assertRedirects(logged_in, reverse("home"))

    def test_duplicate_phone_is_rejected(self):
        self.register()
        self.client.post(reverse("logout"))
        response = self.client.post(
            reverse("register"),
            {
                "phone": "09121112233",
                "first_name": "نفر",
                "last_name": "دوم",
                "password1": self.password,
                "password2": self.password,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "قبلاً ثبت‌نام شده")
        self.assertEqual(get_user_model().objects.count(), 1)
