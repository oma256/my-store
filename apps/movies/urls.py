from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.movies.views import MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)