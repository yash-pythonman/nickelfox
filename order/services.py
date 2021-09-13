from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from service_objects.services import Service
from django_fsm import TransitionNotAllowed
from common.constants import SHOPPER, MESSAGE, ORDER_CREATED, ORDER_UPDATED, ERROR, INVALID_TRANSITION, OFFER_CREATED, \
    INVALID_OFFER_REQUEST
from order.models import Order, Address, Offer
from user.utils import get_custom_user
from rest_framework import status


class CreateOrderService(Service):
    """
    Service created to insert record in order table.
    """

    def process(self):
        Order.objects.create(
            order_to=Address.objects.create(**self.data["payload"].pop("order_to")),
            order_from=Address.objects.create(**self.data["payload"].pop("order_from")),
            shopper=get_custom_user(self.data.pop("user"), SHOPPER),
            **self.data["payload"]
        )
        return Response({MESSAGE: ORDER_CREATED}, status=status.HTTP_201_CREATED)


class UpdateOrderService(Service):
    """
    Service created to update order.
    """

    def process(self):
        try:
            order = Order.objects.get(id=self.data.pop("pk"))
            for key, value in self.data["payload"].items():
                if key == "state":
                    order.__getattribute__(value.lower())()
                    continue
                elif key == "order_to":
                    Address.objects.filter(order_on_to_address__in=[order]).update(**value)
                    continue
                elif key == "order_from":
                    Address.objects.filter(order_on_from_address__in=[order]).update(**value)
                    continue
                order.__setattr__(key, value)
            order.save()
            return Response({MESSAGE: ORDER_UPDATED})
        except TransitionNotAllowed:
            raise ValidationError({ERROR: INVALID_TRANSITION})


class CreateOfferService(Service):
    """
    Service created to insert offer details into DB.
    """
    def process(self):
        try:
            Offer.objects.create(**self.data.pop("payload"), **self.data)
            return Response({MESSAGE: OFFER_CREATED}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            raise ValidationError({ERROR: INVALID_OFFER_REQUEST})
