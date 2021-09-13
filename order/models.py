from django.db import models
from django_fsm import FSMField, transition
from djmoney.models.fields import MoneyField

from common.constants import (IN_TRANSIT, INACTIVE, PUBLISHED, RECEIVED,
                              REQUESTED, UNPUBLISHED, PENDING, ACCEPT, CANCEL)
from user.models import User


class Address(models.Model):
    """
    Model created to store to and from address.
    """

    house_number = models.SmallIntegerField(null=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=10)

    class Meta:
        db_table = "address"


class Order(models.Model):
    """
    Model created to store product details.
    """

    product_name = models.CharField(max_length=255)
    actual_price = MoneyField(
        max_digits=10, decimal_places=2, null=True, default_currency=None
    )
    selling_price = MoneyField(
        max_digits=10, decimal_places=2, default_currency="INR"
    )
    order_to = models.ForeignKey(
        Address, on_delete=models.DO_NOTHING, related_name="order_on_to_address"
    )
    order_from = models.ForeignKey(
        Address, on_delete=models.DO_NOTHING, related_name="order_on_from_address"
    )
    state = FSMField(default=UNPUBLISHED)
    shopper = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders_of_shopper"
    )
    traveler = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders_of_traveler", null=True
    )

    class Meta:
        db_table = "order"

    @transition(field=state, source=UNPUBLISHED, target=PUBLISHED)
    def published(self):
        """
        Method created to change state unpublished to published.
        """
        pass

    @transition(field=state, source=PUBLISHED, target=REQUESTED)
    def requested(self):
        """
        Method created to change state published to requested.
        """
        pass

    @transition(field=state, source=REQUESTED, target=IN_TRANSIT)
    def in_transit(self):
        """
        Method created to change state requested to in_transit.
        """
        pass

    @transition(field=state, source=IN_TRANSIT, target=RECEIVED)
    def received(self):
        """
        Method created to change state in_transit to received.
        """
        pass

    @transition(field=state, source=RECEIVED, target=INACTIVE)
    def inactive(self):
        """
        Method created to change state received to inactive.
        """
        pass


class Offer(models.Model):
    """
    Model create to record offer details.
    """
    STATUS_CHOICES = [(PENDING, PENDING), (ACCEPT, ACCEPT), (CANCEL, CANCEL)]
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="offers_on_order"
    )
    traveler = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="offers_by_traveler"
    )
    price = MoneyField(
        max_digits=10, decimal_places=2, null=True, default_currency="INR"
    )
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=PENDING)

    class Meta:
        db_table = "offer"
        unique_together = ("order", "traveler")
