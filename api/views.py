from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.serializers import UserSerializer, JogSerializer
from api.models import Jog
from api.permissions import UserPermission, JogPermission


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]


class JogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jogs to be viewed or edited.
    """
    queryset = Jog.objects.all()
    serializer_class = JogSerializer
    permission_classes = [JogPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Jog.objects.filter(user=self.request.user)
