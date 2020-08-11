"""Models of artist, genres and albums"""

#Django
from django.db import models

#Utilities
from ceol.utils.models import CeolModel 


class Artist(CeolModel):
    """Class to create a artist model"""

    slug_name = models.SlugField(unique=True, max_length=50)
    artist_name = models.CharField('artist name', max_length=60, blank=False)
    last_name = models.CharField('last_name', max_length=50, blank=True, null=True)
    picture = models.ImageField('Picture of artist', upload_to='player/artists/')

    def __str__(self):
        """Return artirst name"""
        return self.artist_name

class Album(CeolModel):
    """Callas to create a albums model
    this class depends of artist"""

    artist = models.ForeignKey('player.Artist', on_delete=models.CASCADE)
    slug_name = models.SlugField(unique=True, max_length=50)
    album_name = models.CharField('album name', max_length=60, blank=False)
    album_picture = models.ImageField('album picture', upload_to='player/albums/', blank=False)
    total_songs = models.PositiveSmallIntegerField('total tracks', blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        """Return album name."""
        return self.album_name


