from django.urls import path
from . import views

app_name = "applications"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.application_create, name="application_create"),
    path("success/<int:pk>/", views.application_success, name="application_success",)


]