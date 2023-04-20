from django.urls import path

from apps.users.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]