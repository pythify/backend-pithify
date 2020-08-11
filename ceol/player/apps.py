"""Player apps"""

#Django
from django.apps import AppConfig

class PlayerAppConfig(AppConfig):
    """Player app config
    
    The player contains the reference to the objects models like artists, songs
    and albums.
    """

    name = 'ceol.player'
    verbose_name = 'Player'
