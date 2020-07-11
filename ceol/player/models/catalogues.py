"""Models of artist, genres and albums"""

import uuid

#Django
from django.db import models

#Utilities
from ceol.utils.models import CeolModel 


class Artist(CeolModel):
    """Class to create a artist model"""

    id_artist = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('artist name', max_length=60, blank=False)
    last_name = models.CharField('last_name', max_length=50, blank=True, null=True)
    picture = models.ImageField('Picture of artist', upload_to=None)

    def __str__(self):
        """Return artirst name"""
        return self.name

class Album(CeolModel):
    """Callas to create a albums model
    this class depends of artist"""

    id_album = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    album_name = models.CharField('album name', max_length=60, blank=False)
    album_picture = models.ImageField('album picture', upload_to=None, blank=False)
    artist_id = models.ForeignKey("player.Artist", verbose_name="album artist", on_delete=models.CASCADE)

class Genres(CeolModel):
    """Genres have a relation many to many with
    songs"""

    id_genres = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
