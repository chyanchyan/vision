from django.db import models


class InsAlias(models.Model):
    alias = models.CharField(max_length=200, unique=True)


class InsType(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Ins(models.Model):
    name = models.CharField(max_length=200, unique=True)
    alias = models.ForeignKey(InsAlias, on_delete=models.SET_NULL, blank=True, null=True)
    ins_type = models.ForeignKey(InsType, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)


class Account(models.Model):
    name = models.CharField(max_length=200, unique=True)
    account_number = models.CharField(blank=True)


class CashFlow(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    amount = models.DecimalField()
    account = models.OneToOneField(Account, on_delete=models.SET_NULL, blank=True)
    comments = models.CharField(max_length=500, blank=True)


class Balance(models.Model):
    date_time = models.DateTimeField()
    amount = models.DecimalField()


