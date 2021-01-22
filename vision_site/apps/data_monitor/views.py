from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers


def monitor_view(req):
    context = {}

    # assert False
    return render(req, 'data_monitors/data_monitor.html', context=context)
