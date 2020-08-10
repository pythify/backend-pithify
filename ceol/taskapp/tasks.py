""" Celery tasks."""

#Django
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone

#Celery
from celery.decorators import task, periodic_task

#models
from ceol.users.models import User

#Utilities
from datetime import timedelta
import jwt
import time
import requests
import json

@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):
    """Send account verification link to given user."""
    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user)
    subject = f'Welcome @{user.username}! Verify your account to start using Ceol'
    from_email = 'CEOL <noreply@ceolapi.xyz> '
    content = render_to_string(
        'emails/users/account_verification.html',
        {'token':verification_token, 'user': user}
    )

    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()

def gen_verification_token(user):
    """Create JWT token that the user can use to verify its account."""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.username,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token.decode()

@task(name='search artist', max_retries=3)
def someSearch(query):
    url = "https://deezerdevs-deezer.p.rapidapi.com/search"
    querystring = {"q":query}
    headers = {
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
        'x-rapidapi-key': "292b7df762msh8d462e70b1e0dbap14fbf1jsn6e68782d54cf"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = response.text
    searchdict = json.loads(json_data)["data"]
    artist = {}
    for result in searchdict:
        artist['id'] = result["id"]
        artist['title'] = result["title"]
        artist['duration'] = result["duration"]
        artist['url_track'] = result["preview"]
        artist['artist_id'] = result["artist"]["id"]
        artist['name'] = result["artist"]["name"]
        artist['album_id'] = result["album"]["id"]
        artist['album_name'] = result["album"]["title"]
        artist['album_cover'] = result["album"]["cover"]
    return artist

