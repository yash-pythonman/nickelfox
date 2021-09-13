from rest_framework.routers import DefaultRouter

from trip.views import TripViewSet

router = DefaultRouter()
router.register("trips", TripViewSet, basename="trips")
urlpatterns = router.urls
