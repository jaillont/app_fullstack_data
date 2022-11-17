import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyPlaylists():

    def __init__(self, sp_auth):
        self.sp_auth = spotipy.Spotify(sp_auth)
        
    def get_playlists(self):
        results = self.sp_auth.current_user_playlists()
