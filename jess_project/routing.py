from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/kitchen/', consumers.KitchenConsumer.as_asgi()),
    path('ws/kasir/', consumers.KasirConsumer.as_asgi()),
]