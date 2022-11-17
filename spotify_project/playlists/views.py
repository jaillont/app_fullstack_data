from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .api_spotify.playlists import SpotifyPlaylists

from spotipy.oauth2 import SpotifyOAuth
from django.http import HttpResponseRedirect

CLIENT_ID = "b751ebf7066340d8951403feedf2813e"
CLIENT_SECRET = "20be98783d754c119f595929cf11e42f"


def home(request):
    return render(
        request,
        'playlists/home.html',
        context={}
    )

@login_required
def playlists(request):
    
    return render(
        request,
        'playlists/playlists.html',
        context={
            
        }
    )
