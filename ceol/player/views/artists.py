"""Artist views. """

# Draft
from rest_framework import viewsets, mixins

from rest_framework.permissions import IsAuthenticated

#Serializers
from ceol.player.serializers import ArtistModelSerializer

#Models
from ceol.player.models import Artist

class ArtistViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Artist view set. """

    queryset = Artist.objects.all()
    serializer_class = ArtistModelSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'slug_name'

