# Generated by Django 4.1.2 on 2022-10-28 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('duration', models.DurationField(null=True)),
                ('number_of_tracks', models.IntegerField(null=True)),
                ('cover_image', models.CharField(max_length=50, null=True)),
            ],
            options={
                'ordering': ['number_of_tracks'],
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('duration', models.DurationField()),
                ('artist_id', models.CharField(max_length=50)),
                ('artist_name', models.CharField(max_length=50)),
                ('album_id', models.CharField(max_length=50)),
                ('album_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['artist_name'],
            },
        ),
        migrations.CreateModel(
            name='PlaylistWithTracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.track')),
            ],
            options={
                'ordering': ['playlist'],
            },
        ),
    ]
