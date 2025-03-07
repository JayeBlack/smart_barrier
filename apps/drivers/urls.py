# apps/drivers/urls.py
from django.urls import path
from .views import (
    DriverCreateView,
    DriverRetrieveView,
    DriverUpdateView,
    DriverDeleteView,
)

urlpatterns = [
    path('', DriverCreateView.as_view(), name='driver_create'),
    path('<uuid:id>/retrieve/', DriverRetrieveView.as_view(), name='driver_retrieve'),
    path('<uuid:id>/update/', DriverUpdateView.as_view(), name='driver_update'),
    path('<uuid:id>/delete/', DriverDeleteView.as_view(), name='driver_delete'),
]