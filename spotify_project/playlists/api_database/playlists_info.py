import base64

from playlists.models import Playlist, Track, PlaylistWithTrack
from user.models import User


class PlaylistsInfo:

    def __init__(self, username):
        self.username = username


    def save(self, spotify_client, spotify_username):

        playlists = spotify_client.user_playlists(spotify_username)['items']

        for playlist_item in playlists:

            ## Récupérer les infos sur la playlist
            playlist_to_save, created = Playlist.objects.get_or_create(
                user = User.objects.get(
                    email = self.username
                ),
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
            tracks = spotify_client.playlist_tracks(
                playlist_id = playlist_item['id']
            )['items']

            duration_ms_total = 0

            for track in tracks:
                track_to_save, created = Track.objects.get_or_create(
                    name = track['track']['name'],
                    artist_name = track['track']['artists'][0]['name']
                )
                if created : 
                    track_to_save.duration_ms = track['track']['duration_ms']
                    track_to_save.popularity = track['track']['popularity']
                    if track['track']['preview_url'] != None:
                        track_to_save.preview_url = track['track']['preview_url']
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


    def delete(self):
        Playlist.objects.filter(
            user = User.objects.get(
                email = self.username
            )
        ).delete()


    def get_user_playlist(self):
        playlists = Playlist.objects.filter(
            user = User.objects.get(
                email = self.username
            )
        )
        return playlists

    
    def create_playlist(self, request, spotify_client):
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
            user = User.objects.get(email = self.username).spotify_username,
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

    
    def get_account_stats(self):
         # Get account stats

        # Number playlists
        total_playlists = len(Playlist.objects.filter(user = User.objects.get(email = self.username)))

        # Global popularity
        playlists_user = Playlist.objects.filter(user = User.objects.get(email = self.username))

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

        return account_stats

    
    def get_playlist_info_by_id(self, playlist_id):
        playlist = Playlist.objects.get(
            id = playlist_id
        )
        tracks = PlaylistWithTrack.objects.filter(
            playlist = playlist_id
        )

        total_popularity = 0
        counter = 0

        for track in tracks:
            total_popularity += track.track.popularity
            counter += 1
        
        global_popularity = int(total_popularity/counter)

        return playlist, tracks, global_popularity
