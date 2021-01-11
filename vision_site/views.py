from django.shortcuts import render


def index(req):
    return render(req, 'index.html')


def data_monitor(req):
    return render(req, 'data_monitor.html')


