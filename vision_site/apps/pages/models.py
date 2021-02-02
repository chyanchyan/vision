from django.db import models
# Create your models here.


class DataWidget(models.Model):
    widget_id = models.CharField(max_length=50, unique=True, null=True)
    title = models.CharField(max_length=50, unique=True, null=True)
    js_name = models.CharField(max_length=1000, unique=True)
    python_script = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.widget_id


class Page(models.Model):
    title = models.CharField(max_length=100)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)
    widgets = models.ManyToManyField(DataWidget, blank=True)

    def __str__(self):
        return self.title



