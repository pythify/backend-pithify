"""Album views. """

# Draft
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
# from rest_framework import IsAuthenticated

#Serializers
from ceol.player.serializers import AlbumModelSerializer, ArtistModelSerializer

#Models
from ceol.player.models import Album, Artist

class AlbumViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Album view set. """
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verify that album exists."""
        slug_name = kwargs['slug_name']
        self.artist = get_object_or_404(Artist, slug_name=slug_name)
        return super(AlbumViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """Return albums for artist"""
        return Album.objects.filter(
            artist=self.artist
        )



