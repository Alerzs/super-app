from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeDoneView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import LoginForm, ProfileForm, RegisterForm, StyledPasswordChangeForm


class PhoneLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site_name"] = settings.SITE_NAME
        return context

    def form_valid(self, form):
        messages.success(self.request, "خوش آمدید.")
        return super().form_valid(form)


class PhonePasswordChangeView(PasswordChangeView):
    template_name = "accounts/password_change.html"
    form_class = StyledPasswordChangeForm
    success_url = reverse_lazy("password_change_done")


class PhonePasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"


def home(request):
    return render(request, "accounts/home.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        messages.success(request, "حساب شما ساخته شد.")
        return redirect("home")
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "پروفایل ذخیره شد.")
        return redirect("profile")
    return render(request, "accounts/profile.html", {"form": form})
