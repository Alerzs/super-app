from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django import forms

from .forms import parsed_phone
from .models import User


class AdminUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="رمز عبور", widget=forms.PasswordInput)
    password2 = forms.CharField(label="تکرار رمز عبور", widget=forms.PasswordInput)
    phone = forms.CharField(label="شماره همراه", max_length=20)

    class Meta:
        model = User
        fields = ("phone", "first_name", "last_name")

    def clean_phone(self):
        phone = parsed_phone(self.cleaned_data.get("phone"))
        if User.objects.filter(phone=phone).exists():
            raise ValidationError("با این شماره همراه قبلاً ثبت‌نام شده است.")
        return phone

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("رمز عبور و تکرار آن یکسان نیست.")
        return password2

    def clean(self):
        cleaned = super().clean()
        password = cleaned.get("password1")
        if password and cleaned.get("password2") == password:
            if cleaned.get("phone"):
                self.instance.phone = cleaned["phone"]
            validate_password(password, self.instance)
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AdminUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="رمز عبور")
    phone = forms.CharField(label="شماره همراه", max_length=20)

    class Meta:
        model = User
        fields = "__all__"

    def clean_password(self):
        return self.initial.get("password")

    def clean_phone(self):
        phone = parsed_phone(self.cleaned_data.get("phone"))
        if User.objects.exclude(pk=self.instance.pk).filter(phone=phone).exists():
            raise ValidationError("با این شماره همراه قبلاً ثبت‌نام شده است.")
        return phone


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm
    ordering = ("phone",)
    list_display = ("phone", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("phone", "first_name", "last_name")
    readonly_fields = ("date_joined", "last_login")
    filter_horizontal = ("groups", "user_permissions")
    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        ("پروفایل", {"fields": ("first_name", "last_name")}),
        (
            "دسترسی",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
        ("تاریخ", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("phone", "first_name", "last_name", "password1", "password2")},
        ),
    )
