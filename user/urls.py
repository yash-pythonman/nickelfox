from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user.views import SingUpView, ProfileView

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("singUp/", SingUpView.as_view(), name="sing_up"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
