from django.conf.urls import url

from . import consumers

print("HERE")
websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]