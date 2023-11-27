from django.urls import path, include
from .views import BotListView, BotIdView, RegisterView, LoginView

urlpatterns = [
    path("proxy/data", BotListView.as_view()),
    path("proxy/data/bot", BotIdView.as_view()),
    path("proxy/data/auth/register", RegisterView.as_view()),
    path("proxy/data/auth/login", LoginView.as_view())
]


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
