from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator,OriginValidator
from chaterino.consumers import ConsumidorChat
application = ProtocolTypeRouter({
  'websocket': AllowedHostsOriginValidator(
    AuthMiddlewareStack(
      URLRouter(
        [
          url(r"^messages/(?P<username>[\w.@+-]+)/$", ConsumidorChat),
        ]
      )
    )

  )
})