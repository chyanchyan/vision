from django.contrib import admin

# Register your models here.
from .models import UserPersona, UserProfile

admin.site.register(UserPersona)
admin.site.register(UserProfile)
