"""Song views. """

# Draft
from rest_framework import viewsets, mixins
# from rest_framework import IsAuthenticated

#Serializers
from ceol.player.serializers import SongModelSerializer

#Models
from ceol.player.models import Song

class SongViewSet(viewsets.ModelViewSet):
    """Song view set. """
    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
    

