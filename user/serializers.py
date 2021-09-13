from rest_framework import serializers

from user.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Serializer created to validate request parameters.
    """

    first_name = serializers.CharField(source="base_user.first_name")
    last_name = serializers.CharField(source="base_user.last_name")
    email = serializers.CharField(source="base_user.email")
    username = serializers.CharField(source="base_user.username")
    password = serializers.CharField(source="base_user.password")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password", "type")
