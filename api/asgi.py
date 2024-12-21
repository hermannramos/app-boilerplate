"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path

# Importa las vistas para los websockets
# from api.consumers import ChatConsumer  # Asegúrate de tener un consumidor creado

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Maneja solicitudes HTTP
    # "websocket": AuthMiddlewareStack(
    #     URLRouter([
    #         path('ws/chat/', ChatConsumer.as_asgi()),  # Ruta de ejemplo para websockets
    #     ])
    # ),
})
