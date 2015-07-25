from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def is_open_view(self, view):
        return view.action in ['create', 'retrieve']

    def is_staff(self, request):
        return request.user and request.user.is_authenticated() and request.user.is_staff

    def has_permission(self, request, view):
        return self.is_open_view(view) or self.is_staff(request)

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user


class JogPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user
