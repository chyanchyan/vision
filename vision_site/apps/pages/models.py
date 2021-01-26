from django.db import models

# Create your models here.


class DataWidget(models.Model):
    title = models.CharField(max_length=50, unique=True, null=True)
    js_name = models.CharField(max_length=1000, unique=True)
    data_structure_model_name = models.CharField(max_length=50, null=True)
    comments = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=100)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)
    widgets = models.ManyToManyField(DataWidget, blank=True)

    def __str__(self):
        return self.title


class ExternalLink(models.Model):
    title = models.CharField(max_length=100)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title

