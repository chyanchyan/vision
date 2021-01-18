from django.shortcuts import render
from django.http import HttpResponse


def data_monitor(req: HttpResponse) -> HttpResponse:
    return render(req, 'data_monitor.html')
