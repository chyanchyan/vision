from django.db import models

class CashFlow(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    amount = models.BigIntegerField()
    comments = models.CharField(max_length=500)

    # class Meta:
    #     db_table = 'cash_flow'
