from rest_framework.viewsets import ViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BaseViewSet(ViewSet):
    """
    ViewSet created to authentication and permission validation.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
