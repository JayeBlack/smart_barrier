# apps/checkpoints/urls.py
from django.urls import path
from .views import (
    CheckpointLogCreateView,
    CheckpointLogRetrieveView,
    CheckpointLogUpdateView,
    CheckpointLogDeleteView,
)

urlpatterns = [
    path('', CheckpointLogCreateView.as_view(), name='checkpoint_create'),
    path('<uuid:id>/retrieve/', CheckpointLogRetrieveView.as_view(), name='checkpoint_retrieve'),
    path('<uuid:id>/update/', CheckpointLogUpdateView.as_view(), name='checkpoint_update'),
    path('<uuid:id>/delete/', CheckpointLogDeleteView.as_view(), name='checkpoint_delete'),
]