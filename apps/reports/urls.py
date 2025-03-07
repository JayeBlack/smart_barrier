# apps/reports/urls.py
from django.urls import path
from .views import (
    ReportCreateView,
    ReportRetrieveView,
    ReportUpdateView,
    ReportDeleteView,
)

urlpatterns = [
    path('', ReportCreateView.as_view(), name='report_create'),
    path('<uuid:id>/retrieve/', ReportRetrieveView.as_view(), name='report_retrieve'),
    path('<uuid:id>/update/', ReportUpdateView.as_view(), name='report_update'),
    path('<uuid:id>/delete/', ReportDeleteView.as_view(), name='report_delete'),
]