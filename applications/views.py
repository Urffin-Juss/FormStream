from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from . import form
from .form import ApplicationForm
from .models import Application

def index(request):
    return HttpResponse("FormStream: applications works")



def application_create(request):
    """Создание новой заявки через форму"""
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Здесь потом добавим проверку адресов через DaData
            application = form.save()
            messages.success(request, f'Заявка #{application.id} успешно создана!')
            return redirect('application_success', pk=application.id)
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = ApplicationForm()

    return render(request, "application_form.html", {"form": form})


def application_success(request, pk):
    """Страница успешного создания заявки"""
    application = Application.objects.get(pk=pk)
    return render(request, "application_form.html", {"form": form})