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


class IsSelfOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow officers to access their own data, or admins to access any officer's data.
    """

    def has_object_permission(self, request, view, obj):
        # Allow access if the user is the officer themselves or an admin
        return (request.user.is_authenticated and
                (obj == request.user or
                 (hasattr(request.user, 'role') and request.user.role == 'admin')))
