from django.contrib import admin

from playlists.models import Playlist, Track, PlaylistWithTrack


admin.site.register(Playlist)
admin.site.register(Track)
admin.site.register(PlaylistWithTrack)
