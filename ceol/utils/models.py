""" Django models utilities"""

#django
from django.db import models

class CeolModel(models.Model):
    """Ceol Model
    CeolModel acts as an abstract class from which other mdoel in the project
    will be inherit. This class provides everty table with the following attributes:
        * created(Datetime): store the datetime the object was created
        * modified(Datetime): store last dateime the object was modified
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on whiche the element was created')
    modified = models.DateTimeField(
        'modified at', 
        auto_now=True)
    
    class Meta:
        """Meta options"""
        abstract=True
        get_latest_by='created'
        ordering = ['-created', '-modified']