# apps/officer_auth/permissions.py
from rest_framework import permissions


class IsAdminRole(permissions.BasePermission):
    """
    Custom permission to only allow officers with role 'admin' to perform actions.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and has role 'admin'
        return (request.user.is_authenticated and
                hasattr(request.user, 'role') and
                request.user.role == 'admin')
