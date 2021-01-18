from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=100)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('page content', blank=True)

    def __str__(self):
        return self.title