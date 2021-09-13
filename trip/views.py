from rest_framework.response import Response

from common.base_views import BaseViewSet
from common.constants import TRAVELER
from trip.models import Trip
from trip.serializers import TripSerializer, TripListSerializer
from trip.services import CreateTripService
from user.utils import get_custom_user


class TripViewSet(BaseViewSet):
    """
    ViewSet created handle http POST, GET, PATCH methods.
    """

    @staticmethod
    def create(request):
        """
        Method created to handle http POST method and create trip.
        """
        payload = TripSerializer(data=request.data)
        if payload.is_valid(raise_exception=True):
            return CreateTripService.execute(
                {"payload": payload.validated_data, "user": get_custom_user(request.user, TRAVELER)}
            )

    @staticmethod
    def list(request):
        """
        Method created to handle http GET method and provide the list of trips.
        """
        return Response(TripListSerializer(Trip.objects.filter(traveler__base_user=request.user), many=True).data)
