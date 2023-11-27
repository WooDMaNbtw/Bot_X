from django.contrib import admin
from django.urls import path, include
from .views import UserDataAPIView, RegisterAPIView, LoginAPIView
# from .views_2 import BotView

urlpatterns = [
    path("api/v0/apps/123-456-789-000/users/register", RegisterAPIView.as_view(), name="register"),
    path("api/v0/apps/123-456-789-000/users/login", LoginAPIView.as_view(), name="login"),
    path("api/v0/apps/123-456-789-000/users", UserDataAPIView.as_view(), name='users'),
]
