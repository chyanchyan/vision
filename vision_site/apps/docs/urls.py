from django.urls import path
from . import views

app_name = 'docs'
urlpatterns = [
    path(r'/^(\d+)/$', views.Docs, name='docs')
]