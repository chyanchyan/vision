from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vision_site.apps.public.urls')),
    path('accounts/', include('vision_site.apps.accounts.urls')),
    path('data_monitor/', include('vision_site.apps.data_monitor.urls')),
]
