from django.shortcuts import render, redirect
from movie.models import *

# Create your views here.
def catalog_films(request):
    films = Movie.objects.all()
    return render(request, 'movie/catalog_films.html', {'films': films})

def films_detale(request, films_id):
    film = Movie.objects.get(id=films_id)
    return render(request, 'movie/films_detale.html', {'film':film, 'reviews': MovieReview.objects.filter(movie_id=films_id)})

def leave_review(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        text = request.POST.get('user_review')
        movie_id = request.POST.get('movie_id')
        MovieReview.objects.create(
            author = request.user,
            movie = Movie.objects.get(id=movie_id),
            text = text
            )
        return redirect('detale_films', films_id=movie_id)