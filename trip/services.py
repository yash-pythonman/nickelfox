from rest_framework.response import Response
from service_objects.services import Service

from common.constants import TRIP_CREATED, MESSAGE
from order.models import Address
from trip.models import Trip


class CreateTripService(Service):
    """
    Service created to insert record in trip table.
    """

    def process(self):
        Trip.objects.create(trip_to=Address.objects.create(**self.data["payload"].get("trip_to")),
                            trip_from=Address.objects.create(**self.data["payload"].get("trip_from")),
                            traveler=self.data["user"])
        return Response({MESSAGE: TRIP_CREATED})
