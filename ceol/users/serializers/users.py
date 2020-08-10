
"""User serializers"""

#Django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate


#Serializers
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

#Serializers
from ceol.users.serializers.profiles import ProfileModelSerializer

#models
from ceol.users.models import User, Profile

#utilities
from datetime import timedelta
import jwt


#Tasks
from ceol.taskapp.tasks import send_confirmation_email

class UserModelSerializer(serializers.ModelSerializer):
    """User model Serializer."""
    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profile'
        )

class UserSignUpSerializer(serializers.Serializer):
    """User signupSerializer
    Handle sign up data validation and user/profiel creation.
    """
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    #Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    #Name
    first_name =  serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Verify paswords match"""
        passwd = data['password']
        passwd_confirmation = data['password_confirmation']
        if passwd != passwd_confirmation:
            raise serializers.ValidationError("Passwords don't match")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile."""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False, is_premium=False)
        Profile.objects.create(user=user)
        send_confirmation_email.delay(user_pk=user.pk)
        return user


class UserLoginSerializer(serializers.Serializer):
    """User login Serializer
    Handle the login request data."""

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        if not user.is_verified:
            raise serializers.ValidationERror('Account is not active yet')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

class AccountVerificationSerializer(serializers.Serializer):
    """Account Verification Serializer."""
    token = serializers.CharField()

    def validate_token(self, data):
        """Verify token is valid."""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorith=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired')
        except jwt.exceptions.PyJWTError:
            raise serializers.ValidationError('Invalid Token')

        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid Token')
        self.context['payload'] = payload
        return data

    def save(self):
        """Update user's verified status"""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
        


