from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class User(AbstractUser):
    gender = models.BooleanField(null=True, blank=True)
    wathedMovie = models.ManyToManyField('movie.Movie', related_name='wached_movies')
    photo = models.ImageField(upload_to="images/users/avatars/")
    favMovie = models.ManyToManyField('movie.Movie', related_name='fav_movies')


# models.py
