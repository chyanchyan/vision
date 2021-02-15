from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from .models import Page
from django.http.response import HttpResponse
from ..data_structure.models import ExternalLink
from django_pandas.io import read_frame

# imports for exec
import pandas as pd
from pandas import DataFrame as dtf
import numpy as np
from collections import Counter
from datetime import datetime as dt
import json

from ..data_structure.models import *


def page_view(req, page_name):
    page_name = '/' + page_name
    pg = get_object_or_404(Page, permalink=page_name)
    widgets = model_to_dict(Page.objects.get(permalink=page_name))['widgets']
    widgets = {
        widget.widget_id:
            {'data': py(widget.python_script),
             'widget_id': widget.widget_id,
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
        'widgets': widgets,
        'external_links': ExternalLink.objects.all(),
    }

    # assert False
    return render(req, 'pages/page.html', context=context)


def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def json_to_view(data):
    s = data.to_json()
    f = open('re.txt', 'w+')
    f.write(s)
    f.close()


def py(script_str):

    exec(script_str, globals())

    f = open('re.txt', 'r')

    return f.readlines()[0]
