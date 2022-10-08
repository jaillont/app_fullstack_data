import spotipy
from spotipy.oauth2 import SpotifyOAuth

import base64

scope_playlist = "playlist-modify-public"
scope_image ="ugc-image-upload"

username = ""

CLIENT_ID = ""
CLIENT_SECRET = ""

token = SpotifyOAuth(
    scope = [
        scope_playlist,
        scope_image
    ],
    username = username,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="https://open.spotify.com"
)
spotify = spotipy.Spotify(auth_manager=token)


### 1. Créer une playlist si elle n'existe pas déjà
# Comment les différencier ? => Nom

playlists = spotify.current_user_playlists()['items']

playlist_name = "Playlist 47ter"
playlist_description = "Mes musiques préférées de 47ter"


if len(playlists) == 0:
    playlist = spotify.user_playlist_create(
        user = username,
        name = playlist_name,
        public = True,
        description = playlist_description
    )

    playlist_id = playlist['id'] # A stocker dans une base de donnée

for i in range(len(playlists)):
    if playlists[i]['name'] == playlist_name:
        break
    else:
        playlist = spotify.user_playlist_create(
            user = username,
            name = playlist_name,
            public = True,
            description = playlist_description
        )

        playlist_id = playlist['id'] # A stocker dans une base de donnée

### 2a. Trouver une musique et récupérer son ID 

track_to_add_1 = spotify.search(
    q = "47ter Harakiri",
    type = "track",
    market = "FR"
)

track_id_1 = track_to_add_1['tracks']['items'][0]['id']

track_to_add_2 = spotify.search(
    q = "47ter L'adresse",
    type = "track",
    market = "FR"
)

track_id_2 = track_to_add_2['tracks']['items'][0]['id']

musics_to_add = [
    track_id_1,
    track_id_2
]

### 2b. Ajouter des musiques à cette playlist

playlist_id = playlist_id

spotify.playlist_add_items(
    playlist_id=playlist_id,
    items=musics_to_add
)

### 2. Récupérer les musiques de la playlist (exemple d'info possible)

playlist_tracks = spotify.playlist_tracks(
    playlist_id=playlist_id,
    market="FR"
)

print("\n")
print('TRACKS')
print("\n")

for i in range(len(playlist_tracks['items'])):
    print("-", playlist_tracks['items'][i]['track']['name'])

print("\n")

### 3. Changer l'image de couverture


with open("image.jpeg", 'rb') as image:
    image_to_upload = base64.b64encode(image.read()).decode("utf-8")

spotify.playlist_upload_cover_image(
    playlist_id=playlist_id,
    image_b64=image_to_upload
)