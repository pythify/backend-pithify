""" Player Admin."""

#Django
from django.contrib import admin

#models
from ceol.player.models import Artist, Album, Song

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Artist admin."""

    list_display = (
        'slug_name',
        'artist_name',
        'last_name'
    )
    search_fields = ('artist_name', 'slug_name')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Album admin."""
    list_display = (
        'slug_name',
        'album_name',
        'total_songs',
    )
    search_fields = (
        'slug_name',
        'artist__artist_name',
        'album_name'
    )
    list_filter = (
        'release_date',
    )

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """Song Admin"""

    list_display = (
        'name',
        'album',
        'track_number'
    )
    search_fields = (
        'album__artist_name',
        'album__album_name'
    )
