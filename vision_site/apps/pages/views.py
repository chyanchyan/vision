from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from .models import Page
from django.core import serializers
import json
from django.db import connection as conn
from ..data_structure.models import *


def page_view(req, page_name):
    page_name = '/' + page_name
    pg = get_object_or_404(Page, permalink=page_name)
    widgets = model_to_dict(Page.objects.get(permalink=page_name))['widgets']
    widgets = {
        widget.name:
            {'data': py(widget.python_script),
             'title': widget.title,
             'js_name': widget.js_name,
             'comments': widget.comments,
             }
        for widget in widgets
    }
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        'widgets': widgets
    }

    # assert False
    return render(req, 'pages/page.html', context=context)


def py(script_str):

    exec(script_str, globals())

    f = open('re.txt', 'r')

    return f.readlines()[0]
