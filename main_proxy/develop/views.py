from django.views import View

from develop.classes.botList import BotList
from develop.classes.BotId import BotId
from develop.classes.Register import Register
from develop.classes.Login import Login
from rest_framework.response import Response
from rest_framework.views import APIView

'''
Ядро

appId's:
2750bc42-702e-4cbe-bae5-798f171389e1
2850bc42-702e-4cbe-bae5-798f171389e2

Апи-метод в swagger:
http://core.webstktw.beget.tech/docs/?path=bot.yaml
'''


class BotListView(APIView):
    def get(self, request):
        status, data = BotList().send()
        print(status)
        print(data)
        return Response(status=status, data=data)


class BotIdView(APIView):
    def get(self, request):
        BotId().get_patch(1)
        return Response(BotId().send(1))


class RegisterView(APIView):
    def get(self, request):
        register = Register()
        data = request.query_params.dict()
        register.set_parameters(data)
        return Response(register.send())

class LoginView(APIView):
    def get(self, request):
        login = Login()
        data = request.query_params.dict()
        login.set_parameters(data)
        return Response(login.send())


