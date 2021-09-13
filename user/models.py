from django.contrib.auth.models import User as BaseUser
from django.db import models

from common.constants import SHOPPER, TRAVELER


class User(models.Model):
    """
    Model created to store costume user details.
    """

    USER_TYPE = ((TRAVELER, TRAVELER), (SHOPPER, SHOPPER))
    base_user = models.OneToOneField(
        BaseUser, on_delete=models.CASCADE, related_name="user_on_auth_user"
    )
    type = models.CharField(choices=USER_TYPE, max_length=25)

    class Meta:
        db_table = "user"


class ChatRoom(models.Model):
    """
    Model created to store chat room details.
    """

    user_1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chat_rooms_of_user_1"
    )
    user_2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chat_rooms_of_user_2"
    )

    class Meta:
        db_table = "chat_room"
        unique_together = ("user_1", "user_2")


class Message(models.Model):
    """
    Model created to store message details.
    """

    chat_room = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE, related_name="message_in_chat_room"
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_of_sender"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_of_receiver"
    )
    message = models.CharField(max_length=255)

    class Meta:
        db_table = "message"


class Notification(models.Model):
    """
    Model created to store notification details.
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications_for_user"
    )
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = "notification"
