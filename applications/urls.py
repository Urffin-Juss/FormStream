from django.urls import path

from accounts import views

app_name = 'application'

urlpatterns = [

    path('', views.index, name='index'),


]