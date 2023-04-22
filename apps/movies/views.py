from django.views.generic import ListView, DetailView

from apps.movies.models import Movie


class MovieListView(ListView):
    template_name = 'pages/index.html'
    queryset = Movie.objects.all()
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'pages/movie_detail.html'
    context_object_name = 'movie'
