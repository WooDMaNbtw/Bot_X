import datetime
from django.utils import timezone
from django.views import View
from django.views.generic import UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import User
# from .routes import *
from .serializers import UserSerializer
from django.middleware.csrf import get_token


class UserDataAPIView(APIView):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)


class RegisterAPIView(APIView):
    def get(self, request):
        return Response({"notification": "Register view is not necessary here!"})

    def post(self, request):
        email, password, created_at = request.data["email"], request.data["password"], datetime.datetime.utcnow().isoformat()
        print(email, password)
        if email == "admin@admin.ru" and password == "qwerty123456":
            user = User.objects.get_or_create(email=email, defaults={"password": password, "created_at": created_at})[0]
            serializer = UserSerializer(user)

            response = {
                "status": status.HTTP_200_OK,
                "user_id": serializer.data.get("id"),
                "created_at": user.created_at
            }

        else:
            response = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": "Bad email"
            }

        return Response(response)


class LoginAPIView(APIView):
    def get(self, request):
        return Response({"notification": "Login view is not necessary here!"})

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        if email == "admin@admin.ru" and password == "qwerty123456":
            response = {
                "status": status.HTTP_200_OK,
                "access_token": "abcd",
                "created_at": User.objects.get(email=email).created_at
            }

        elif email == "admin" and password == "qwerty123456":
            response = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": "Bad email"
            }

        else:
            response = {
                "status": status.HTTP_401_UNAUTHORIZED,
                "error": "Bad email or password"
            }

        return Response(response)

