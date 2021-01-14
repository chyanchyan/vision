from django.urls import path
from . import views

app_name = 'data_widget'
urlpatterns = [
    path('', views.CashFlowView, name='data_widget')
]