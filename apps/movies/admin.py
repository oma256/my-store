from django.contrib import admin
from apps.movies.models import Movie, Genre


admin.site.register(Movie)
admin.site.register(Genre)
