from django.urls import path
from django.contrib.auth.views import LoginView

import playlists.views as views

urlpatterns = [
    path(
        '',
        views.playlists,
        name="playlists"
    ),
]