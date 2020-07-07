"""Profile model"""

#django
from django.db import models

#Utilities
from ceol.utils.models import CeolModel

class Profile(CeolModel):
    """Profile Model

    A profile holds a user's public data like picture and statistics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True
    )

    def __str__(self):
        """Return user's str representation"""
        return str(self.user)