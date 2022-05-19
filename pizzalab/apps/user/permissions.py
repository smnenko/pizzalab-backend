from rest_framework import permissions


class AdminOrDeny(permissions.BasePermission):

    def has_permission(self, request, view):
        return False or request.user.is_staff


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated or request.user.is_staff
        elif request.method in ('GET', 'PUT', 'PATCH', 'DELETE'):
            return request.user.is_authenticated
        return False

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff
