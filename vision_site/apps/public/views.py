from django.shortcuts import render
from django.http import HttpResponse


def index(req: HttpResponse) -> HttpResponse:
    return render(req, 'index.html')


def data_monitor(req: HttpResponse) -> HttpResponse:
    return render(req, 'data_monitor.html')


def uploading(req: HttpResponse) -> HttpResponse:
    return render(req, 'uploading.html')


def calendar(req: HttpResponse) -> HttpResponse:
    return render(req, 'calendar.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
