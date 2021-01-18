from django.shortcuts import render
from django.http import HttpResponse


def control_panel(req: HttpResponse) -> HttpResponse:
    return render(req, 'control_panel.html')
