from django.db import models

from order.models import Address
from user.models import User


class Trip(models.Model):
    """
    Model created to store trip details.
    """

    trip_to = models.ForeignKey(
        Address, on_delete=models.DO_NOTHING, related_name="trip_on_to_address"
    )
    trip_from = models.ForeignKey(
        Address, on_delete=models.DO_NOTHING, related_name="trip_on_from_address"
    )
    traveler = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trips_of_traveler"
    )

    class Meta:
        db_table = "trip"
