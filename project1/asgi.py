import app1.routing
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        app1.routing.websocket_urlpatterns
    )
})
