# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:56:52 2022

@author: tjail
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id="add_client_id", client_secret="add_client_secret")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

album_name=[]
artist_name = []
track_name = []
track_popularity = []
artist_id = []
track_id = []
for i in range(0,1000,50):
    track_results = sp.search(q='year:2021', type='track,album',market="FR", limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        artist_id.append(t['artists'][0]['id'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        track_popularity.append(t['popularity'])
        album_name.append(t['album']['name'])
import pandas as pd
track_df = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'track_popularity' : track_popularity, 'artist_id' : artist_id,"album_name":album_name})
print(track_df.shape)
print(track_df.head())