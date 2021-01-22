from django.db import models
from ..data_structure import *


class MonitorData(models.Model):
    title = models.CharField(max_length=200, unique=True)
    sql_str = models.TextField()
    data_structure = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title