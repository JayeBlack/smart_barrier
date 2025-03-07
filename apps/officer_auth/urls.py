from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    CustomTokenBlacklistView,
    OfficerCreateView,
    OfficerRetrieveView,
    OfficerUpdateView,
    OfficerDeleteView,
)

# apps/officer_auth/urls.py
urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', CustomTokenBlacklistView.as_view(), name='token_blacklist'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('officers/', OfficerCreateView.as_view(), name='officer_create'),
    path('officers/<uuid:id>/retrieve/', OfficerRetrieveView.as_view(), name='officer_retrieve'),
    path('officers/<uuid:id>/update/', OfficerUpdateView.as_view(), name='officer_update'),
    path('officers/<uuid:id>/delete/', OfficerDeleteView.as_view(), name='officer_delete'),
]