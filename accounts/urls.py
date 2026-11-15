from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (
    PhoneLoginView,
    PhonePasswordChangeDoneView,
    PhonePasswordChangeView,
    home,
    profile,
    register,
)

urlpatterns = [
    path("", home, name="home"),
    path("login/", PhoneLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("profile/password/", PhonePasswordChangeView.as_view(), name="password_change"),
    path(
        "profile/password/done/",
        PhonePasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
