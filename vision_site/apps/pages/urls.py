from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, {'page_name': ''}, name='home'),
    path('<str:page_name>', views.index, name='index'),
]