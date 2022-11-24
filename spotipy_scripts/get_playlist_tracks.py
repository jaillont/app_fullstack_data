# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:41:38 2022

@author: tjaill
"""

#imports
import spotipy
import numpy as np
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id="client_id", client_secret="client_secret")
spotify_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
user_id='user_id'

#this keys will be the data we'll keep
new_keys=["name","id","duration_ms","popularity","artists","album"]
#This function extracts all the items data from a playlist using its id
def get_playlist_tracks(playlist_id):
    results = spotify_client.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify_client.next(results)
        tracks.extend(results['items'])

    #this list will  all the tracks data
    songs=[]
    for i in tracks:
        #navigate through the nested dictionaries to get the desired data
        t=i['track']
        #get the wanted data according to our new keys
        new_dict = { key: t[key] for key in new_keys }
        #add the tracks to the song list
        songs.append(new_dict)  
    df=pd.DataFrame(songs)
    for i in range(df.shape[0]):
        df.artists[i]=df.artists[i][0].get('name')
    return df

df=get_playlist_tracks('76XgecIbSzl3UpkcEZSIUa')


