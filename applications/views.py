from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import ApplicationForm
from .geo import check_application_gps
from .models import Application

def index(request):
    return HttpResponse("FormStream: applications works")



def application_create(request):
    """Создание новой заявки через форму"""
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():

            application = form.save()

            check_application_gps(application)





            messages.success(request, f'Заявка #{application.id} успешно создана!')

            return redirect("applications:application_success", pk=application.id)
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = ApplicationForm()

    return render(request, "application_form.html", {"form": form})


def application_success(request, pk):
    application = Application.objects.get(pk=pk)
    return render(
        request,
        "applications/application_success.html",
        {"application": application}
    )