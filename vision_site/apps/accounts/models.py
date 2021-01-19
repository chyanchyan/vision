from django.db import models
from django.contrib.auth.models import User
from ..data_monitor.models import DashBoard


class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=1)
    normalized_name = models.CharField(max_length=64, unique=1)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_full_name_displayed = models.BooleanField(default=1)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=1, null=1)
    dashboards = models.ManyToManyField(DashBoard, blank=1)

