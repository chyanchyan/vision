from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vision.apps.public.urls')),
    path('accounts/', include('vision.apps.accounts.urls')),
    path('data_monitor/', include('vision.apps.data_monitor.urls')),
]
