from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

import spotipy
from spotipy import SpotifyOAuth

import os
import shutil
import json
from urllib.parse import urlparse, parse_qs

from playlists.api_database.playlists_info import PlaylistsInfo
from playlists.image_model.generate_image import GenerateImage

from playlists.forms import CustomNewPlaylistForm, CustomContactForm, CustomImageForm, CustomImagesChosenForm


CLIENT_ID = "318c76e1a8bc41b8ad39c9412c7ef341"
CLIENT_SECRET = "f060983626184202a5a4651725687234"

# ==== Create User example Start ==== #

from user.create_example import CreateTrackgroundExample

spotifyUserExample = CreateTrackgroundExample()
spotifyUserExample.create_user_example()

# ==== Create User example End ==== #


def home(request):
    
    return render(
        request,
        'playlists/home.html',
        context={}
    )


@login_required
def playlists(request, username):

    # ==== Create Spotify Connexion Start ==== #

    sp_auth = SpotifyOAuth(
        username=request.user.spotify_username,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://localhost:8000/playlists/spotify_callback",
        scope="user-library-read playlist-modify-public ugc-image-upload"
    )
    # Get code from url
    with open('spotify_auth.json', 'r') as f:
       my_loaded_dict = json.load(f)

    code = my_loaded_dict[username]
    token = sp_auth.get_access_token(
        code=code
    )

    spotify_client = spotipy.Spotify(
        auth_manager=sp_auth
    )

    # ==== Create Spotify Connexion End ==== #

    # ==== Get Info to Display Start ==== #

    # Get connected user
    user = request.user

    # Get user playlists
    spotify_username = request.user.spotify_username

    playlist_info = PlaylistsInfo(username)
    playlist_info.delete()
    playlist_info.save(
        spotify_client,
        spotify_username
    )

    playlist_from_model = playlist_info.get_user_playlist()

    # Get generated images
    images = os.listdir('static/assets/img/cover')

    # Get account stats
    account_stats = playlist_info.get_account_stats()


    # ==== Get Info to Display End ==== #

    
    if request.method == 'POST':
        
        # Form to create a new playlist
        if 'title' in request.POST:

            form = CustomNewPlaylistForm(request.POST)

            if form.is_valid():
                
                # Create playlist requested
                playlist_info.create_playlist(
                    request,
                    spotify_client
                )
                return redirect('playlists', username = username)


        # Form to send an email
        if 'subject' in request.POST:

            form = CustomContactForm(request.POST)

            if form.is_valid():

                msg = EmailMessage(
                    subject = request.POST['subject'],
                    body = request.POST['message'],
                    from_email = username,
                    to = [
                        'quentin.barthelemy@edu.esiee.fr',
                        'thomas.jaillon@edu.esiee.fr'
                    ]
                )
                msg.send()

                return redirect(
                    'playlists',
                    username=username
                )


        # Form to create an image
        if 'image_description' in request.POST:

            form = CustomImageForm(request.POST)

            if form.is_valid():
                
                model = GenerateImage(request)
                model.generate_images()

                return redirect(
                    'images',
                    username=username
                )

    else:
        form = CustomNewPlaylistForm()
        contact_form = CustomContactForm()
        image_form = CustomImageForm()

    return render(
        request,
        'playlists/playlists.html',
        context={
            'user': user,
            'playlists': playlist_from_model,
            'form': form,
            'contact_form': contact_form,
            'images': images,
            'image_form': image_form,
            'account_stats': account_stats
        }
    )


@login_required
def tracks(request, username, playlist_id):

    playlist_info = PlaylistsInfo(username)
    playlist, tracks, global_popularity = playlist_info.get_playlist_info_by_id(playlist_id)

    return render(
        request,
        'playlists/tracks.html',
        context={
            'playlist': playlist,
            'tracks': tracks,
            'global_popularity': global_popularity
        }
    )


@login_required
def images(request, username):

    generated_images = os.listdir('static/assets/img/buffer_cover')

    if request.method == 'POST':

        form = CustomImagesChosenForm(request.POST)

        if form.is_valid():
            
            images_to_keep = request.POST['images'].rstrip().split(" ")
            for image in images_to_keep:
                shutil.copyfile(
                    f"static/assets/img/buffer_cover/{image}",
                    f"static/assets/img/cover/{image}"
                )

            dir = 'static/assets/img/buffer_cover'
            for f in os.listdir(dir):
                os.remove(
                    os.path.join(
                        dir,
                        f
                    )
                )

            return redirect(
                'playlists',
                username=username
            )

    else:
        form = CustomImagesChosenForm()


    return render(
        request,
        'playlists/images.html',
        context={
            'generated_images': generated_images,
            'form': form
        }
    )


@login_required
def spotify_login(request):

    my_loaded_dict = {}
    with open('spotify_auth.json', 'r') as f:
        try:
            my_loaded_dict = json.load(f)
        except:
            pass

    if str(request.user) in my_loaded_dict:
        return HttpResponseRedirect('' + str(request.user))

    sp_auth = SpotifyOAuth(
        username=request.user.spotify_username,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://localhost:8000/playlists/spotify_callback",
        scope="user-library-read playlist-modify-public ugc-image-upload"
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

    return HttpResponseRedirect('' + str(request.user))