"""
ASGI config for djangochannels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochannels.settings')
from django.core.asgi import get_asgi_application
application = get_asgi_application()
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack
from chat import routing as chat_routing
from chat import consumers
from django.conf.urls import url

application = ProtocolTypeRouter(    
    {        
        "http": get_asgi_application(),        
        "websocket": AuthMiddlewareStack(            
            URLRouter(                
[   url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]
            )        
        ),

        "https": get_asgi_application(),    
    })
