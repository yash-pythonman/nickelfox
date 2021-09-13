from rest_framework import serializers

from order.serializers import AddressSerializer
from trip.models import Trip


class TripSerializer(serializers.ModelSerializer):
    """
    Serializer created to validate payload for trip.
    """

    trip_to = AddressSerializer()
    trip_from = AddressSerializer()

    class Meta:
        model = Trip
        fields = ("trip_to", "trip_from")


class TripListSerializer(serializers.ModelSerializer):
    """
    Serializer created to validate payload for trip.
    """

    trip_to = AddressSerializer()
    trip_from = AddressSerializer()

    class Meta:
        model = Trip
        fields = ("id", "trip_to", "trip_from")
