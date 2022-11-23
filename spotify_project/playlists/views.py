from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .api_spotify.playlists import SpotifyPlaylists

from spotipy import SpotifyOAuth
from django.http import HttpResponseRedirect

import json
from urllib.parse import urlparse, parse_qs

import spotipy

CLIENT_ID = "b751ebf7066340d8951403feedf2813e"
CLIENT_SECRET = "20be98783d754c119f595929cf11e42f"


def home(request):
    
    return render(
        request,
        'playlists/home.html',
        context={}
    )

@login_required
def playlists2(request):
    return render(
        request,
        'playlists/playlists2.html',
        context={

        }
    )


@login_required
def playlists(request, username):
    # Récupérer les informations de l'utilisateur connecté
    user = request.user

    # Récupérer les informations Spotify
    sp_auth = SpotifyOAuth(
        username=request.user.spotify_username,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://localhost:8000/playlists/spotify_callback",
        scope="user-library-read"
    )
    # Get code from url
    #with open('spotify_auth.json', 'r') as f:
    #    my_loaded_dict = json.load(f)

    #code = my_loaded_dict['quentin.barthelemy@gmail.com']
    #token = sp_auth.get_access_token(code=code)

    spotify_client = spotipy.Spotify(auth_manager=sp_auth)

    playlists = spotify_client.user_playlists(request.user.spotify_username)['items']

    #for item in playlists['items'][0]:
    #print(playlists)
    #print('\n')

    return render(
        request,
        'playlists/playlists2.html',
        context={
            'user': user,
            'playlists': playlists
        }
    )



@login_required
def spotify_login(request):
    #cerca nel json
    my_loaded_dict = {}
    with open('spotify_auth.json', 'r') as f:
        try:
            my_loaded_dict = json.load(f)
        except:
            pass
    if str(request.user) in my_loaded_dict:
        #messages.error(request, "You have already linked your Spotify account")
        return HttpResponseRedirect('' + str(request.user))

    sp_auth = SpotifyOAuth(
        username=request.user.spotify_username,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://localhost:8000/playlists/spotify_callback",
        scope="user-library-read"
    )
    redirect_url = sp_auth.get_authorize_url()
    return HttpResponseRedirect(redirect_url)


@login_required
def spotify_callback(request):
    full_path = request.get_full_path()
    parsed_url = urlparse(full_path)
    spotify_code = parse_qs(parsed_url.query)['code'][0]
    data = {
        str(request.user): spotify_code
    }
    with open('spotify_auth.json', 'w') as f:
        json.dump(data, f)

    #messages.success(request, "You have correctly linked your Spotify account")

    return HttpResponseRedirect('' + str(request.user))