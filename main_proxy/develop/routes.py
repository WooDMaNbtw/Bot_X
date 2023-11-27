from django.shortcuts import render

# Create your views here.
from abc import ABC, abstractmethod
from django.http import JsonResponse

import requests


class RouteTemplate(ABC):

    def set_parameters(self, data):
        self.parameters = data
        print(self.parameters)

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


class Route(RouteTemplate):

    def __init__(self):
        self.parameters = []
        self.response = []
        self.APP_ID = '2750bc42-702e-4cbe-bae5-798f171389e1'
        self.BASE_URL = 'http://core.webstktw.beget.tech/api/v0/apps/'
        # self.BASE_URL = "http://127.0.0.1:8000/api/v0/apps/"
        # self.APP_ID = "123-456-789-000"

    def send(self, id=""):
        url = f'{self.BASE_URL}{self.APP_ID}'
        print(self.get_patch())
        response = requests.request(self.get_method(), f"{url}{self.get_patch(id)}", params=self.get_parameters())
        self.set_response(response.json())
        return self.get_response()




