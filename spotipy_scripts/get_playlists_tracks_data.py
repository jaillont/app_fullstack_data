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

#This function extracts all the items data from a playlist using its id
def get_playlists_tracks(playlist_id):
    results = spotify_client.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify_client.next(results)
        tracks.extend(results['items'])
    return tracks

#request the user's playlists
playlists = spotify_client.user_playlists(user_id)['items']
#build a dataframe from it and extract the id and name columns
ids=pd.DataFrame(playlists)
ids=ids[["id","name"]]

#this list will  all the tracks data
songs=[]
#this keys will be the data we'll keep
new_keys=["name","id","duration_ms","popularity","artists","album","playlist", "preview_url"]

#iterate over playlists ids and names
for x in range(ids.shape[0]):
    #call the function get_playlists_tracks
    tracks=get_playlists_tracks(ids["id"][x])
    #iterate over the tracks
    for i in tracks:
        #navigate through the nested dictionaries to get the desired data
        t=i['track']
        t["playlist"]=ids["name"][x]
        #get the wanted data according to our new keys
        new_dict = { key: t[key] for key in new_keys }
        #add the tracks to the song list
        songs.append(new_dict)     
        
#build a dataframe containing all the tracks from all the playlists
df=pd.DataFrame(songs)

#iterate over this df to get artists name from nested dictionaries
for i in range(df.shape[0]):
    df.artists[i]=df.artists[i][0].get('name')
    if df.preview_url[i] == None:
        df.preview_url[i]="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"


#compute some stats from the df
mean_popularity_score=df.popularity.mean()
top_5_artists=df.artists.value_counts(ascending=False)[0:5]
top_5_songs=df.name.value_counts(ascending=False)[0:5]
mean_duration=str(round(df.duration_ms.mean()/60000,3)).split('.')
mean_duration=mean_duration[0] + ' min ' + mean_duration[1] + ' s '

#compute the total duration time of every playlist
liste=[]
for each in df.playlist.unique():
    duration=np.round(df.loc[df['playlist']==each,'duration_ms'].values.sum()/60000)
    temp={
        'playlist' : each,
        'duration' : duration,
        }
    liste.append(temp)
playlist_duration_df = pd.DataFrame(liste)
    
