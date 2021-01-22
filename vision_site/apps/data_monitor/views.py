from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ..data_structure.models import Data


def monitor_view(req):

    table_name = req.GET['table_name']
    if table_name:
        try:
            sql = 'select * from %s' % table_name
            data = serializers.serialize("json", data.objects.raw(sql))
            context = {'data': data
                       }
        except:
            context = {'data': 'table name doesnt exist'}
    else:
        context = {'data': 'table name is empty'}


    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }

    # assert False
    return render(req, 'data_monitors/data_monitor.html', context=context)
