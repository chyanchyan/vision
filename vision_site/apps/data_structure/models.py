from django.db import models


class Data(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class InsAlias(models.Model):
    alias = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.alias


class InsType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Ins(models.Model):
    name = models.CharField(max_length=200, unique=True)
    alias = models.ForeignKey(InsAlias, on_delete=models.SET_NULL, blank=True, null=True)
    ins_type = models.ForeignKey(InsType, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=200, unique=True)
    account_number = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return 'account: %s' % str(self.name)


class CashFlow(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    account = models.OneToOneField(Account, on_delete=models.SET_NULL, blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return 'cash flow: %s' % str(self.date_time)


class Balance(models.Model):
    date_time = models.DateTimeField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return 'balance: %s' % str(self.date_time)
