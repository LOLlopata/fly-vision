from django.urls import path
from movie.views import *


urlpatterns= [
    path('', catalog_films, name='home'),
    path('film/<int:films_id>/', films_detale, name='detale_films'),
    path('leave_review/', leave_review, name='leave_review'),
]