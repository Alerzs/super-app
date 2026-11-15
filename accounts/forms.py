from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django import forms

from .models import User
from .phones import normalize_phone


def parsed_phone(value):
    try:
        return normalize_phone(value)
    except ValueError as exc:
        raise ValidationError(str(exc)) from exc


class LoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "شماره همراه یا رمز عبور نادرست است.",
        "inactive": "این حساب غیرفعال است.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        phone = self.fields["username"]
        phone.max_length = 20
        phone.label = "شماره همراه"
        phone.widget.attrs.update(
            {
                "class": "field-input",
                "dir": "ltr",
                "inputmode": "tel",
                "autocomplete": "tel",
                "placeholder": "09123456789",
            }
        )
        self.fields["password"].label = "رمز عبور"
        self.fields["password"].widget.attrs.update(
            {
                "class": "field-input",
                "dir": "ltr",
                "autocomplete": "current-password",
            }
        )

    def clean_username(self):
        return parsed_phone(self.cleaned_data.get("username"))


class RegisterForm(forms.ModelForm):
    field_order = ["first_name", "last_name", "phone", "password1", "password2"]
    phone = forms.CharField(label="شماره همراه", max_length=20)
    password1 = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput,
        help_text="حداقل ۸ کاراکتر.",
    )
    password2 = forms.CharField(label="تکرار رمز عبور", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone")
        labels = {"first_name": "نام", "last_name": "نام خانوادگی"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs["class"] = "field-input"
        self.fields["phone"].widget.attrs.update(
            {
                "dir": "ltr",
                "inputmode": "tel",
                "autocomplete": "tel",
                "placeholder": "09123456789",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {"dir": "ltr", "autocomplete": "new-password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"dir": "ltr", "autocomplete": "new-password"}
        )
        self.fields["first_name"].widget.attrs["autocomplete"] = "given-name"
        self.fields["last_name"].widget.attrs["autocomplete"] = "family-name"

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
        for key in ("phone", "first_name", "last_name"):
            if cleaned.get(key) is not None:
                setattr(self.instance, key, cleaned.get(key))
        password = cleaned.get("password1")
        if password and cleaned.get("password2") == password:
            try:
                validate_password(password, self.instance)
            except ValidationError as exc:
                self.add_error("password1", exc)
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
        labels = {"first_name": "نام", "last_name": "نام خانوادگی"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "field-input"


class StyledPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].label = "رمز فعلی"
        self.fields["new_password1"].label = "رمز تازه"
        self.fields["new_password2"].label = "تکرار رمز تازه"
        for field in self.fields.values():
            field.widget.attrs.update({"class": "field-input", "dir": "ltr"})
        self.fields["old_password"].widget.attrs["autocomplete"] = "current-password"
        self.fields["new_password1"].widget.attrs["autocomplete"] = "new-password"
        self.fields["new_password2"].widget.attrs["autocomplete"] = "new-password"
