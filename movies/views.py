from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddFilmForm, SearchFilmForm, Placeform
from django.urls import reverse
from .models import Movie, Places

def main_page(request, search=''):
    all_movies = Movie.objects.all()

    if request.method == 'GET':
        search_text = request.GET.get('q')
        if search_text is not None:
            all_movies = Movie.objects.filter(title__contains=search_text)

    return render(request, 'main_page.html', {'movies': all_movies})


def genre_page(request, genre):
    all_movies = Movie.objects.filter(genre=genre)
    return render(request, 'main_page.html', {'movies': all_movies })

@login_required
def add_film(request):
    if request.method == 'POST':
        form = AddFilmForm(data=request.POST,
                           files=request.FILES)
        if form.is_valid():
            this_movie = form.save()
            Places.objects.create(chain_models=this_movie)

            redirect(reverse('main_page'))
    else:
        form = AddFilmForm(instance=request.user)
    return render(request, 'add_film.html', {'film_form': form})

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    places = get_object_or_404(Places, chain_models=movie)
    if request.method == 'POST':
        select_places_form = Placeform(data=request.POST, instance=places)
        if select_places_form.is_valid():
            select_places_form.save()
    else:
        select_places_form = Placeform()
    return render(request, 'detail.html', {'movie': movie, 'places': places, 'select_places_form': select_places_form})
