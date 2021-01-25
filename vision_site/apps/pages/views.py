from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from .models import Page, ExternalLink
from django.core import serializers
from ..data_structure.models import *


def page_view(req, page_name):
    page_name = '/' + page_name
    pg = get_object_or_404(Page, permalink=page_name)
    widgets = model_to_dict(Page.objects.get(permalink=page_name))['widgets']
    data = {
        'data_' + value.name:
            serializers.serialize("json", eval('%s.objects.all()' % value.class_name))
        for value in widgets
    }

    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }

    for key, value in data.items():
        context[key] = value

    # assert False

    if page_name == '/':
        context['external_links'] = ExternalLink.objects.all()
        return render(req, 'pages/homepage.html', context=context)
    else:
        return render(req, 'pages/page.html', context=context)

