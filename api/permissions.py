from rest_framework.permissions import BasePermission

class IsAdminOrOwner(BasePermission):
    def has_permission(self, request, view):
        print(f"User: {request.user}, is_owner: {getattr(request.user, 'is_owner', False)}")
        return request.user.is_authenticated and ( request.user.is_staff or getattr(request.user, 'is_owner', False))
