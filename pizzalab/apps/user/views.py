from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from user import permissions as user_permissions
from user import serializers


class BaseUserAPIView(generics.GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class UserListCreateView(generics.ListCreateAPIView, BaseUserAPIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return user_permissions.AdminOrDeny(),
        return permissions.AllowAny(),

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.UserCreateSerializer
        return super().get_serializer_class()


class UserRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView,
    BaseUserAPIView
):
    permission_classes = (user_permissions.UserPermission,)
