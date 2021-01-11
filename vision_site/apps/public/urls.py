
from django.urls import path

from . import views

app_name = 'public'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('data_monitor/', views.data_monitor, name='data_monitor'),

]

