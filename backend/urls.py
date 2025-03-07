from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Root URL
    path('api/auth/', include('apps.officer_auth.urls')),
    path('vehicles/', include('apps.vehicles.urls')),
    path('drivers/', include('apps.drivers.urls')),
    path('checkpoints/', include('apps.checkpoints.urls')),
    path('criminals/', include('apps.criminals.urls')),
    path('reports/', include('apps.reports.urls')),
]
