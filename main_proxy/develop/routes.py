from django.shortcuts import render

# Create your views here.
from abc import ABC, abstractmethod
from django.http import JsonResponse

import requests
from rest_framework.response import Response


class RouteTemplate(ABC):

    def set_parameters(self, data):
        self.parameters = data

    def get_parameters(self):
        return self.parameters

    def set_response(self, data):
        self.response = data

    def get_response(self):
        return self.response

    @abstractmethod
    def send(self):
        pass

    def get_patch(self):
        pass

    def get_method(self):
        pass

    def success(self):
        pass

    def error(self):
        pass


class Route(RouteTemplate):

    def get(self, request):
        # print(request)
        return Response(status=self.send()[0], data=self.send()[1])

    def __init__(self):
        self.parameters = []
        self.response = []
        # self.APP_ID = '2750bc42-702e-4cbe-bae5-798f171389e1'
        # self.BASE_URL = 'http://core.webstktw.beget.tech/api/v0/apps/'
        self.BASE_URL = "http://127.0.0.1:5000/api/v0/apps/"
        self.APP_ID = "123-456-789-000"

    def send(self, id=""):

        url = f'{self.BASE_URL}{self.APP_ID}'
        response = requests.request(self.get_method(), f"{url}{self.get_patch(id)}", json=self.get_parameters())

        self.set_response(response.json())

        new_response = None

        if 200 <= response.status_code < 300:
            new_response = self.success(self.get_response())

        if 400 <= response.status_code <= 500:
            new_response = self.error(self.get_response())

        if new_response is None:
            new_response = response

        return response.status_code, new_response

    def success(self, response):
        return response

    def error(self, response):
        return response





