from django.db import models
from user.models import User


class Track(models.Model):

    class Meta:
        ordering = ['artist_name', 'popularity']

    def __str__(self):
        return f'{self.name} | {self.artist_name}'

    name = models.CharField(
        max_length=150,
        null=False
    )
    artist_name = models.CharField(
        max_length=150,
        null=False
    )
    duration_ms = models.IntegerField(
        default=0
    )
    duration = models.CharField(
        max_length=20,
        default=""
    )
    popularity = models.IntegerField(
        default=0
    )
    cover_image = models.CharField(
        max_length=1000,
        default=""
    )


class Playlist(models.Model):

    class Meta:
        ordering = ['number_of_tracks']

    def __str__(self):
        return f'{self.title} | {self.duration}'

    title = models.CharField(
        max_length=50,
        null=False
    )
    description = models.CharField(
        max_length=100,
        null=False,
        default= "No description provide"
    )
    number_of_tracks = models.IntegerField(null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    cover_image = models.CharField(
        max_length=1000,
        default="https://i0.wp.com/lesoreillescurieuses.com/wp-content/uploads/2017/07/arcade-fire-everything-now.jpg?w=640&ssl=1"
    )
    url = models.BooleanField(
        default=True
    )
    duration = models.CharField(
        max_length=20,
        null=True
    )


class PlaylistWithTrack(models.Model):

    class Meta:
        ordering = ['playlist']

    def __str__(self):
        return f'{self.playlist.title} | {self.track.name}'

    playlist = models.ForeignKey(
        Playlist,
        on_delete=models.CASCADE
    )
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE
    )
