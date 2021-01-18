from django.shortcuts import render
from .models import CashFlow
from django.core import serializers
from django.http import HttpResponse


def cash_flow_view(req: HttpResponse) -> HttpResponse:
    template_name = 'widgets/crt_monthly_loan_ost.html'
    table_name = req.GET['table_name']
    if table_name:
        try:
            sql = 'select * from %s' % table_name
            data = serializers.serialize("json", CashFlow.objects.raw(sql))
            context = {'data': data
                       }
        except:
            context = {'data': 'table name doesnt exist'}
    else:
        context = {'data': 'table name is empty'}

    return render(req, template_name, context=context)
