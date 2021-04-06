import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat.consumers import DialogConsumer, ChatConsumer
from django.conf.urls import url

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'postap.settings')

application = ProtocolTypeRouter({
    # Websocket chat handler
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    # url(r"chat/", DialogConsumer, name='chat')
                    url(r"d/(?P<username>[\w.@+-]+)/$", DialogConsumer.as_asgi(), name='dialog'),
                    url(r"chat/(?P<slug>[\w.@+-]+)/$", ChatConsumer.as_asgi(), name='chat')
                ]
            )
        ),
    ),
})
