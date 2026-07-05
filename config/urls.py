

from django.contrib import admin
from django.urls import path, include

import applications

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applications/', include("applications.urls", namespace="applications")),
    path('views/', include("core.views.urls", namespace="core.views")),
]
