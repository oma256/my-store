from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', include('apps.movies.urls')),
    path('auth/', include('apps.users.urls')),
]
