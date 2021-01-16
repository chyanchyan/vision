from django.shortcuts import render
from .models import CashFlow
from django.core import serializers
from django.http import HttpResponse
from django.db.models import F, Q
from datetime import datetime as dt


def CashFlowView(req: HttpResponse) -> HttpResponse:
    template_name = 'widgets/crt_monthly_loan_ost.html'
    now = dt.now()
    sql = 'select * from cash_flow where date_time > convert(DATETIME, "%s")' \
          % ('-'.join([str(now.year), str(now.month), str(now.day)]))
    data = serializers.serialize("json", CashFlow.objects.raw(sql))
    context = {'data': data
               }

    return render(req, template_name, context=context)
