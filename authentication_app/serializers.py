from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'password']

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            full_name=validated_data['full_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
