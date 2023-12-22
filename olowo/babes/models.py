from django.db import models


class Babes(models.Model):
    name = models.CharField(max_length=250)
    year = models.CharField(max_length=250)
    rating = models.CharField(max_length=250)
    age = models.CharField(max_length=250)

    # picture = models.FileField()

    class Meta:
        db_table = "Babies"
