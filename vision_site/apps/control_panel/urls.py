from django.urls import path
from . import views

app_name = 'control_panel'
urlpatterns = [
    path('control_panel/', views.control_panel, name='control_panel'),
]
