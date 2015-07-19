from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, JogSerializer
from api.models import Jog


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class JogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jogs to be viewed or edited.
    """
    queryset = Jog.objects.all()
    serializer_class = JogSerializer
