from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order.views import OrderViewSet, OfferViewSet

router = DefaultRouter()
router.register("orders", OrderViewSet, basename="orders")
router.register("offers", OfferViewSet, basename="offer")
urlpatterns = [
    path("", include(router.urls))
]
