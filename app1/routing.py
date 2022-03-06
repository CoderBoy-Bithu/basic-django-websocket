from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/',consumers.MySyncConsumers.as_asgi()),
    path('ws/ac/',consumers.MyAsyncConsumers.as_asgi())
]