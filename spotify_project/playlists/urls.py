from django.urls import path

import playlists.views as views


urlpatterns = [
    path(
        '<str:username>/',
        views.playlists,
        name="playlists"
    ),
    path(
        'spotify_login',
        views.spotify_login,
        name="spotify_login"
    ),
    path(
        'spotify_callback',
        views.spotify_callback,
        name="spotify_callback"
    ),
    path(
        '<str:username>/<int:playlist_id>',
        views.tracks,
        name="tracks"
    ),
    path(
        '<str:username>/images',
        views.images,
        name="images"
    ),
]