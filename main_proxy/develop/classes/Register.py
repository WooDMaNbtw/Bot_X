from develop.routes import Route
from rest_framework.response import Response
from rest_framework.views import APIView


class Register(Route, APIView):

    def get(self, request):
        self.set_parameters(request.data)
        return super().get(request)

    def set_parameters(self, data):
        return super().set_parameters(data)

    def get_method(self):
        return "POST"

    def get_patch(self, id=""):
        return "/users/register"
