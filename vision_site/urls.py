from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vision_site.apps.pages.urls')),
    path('accounts/', include('vision_site.apps.accounts.urls')),
]
