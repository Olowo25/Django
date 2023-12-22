from __future__ import unicode_literals
from django.db import models


class Details(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    user_name=models.CharField(max_length=100)
    pass_word=models.CharField(max_length=300)

    class Meta:
        db_table = "details"
