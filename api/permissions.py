from rest_framework.permissions import BasePermission

class IsAdminOrOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and ( request.user.is_staff or getattr(request.user, 'is_owner', False))

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_owner', False)
