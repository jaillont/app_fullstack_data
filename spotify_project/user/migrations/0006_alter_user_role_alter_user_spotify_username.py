# Generated by Django 4.1.2 on 2022-11-15 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Administrateur'), ('USER', 'Utilisateur')], default='USER', max_length=30, verbose_name='Rôle'),
        ),
        migrations.AlterField(
            model_name='user',
            name='spotify_username',
            field=models.CharField(max_length=50, verbose_name='Spotify Username'),
        ),
    ]
