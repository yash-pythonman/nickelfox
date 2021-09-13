from rest_framework.response import Response
from common.base_views import BaseViewSet
from common.constants import SHOPPER, PUBLISHED, TRAVELER
from order.models import Order, Offer
from order.serializers import CreateOrderSerializer, OrderListSerializer, OrderDetailSerializer, OrderUpdateSerializer, \
    OfferSerializer, OfferListSerializer
from order.services import CreateOrderService, UpdateOrderService, CreateOfferService
from user.models import User
from user.utils import get_custom_user


class OrderViewSet(BaseViewSet):
    """
    View set created to handle http POST, GET, PATCH method.
    """

    @staticmethod
    def create(request):
        """
        Method implemented to handle http post method and create record.
        """
        payload = CreateOrderSerializer(data=request.data)
        if payload.is_valid(raise_exception=True):
            return CreateOrderService.execute(
                {"payload": payload.validated_data, "user": request.user}
            )

    @staticmethod
    def list(request):
        """
        Method implemented to handle http GET request and provide orders list.
        """
        user = User.objects.get(base_user=request.user)
        if user.type == SHOPPER:
            return Response(OrderListSerializer(Order.objects.filter(shopper=user), many=True).data)
        return Response(OrderListSerializer(Order.objects.filter(state=PUBLISHED), many=True).data)

    @staticmethod
    def retrieve(_, pk):
        return Response(OrderDetailSerializer(Order.objects.get(id=pk)).data)

    @staticmethod
    def update(request, pk):
        payload = OrderUpdateSerializer(data=request.data, partial=True)
        if payload.is_valid(raise_exception=True):
            return UpdateOrderService.execute({"payload": payload.validated_data, "pk": pk})


class OfferViewSet(BaseViewSet):
    """
    ViewSet created to handle http POST, GET, PUT method.
    """

    @staticmethod
    def create(request):
        payload = OfferSerializer(data=request.data)
        if payload.is_valid(raise_exception=True):
            return CreateOfferService.execute(
                {"payload": payload.validated_data, "traveler": get_custom_user(request.user, TRAVELER)})

    @staticmethod
    def list(request):
        return Response(OfferListSerializer(Offer.objects.filter(), many=True).data)
