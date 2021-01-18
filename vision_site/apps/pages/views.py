from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.


def index(req, page_name):
    page_name = '/' + page_name
    pg = get_object_or_404(Page, permalink=page_name)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }

    # assert False

    return render(req, 'pages/page.html', context=context)


