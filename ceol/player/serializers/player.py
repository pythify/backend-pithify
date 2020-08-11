"""Player serializers"""

#Django REST
from rest_framework import serializers

#Model
from ceol.player.models import Artist, Album, Song


class ArtistModelSerializer(serializers.ModelSerializer):
    """Artist Model Serializer"""

    class Meta:
        """Meta Class"""
        model = Artist
        fields = (
            'artist_name', 'slug_name',
            'last_name', 'picture'
        )

class AlbumModelSerializer(serializers.ModelSerializer):
    """Album model Serializer"""
    artist = ArtistModelSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = Album
        fields = '__all__'
        

class SongModelSerializer(serializers.ModelSerializer):
    """Song model serializer."""

    class Meta:
        """Meta class."""
        model = Song
        fields = (
            'name', 'album',
            'time','track_number'
        )