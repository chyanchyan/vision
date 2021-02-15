from django.urls import path
from . import views


urlpatterns = [
    path('', views.page_view, {'page_name': ''}, name='home'),
    path('<str:page_name>', views.page_view, {'page_name': '<str:page_name>'}, name='index'),
    path('display_meta/', views.display_meta, name='display_meta'),
]