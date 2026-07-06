from django.contrib import admin
from django.urls import path, include

import applications
from core import views as core_views

urlpatterns = [
    path("", core_views.home, name="home"),
    path("admin/", admin.site.urls),
    path("applications/", include("applications.urls")),

]