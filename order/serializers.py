from rest_framework import serializers

from common.constants import PUBLISHED, REQUESTED, IN_TRANSIT, RECEIVED, INACTIVE
from order.models import Address, Order, Offer


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer created to validate request payload for address.
    """

    class Meta:
        model = Address
        fields = ("house_number", "street", "city", "state", "country", "pin_code")


class CreateOrderSerializer(serializers.ModelSerializer):
    """
    Serializer created to validate request payload for order.
    """

    order_to = AddressSerializer()
    order_from = AddressSerializer()

    class Meta:
        model = Order
        fields = (
            "product_name",
            "actual_price",
            "selling_price",
            "order_to",
            "order_from",
        )


class OrderListSerializer(serializers.ModelSerializer):
    """
    Serializer created for order list response.
    """

    class Meta:
        model = Order
        fields = ("id", "state", "product_name", "selling_price")


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    Serializer created for order detail response.
    """
    order_to = AddressSerializer()
    order_from = AddressSerializer()

    class Meta:
        model = Order
        fields = ("id", "state", "product_name", "selling_price", "order_to", "order_from")


class OrderUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer created to validate payload for update order.
    """
    order_to = AddressSerializer()
    order_from = AddressSerializer()
    state = serializers.ChoiceField(choices=(
        (PUBLISHED, PUBLISHED), (REQUESTED, REQUESTED), (IN_TRANSIT, IN_TRANSIT), (RECEIVED, RECEIVED),
        (INACTIVE, INACTIVE)))

    class Meta:
        model = Order
        fields = ("state", "product_name", "selling_price", "order_to", "order_from")


class OfferSerializer(serializers.ModelSerializer):
    """
    Serializer created to validate payload for create offers.
    """

    class Meta:
        model = Offer
        fields = ("order", "price")


class OfferListSerializer(serializers.ModelSerializer):
    """
    Serializer created to provide offer list response.
    """

    class Meta:
        model = Offer
        fields = ("id", "order", "price", "traveler", "status")
