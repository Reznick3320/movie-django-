from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.

def show_all_movies(request):
    movies = Movie.objects.all()
    # movies = Movie.objects.order_by('name')
    context = {
        'movies': movies
    }
    return render(request, 'movie_app/all_movies.html', context=context)

def show_one_movies(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    context = {
        'movie': movie
    }
    return render(request, 'movie_app/one_movie.html', context=context)

# def show_one_movies(request, id_movie:int):
#     movie = get_object_or_404(Movie, id=id_movie)
#     context = {
#         'movie': movie
#     }
#     return render(request, 'movie_app/one_movie.html', context=context)