from django.urls import path
from django.contrib.auth.views import LoginView

import playlists.views as views

urlpatterns = [
    path(
        '<str:username>/',
        views.playlists,
        name="playlists"
    ),
    path('spotify_login', views.spotify_login, name="spotify_login"),
    path('spotify_callback', views.spotify_callback, name="spotify_callback"),
]