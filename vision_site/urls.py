from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vision_site.apps.pages.urls')),
    path('accounts/', include('vision_site.apps.accounts.urls')),
    path('control_panel/', include('vision_site.apps.control_panel.urls')),
    path('docs/', include('vision_site.apps.docs.urls')),
]
