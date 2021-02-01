from django.contrib import admin
from .models import *


# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title', )
    search_fields = ('title', )


admin.site.register(DataWidget)
admin.site.register(Page)
