from django.shortcuts import render
from .apps.data_widget.models import CashFlow
from django.core import serializers


def index(req):
    return render(req, 'index.html')