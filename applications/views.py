from django.http import HttpResponse


def index(request):
    return HttpResponse("FormStream: applications works")


