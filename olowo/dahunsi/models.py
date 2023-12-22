from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length = 250)
    album_title = models.CharField(max_length = 250)
    genre = models.CharField(max_length = 250)
    album_logo = models.FileField()

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    artist = models.CharField(max_length = 250)
    song_title = models.CharField(max_length = 250)
    genre = models.CharField(max_length = 250)
    song = models.FileField()
