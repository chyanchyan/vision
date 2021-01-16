from django.shortcuts import render
from django.http import HttpResponse


def Docs(req: HttpResponse) -> HttpResponse:
    return render(req, 'docs/docs.html')
