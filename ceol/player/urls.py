""" Player urls."""

from django.urls import include, path, re_path

#Django REST
from rest_framework.routers import DefaultRouter

#Views
from .views import albums as album_views
from .views import artists as artist_views
from .views import songs as song_views
from .views.dynamic_view import search_query_view

router = DefaultRouter()

router.register(r'player/(?P<slug_name>[a-zA-Z0-9_-]+)/album',
                album_views.AlbumViewSet,
                basename='album')

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^player/(?P<type_of_search>[a-zA-Z0-9_-]+)/(?P<query_string>[a-zA-Z0-9_-]+)/$',
                search_query_view)
]