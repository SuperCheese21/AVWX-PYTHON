from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("api/", include("app.airports.urls")),
    path("admin/", admin.site.urls),
    re_path(r"", TemplateView.as_view(template_name="index.html"))
]
