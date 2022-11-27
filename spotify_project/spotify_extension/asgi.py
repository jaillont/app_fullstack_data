"""
ASGI config for spotify_extension project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
from django.core.asgi import get_asgi_application

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify_extension.settings')

application = get_asgi_application()
