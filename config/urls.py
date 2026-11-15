from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "مدیریت کشتیار"
admin.site.site_title = "کشتیار"
admin.site.index_title = "مدیریت سامانه"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
]
