from django.db import models


# Create your models here.


class Videos(models.Model):
    artist = models.CharField(max_length=250)
    video_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    video_file_type = models.CharField(max_length=250)