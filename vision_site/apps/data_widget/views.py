from django.shortcuts import render
from .models import CashFlow
from django.core import serializers


def CashFlowView(req):
    template_name = 'widgets/crt_monthly_loan_ost.html'
    date_time = CashFlow.objects
    amount = CashFlow.objects.values('amount')
    data = serializers.serialize('json', date_time)
    data2 = serializers.serialize('json', amount)
    return render(req, template_name, {'date_time': date_time, 'amount': data2})
