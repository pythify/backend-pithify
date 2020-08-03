""" Player urls."""

from django.urls import include, path

#Django REST
from rest_framework.routers import DefaultRouter

#Views
from .views import albums as album_views
from .views import artists as artist_views
from .views import songs as song_views

router = DefaultRouter()

router.register(r'player/artist', artist_views.ArtistViewSet, basename='artist')

router.register(r'player/(?P<slug_name>[a-zA-Z0-9_-]+)/album',
                album_views.AlbumViewSet,
                basename='album')

urlpatterns = [
    path('', include(router.urls))
]