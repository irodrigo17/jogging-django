from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Jog


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def restore_object(self, attrs, instance=None):
            # call set_password on user object. Without this
            # the password will be stored in plain text.
            user = super(UserSerializer, self).restore_object(attrs, instance)
            user.set_password(attrs['password'])
            return user


class JogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jog
        fields = ('url', 'user', 'date', 'meters', 'seconds')
