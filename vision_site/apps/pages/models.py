from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=100)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title


class ExternalLink(models.Model):
    title = models.CharField(max_length=100)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.title
