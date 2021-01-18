from django.db import models


class CashFlow(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    amount = models.BigIntegerField()
    comments = models.CharField(max_length=500, blank=True)

    class Meta:
       db_table = 'cash_flow'

    def __str__(self):
        return 'cash flow %s' % str(self.date_time)
