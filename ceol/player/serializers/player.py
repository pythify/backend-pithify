"""Player serializers"""

#Django REST
from rest_framework import serializers

#Model
from ceol.player.models import Artist, Album, Genre

class ArtistModelSerializer(serializers.ModelSerializer):
    """Artist Model Serializer"""

    class Meta:
        """Meta Class"""
        model = Artist
        fields = (
            'id_artist', 'name',
            'last_name',
        )

class AlbumModelSerializer(serializers.ModelSerializer):
    """Album model Serializer"""

    class Meta:
        model = Album
        fields = (
            'id_album', 'album_name',
            'artist_id',
        )    