"""Main class song that contains the main model object of the applications."""

#Django
from django.db import models

#Utilities
from ceol.utils.models import CeolModel

class Song(CeolModel):
    """ Class for create the song models"""
    
    name = models.CharField('Song name', blank=False, max_length=50)
    album = models.ForeignKey('player.Album', on_delete=models.CASCADE)
    time = models.DurationField('track duration')
    mp3 = models.FileField('track', upload_to='player/tracks')
    track_number = models.PositiveSmallIntegerField('No album track', blank=False)

    def __str__(self):
        """Return song name"""
        return f'{self.artist.name}: {self.name}'