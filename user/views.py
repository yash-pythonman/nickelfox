from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import CreateUserSerializer
from user.services import CreateUserService, UpdateProfileService


class SingUpView(APIView):
    """
    View created to handle http post request.
    """

    @staticmethod
    def post(request):
        payload = CreateUserSerializer(data=request.data)
        if payload.is_valid(raise_exception=True):
            return CreateUserService.execute(payload.validated_data)


class ProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        response = CreateUserSerializer(User.objects.get(base_user=request.user)).data
        response.pop("password")
        return Response(response)

    @staticmethod
    def patch(request):
        payload = CreateUserSerializer(data=request.data, partial=True)
        if payload.is_valid(raise_exception=True):
            return UpdateProfileService.execute({"payload": payload.validated_data, "user": request.user})
