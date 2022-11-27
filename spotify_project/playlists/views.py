from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

import spotipy
from spotipy import SpotifyOAuth

from stable_diffusion_tensorflow.stable_diffusion_tf.stable_diffusion import StableDiffusion

import base64
import os
import shutil
import json
from urllib.parse import urlparse, parse_qs
import matplotlib.pyplot as plt
from tensorflow import keras


from playlists.models import Playlist, Track, PlaylistWithTrack
from user.models import User
from playlists.forms import CustomNewPlaylistForm, CustomContactForm, CustomImageForm, CustomImagesChosenForm


CLIENT_ID = "533e61a793454e5387d1c5c2ab7208d8"
CLIENT_SECRET = "02fcc002491648d1bc74d3f67b510292"



def home(request):

    # ==== Create User example Start ====

    from user.create_example import CreateTrackgroundExample

    spotifyUserExample = CreateTrackgroundExample()
    spotifyUserExample.create_user_example()

    # ==== Create User example End ====
    
    return render(
        request,
        'playlists/home.html',
        context={}
    )


@login_required
def playlists(request, username):

    user = request.user

    # Récupérer les informations Spotify
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
    token = sp_auth.get_access_token(code=code)

    spotify_client = spotipy.Spotify(auth_manager=sp_auth)

    playlists = spotify_client.user_playlists(request.user.spotify_username)['items']

    Playlist.objects.filter(user = User.objects.get(email = username)).delete()

    for playlist_item in playlists:

        ## Récupérer les infos sur la playlist
        playlist_to_save, created = Playlist.objects.get_or_create(
            user = User.objects.get(email = username),
            title = playlist_item['name']
        )
        if created:
            playlist_to_save.description = playlist_item['description']
            playlist_to_save.number_of_tracks = playlist_item['tracks']['total']
            try:
                playlist_to_save.cover_image = playlist_item['images'][0]['url']
            except:
                pass
            playlist_to_save.url = True
            playlist_to_save.save()

        ## Récupérer les chansons dans la playlist
        tracks = spotify_client.playlist_tracks(playlist_id = playlist_item['id'])['items']

        duration_ms_total = 0

        for track in tracks:
            track_to_save, created = Track.objects.get_or_create(
                name = track['track']['name'],
                artist_name = track['track']['artists'][0]['name']
            )
            if created : 
                track_to_save.duration_ms = track['track']['duration_ms']
                track_to_save.popularity = track['track']['popularity']
                track_to_save.cover_image = track['track']['album']['images'][0]['url']
                
                duration_track_min = (track['track']['duration_ms']/1000) // 60
                duration_track_sec = (track['track']['duration_ms']/1000) - duration_track_min*60
                duration_track = f"{int(duration_track_min)} min {int(duration_track_sec)} s"

                track_to_save.duration = duration_track

                track_to_save.save()

                duration_ms_total += track['track']['duration_ms']
            
            else:
                duration_ms_total += track_to_save.duration_ms

            PlaylistWithTrack.objects.get_or_create(
                playlist = playlist_to_save,
                track = track_to_save
            )

        duration_min = (duration_ms_total/1000) // 60
        duration_ms_total -= duration_min*60*1000
        duration_sec = duration_ms_total // 1000

        duration = f"{int(duration_min)} min {int(duration_sec)} s"
        
        playlist_to_save.duration = duration
        playlist_to_save.save()
        

    playlist_from_model = Playlist.objects.filter(user = User.objects.get(email = username))

    if request.method == 'POST':

        if 'title' in request.POST:


            form = CustomNewPlaylistForm(request.POST)


            if form.is_valid():

                tracks = request.POST['tracks']
                list_tracks = tracks.split('-')

                musics_to_add = []

                for track in list_tracks:
                    track_info = track.split(',')
                    artist_name = track_info[0][1:]
                    song_title = track_info[1][:-1]

                    track_to_add = spotify_client.search(
                        q = f"{artist_name} {song_title}",
                        type = "track",
                        market = "FR"
                    )

                    musics_to_add += [track_to_add['tracks']['items'][0]['id']]

                playlist = spotify_client.user_playlist_create(
                    user = User.objects.get(email = username).spotify_username,
                    name = request.POST['title'],
                    public = True,
                    description = request.POST['description']
                )

                playlist_tracks = spotify_client.playlist_add_items(
                    playlist_id=playlist['id'],
                    items=musics_to_add
                )
                try:

                    with open("static/assets/img/cover/"+request.POST['image'], 'rb') as image:
                        image_to_upload = base64.b64encode(image.read()).decode("utf-8")
                    
                    spotify_client.playlist_upload_cover_image(
                        playlist_id=playlist['id'],
                        image_b64=image_to_upload
                    )
                except:
                    pass

                return redirect('playlists', username = username)
        
        if 'subject' in request.POST:

            form = CustomContactForm(request.POST)

            if form.is_valid():

                msg = EmailMessage(
                    subject = request.POST['subject'],
                    body = request.POST['message'],
                    #from_email = username,
                    to = ['quentin.barthelemy@edu.esiee.fr', 'thomas.jaillon@edu.esiee.fr']
                )
                msg.send()

                return redirect('playlists', username = username)

        if 'image_description' in request.POST:

            form = CustomImageForm(request.POST)

            if form.is_valid():
                
                # Générer l'image
                height = int(os.environ.get("WIDTH", 640))
                width = int(os.environ.get("WIDTH", 640))
                mixed_precision = os.environ.get("MIXED_PRECISION", "no") == "yes"

                if mixed_precision:
                    keras.mixed_precision.set_global_policy("mixed_float16")

                generator = StableDiffusion(img_height=height, img_width=width, jit_compile=True, download_weights=True)

                description = 'album cover ' + request.POST['image_description'] + ' ' + request.POST['image_type'] + ' ' + request.POST['image_aspect']

                # tf.keras.mixed_precision.set_global_policy("mixed_float16")
                # model = keras_cv.models.StableDiffusion(jit_compile=True, img_width=320, img_height=320)
                # print("model has been trained")
                # image = model.text_to_image(description, batch_size=1, num_steps=20)

                images = generator.generate(description, batch_size=3, num_steps=20, unconditional_guidance_scale=7.5, temperature=1,)

                for i in range(len(images)):
                    plt.imsave('static/assets/img/buffer_cover/' + str(i)+request.POST['image_name']+'.jpeg',images[i])

                # plt.imsave('static/assets/img/cover/' + request.POST['image_name']+'.jpeg',image[0])

                #return redirect('playlists', username = username)

                return redirect('images', username = username)

    else:
        form = CustomNewPlaylistForm()
        contact_form = CustomContactForm()
        image_form = CustomImageForm()

    images = os.listdir('static/assets/img/cover')

    # Get account stats

    # Number playlists
    total_playlists = len(Playlist.objects.filter(user = User.objects.get(email = username)))

    # Global popularity
    playlists_user = Playlist.objects.filter(user = User.objects.get(email = username))

    total_popularity = 0
    counter = 0

    for playlist in playlists_user:
        tracks = PlaylistWithTrack.objects.filter(playlist=playlist.id)
        for track in tracks:
            total_popularity += track.track.popularity
            counter += 1
    
    global_popularity = int(total_popularity/counter)

    total_duration = 0

    for playlist in playlists_user:
        tracks = PlaylistWithTrack.objects.filter(playlist=playlist.id)
        for track in tracks:
            total_duration += track.track.duration_ms
    
    mean_duration = total_duration/counter

    mean_duration_min = mean_duration/1000//60
    mean_duration -= mean_duration_min*60*1000
    mean_duration_sec = mean_duration // 1000
    
    mean_duration_str = f"{int(mean_duration_min)} min {int(mean_duration_sec)} sec"


    f = open('static/css/styles-playlists.css', 'r+')

    raw = ".account .global-popularity {\n"
    raw += "  width: " + str(global_popularity) + "%;\n"
    raw += "}\n\n"

    raw += ".account .mean-playlist-duration {\n"
    raw += "  width: " + str(int(mean_duration_min)/7*100) + "%;\n"
    raw += "}\n\n"

    f.write(raw)

    
    # All stats
    account_stats = [total_playlists, global_popularity, mean_duration_str]

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

    #messages.success(request, "You have correctly linked your Spotify account")

    return HttpResponseRedirect('' + str(request.user))


@login_required
def tracks(request, username, playlist_id):

    playlist = Playlist.objects.get(id = playlist_id)
    tracks = PlaylistWithTrack.objects.filter(playlist = playlist_id)

    total_popularity = 0
    counter = 0

    for track in tracks:
        total_popularity += track.track.popularity
        counter += 1
    
    global_popularity = int(total_popularity/counter)

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
                shutil.copyfile(f"static/assets/img/buffer_cover/{image}", f"static/assets/img/cover/{image}")

            dir = 'static/assets/img/buffer_cover'
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))

            return redirect('playlists', username = username)

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