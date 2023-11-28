from django.urls import path, include

from .classes.botList import BotList
from .classes.Register import Register
from .classes.Login import Login

from .views import BotListView, BotIdView, RegisterView, LoginView

urlpatterns = [
    path("api/v0/bots", BotList().as_view()),
    path("proxy/data/bot", BotIdView.as_view()),
    path("proxy/data/auth/register", Register.as_view()),
    path("proxy/data/auth/login", Login.as_view())
]


# routes {
#     "BotId": "BotId.py"
# }


# from django.urls import path, include
#
# from rest_framework.routers import SimpleRouter
# from .views import BotListView, BotIdView, RegisterView, LoginView
#
# router = SimpleRouter()
#
# router.register(r'proxy/data', BotListView.as_view(), basename='bot-list')
# router.register(r'proxy/data/bot', BotIdView.as_view(), basename='bot-id')
# router.register(r'proxy/data/auth/register', RegisterView.as_view(), basename='register')
# router.register(r'proxy/data/auth/login', LoginView.as_view(), basename='login')
#
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
