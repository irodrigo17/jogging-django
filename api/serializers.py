from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Jog


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()

        return instance


class JogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jog
        fields = ('url', 'user', 'date', 'meters', 'seconds')
        extra_kwargs = {'user': {'read_only': True}}
