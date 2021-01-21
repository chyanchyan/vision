from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'data_monitor'
urlpatterns = [
    path('data_monitor/', views.dash_board, name='dash_board'),
]
