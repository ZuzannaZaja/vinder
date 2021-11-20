from typing import Text
from django.db import models
from django.contrib.auth.models import User


class VinderSession(models.Model):
    choices1 = models.TextField()
    choices2 = models.TextField() #kolumny varchar
    init_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="Init_User") ## co sie ma stac vider session gdy user jest usuniety
    other_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="Other_User") # tworzy relacje z users

class Movie(models.Model):
    poster = models.URLField()
    title = models.TextField() 
    director = models.TextField() 
    genre = models.TextField()
    IMDB_Rating = models.FloatField()
    cast = models.TextField()
    country = models.TextField()
    description = models.TextField()
    release_year = models.IntegerField()
    duration = models.TextField()
    