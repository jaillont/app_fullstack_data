from django.db import models

class Playlist(models.Model):

    class Meta:
        ordering = ['number_of_tracks']

    def __str__(self):
        return f'{self.title} | {self.duration}'

    title = models.CharField(
        max_length=50,
        null=False
    )
    duration = models.DurationField(
        null=True
    )
    number_of_tracks = models.IntegerField(
        null=True
    )
    cover_image = models.CharField(
        max_length = 50,
        null=True
    )


class Track(models.Model):

    class Meta:
        ordering = ['artist_name']

    def __str__(self):
        return f'{self.title} | {self.artist_name} | {self.album_name}'

    title = models.CharField(
        max_length = 50,
        null=False
    )
    duration = models.DurationField()
    artist_id = models.CharField(
        max_length = 50,
        null=False
    )
    artist_name = models.CharField(
        max_length = 50,
        null=False
    )
    album_id = models.CharField(
        max_length = 50,
        null=False
    )
    album_name = models.CharField(
        max_length = 50,
        null=False
    )


class PlaylistWithTracks(models.Model):

    class Meta:
        ordering = ['playlist']

    def __str__(self):
        return f'{self.track.title} | {self.playlist.title}'

    track = models.ForeignKey(
        Track,
        null=False,
        on_delete=models.CASCADE
    )
    playlist = models.ForeignKey(
        Playlist,
        null=False,
        on_delete=models.CASCADE
    )
