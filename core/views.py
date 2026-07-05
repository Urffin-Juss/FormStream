from django.shortcuts import render
from django.http import HttpResponse



def home_html_view(request):
    context = {'title': 'Главная страница'}
    return render(request, 'core/home.html', context)

