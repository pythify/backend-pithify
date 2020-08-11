"""Serializer Profile."""

#Djagno REST
from rest_framework import serializers

#Models
from ceol.users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile Model Serializer."""
    class Meta:
        """Meta Class."""
        model = Profile
        
        fields = (
            'picture',
        )

