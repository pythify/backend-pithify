"""Users model"""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser

#Utilities
from ceol.utils.models import CeolModel

class User(CeolModel, AbstractUser):
    """Users model.

    Extend from django's Abstract User, change the username field to email,
    and add some extra fields.
    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with the email already exists'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_premium = models.BooleanField(
        'premium membership',
        default=False,
        help_text=(
            'Distinguish users with premium membership or free membership'
        )
    )
    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to True when the user have verified its emaill address'
    )

    def __str__(self):
        """Return username"""
        return self.username
