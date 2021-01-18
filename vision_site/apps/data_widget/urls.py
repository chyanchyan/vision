from django.urls import path
from . import views

app_name = 'data_widget'
urlpatterns = [
    path('', views.cash_flow_view, name='data_widget')
]