from rest_framework.exceptions import ValidationError

from common.constants import ERROR, INVALID_USER
from user.models import User


def get_custom_user(base_user, target_user):
    user = User.objects.get(base_user=base_user)
    if user.type != target_user:
        raise ValidationError({ERROR: INVALID_USER})
    return user
