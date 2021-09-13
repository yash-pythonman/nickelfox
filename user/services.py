from django.contrib.auth.models import User as BaseUser
from django.db import IntegrityError
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from service_objects.services import Service

from common.constants import ERROR, MESSAGE, USER_CREATED, USERNAME_ALREADY_EXIST, USER_UPDATED
from user.models import User


class CreateUserService(Service):
    """
    Service created to insert record in user table.
    """

    def process(self):
        try:
            User.objects.create(
                type=self.data.pop("type"),
                base_user=BaseUser.objects.create_user(**self.data.pop("base_user")),
            )
        except IntegrityError:
            raise ValidationError({ERROR: USERNAME_ALREADY_EXIST})

        return Response({MESSAGE: USER_CREATED}, status=status.HTTP_201_CREATED)


class UpdateProfileService(Service):
    """
    Service created to update user profile.
    """

    def process(self):
        try:
            user = self.data.pop("user")
            payload = self.data.pop("payload")
            for key, value in payload.pop("base_user").items():
                if key == "password":
                    user.set_password(value)
                    continue
                user.__setattr__(key, value)
            user.save()
            User.objects.filter(base_user=user).update(**payload)
        except IntegrityError:
            raise ValidationError({ERROR: USERNAME_ALREADY_EXIST})
        return Response({MESSAGE: USER_UPDATED})
