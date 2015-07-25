from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.serializers import UserSerializer, JogSerializer
from api.models import Jog
from api.permissions import IsStaffOrTargetUser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return [(AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser())]


class JogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jogs to be viewed or edited.
    """
    queryset = Jog.objects.all()
    serializer_class = JogSerializer
