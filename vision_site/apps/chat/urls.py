import os
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from . import views
from ...settings import STATICFILES_DIRS
from django.views.generic import TemplateView


app_name = 'chat'
urlpatterns = [
    path('talk/', views.TalkMain.as_view(), name='talk'),
    path('messages/', views.TalkMessages.as_view(), name='messages'),
    url(r'^static/(?P<path>.*)$',
        serve,
        {'document_root': STATICFILES_DIRS[0], 'show_indexes': True},
        name='static'
        )
]