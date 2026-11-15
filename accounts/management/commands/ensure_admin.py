import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from accounts.phones import normalize_phone


class Command(BaseCommand):
    help = "اگر DJANGO_SUPERUSER_PHONE تازه باشد، یک مدیر کل می‌سازد."

    def handle(self, *args, **options):
        raw = (
            os.environ.get("DJANGO_SUPERUSER_PHONE", "").strip()
            or os.environ.get("DJANGO_SUPERUSER_USERNAME", "").strip()
        )
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "")
        if not raw or not password:
            self.stdout.write("DJANGO_SUPERUSER_PHONE is unset; skipping.")
            return
        try:
            phone = normalize_phone(raw)
        except ValueError as exc:
            raise CommandError(str(exc)) from exc
        User = get_user_model()
        if User.objects.filter(phone=phone).exists():
            self.stdout.write(f"{phone} already exists; password and role left unchanged.")
            return
        name = os.environ.get("DJANGO_SUPERUSER_NAME", "مدیر کل").strip()
        first_name, _, last_name = name.partition(" ")
        User.objects.create_superuser(
            phone,
            password,
            first_name=first_name,
            last_name=last_name,
        )
        self.stdout.write(self.style.SUCCESS(f"Created superuser {phone}."))
