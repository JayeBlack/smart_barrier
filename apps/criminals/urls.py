# apps/criminals/urls.py
from django.urls import path
from .views import (
    CriminalRecordCreateView,
    CriminalRecordRetrieveView,
    CriminalRecordUpdateView,
    CriminalRecordDeleteView,
)

urlpatterns = [
    path('', CriminalRecordCreateView.as_view(), name='criminal_create'),
    path('<uuid:id>/retrieve/', CriminalRecordRetrieveView.as_view(), name='criminal_retrieve'),
    path('<uuid:id>/update/', CriminalRecordUpdateView.as_view(), name='criminal_update'),
    path('<uuid:id>/delete/', CriminalRecordDeleteView.as_view(), name='criminal_delete'),
]
