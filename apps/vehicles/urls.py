# apps/vehicles/urls.py
from django.urls import path
from .views import (
    VehicleCreateView,
    VehicleRetrieveView,
    VehicleUpdateView,
    VehicleDeleteView,
)

urlpatterns = [
    path('', VehicleCreateView.as_view(), name='vehicle_create'),
    path('<str:plate_number>/retrieve/', VehicleRetrieveView.as_view(), name='vehicle_retrieve'),
    path('<str:plate_number>/update/', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('<str:plate_number>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),
]