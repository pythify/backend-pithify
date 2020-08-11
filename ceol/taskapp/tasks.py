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
def search_query(query, type_of_search):
    try:
        url = "https://deezerdevs-deezer.p.rapidapi.com/search"
        querystring = {"q":query}
        headers = {
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
            'x-rapidapi-key': "292b7df762msh8d462e70b1e0dbap14fbf1jsn6e68782d54cf"
            }
        response = requests.request("GET", url, headers=headers, params=querystring) # Json Object
    
        if type_of_search == 'artist':
            return artistFilter(response)
        if type_of_search == 'album':
            return albumFilter(response)
        if type_of_search == 'songs':
            return songFilter(response)
    except expression as identifier:
        return {'error' :'FATAL ERROR'}


""" Dezeer API modules """
def jsonParser(response):

    json_data = response.text # String
    result_dictionary = json.loads(json_data) # Parse String to Python Dictionary
        
    return result_dictionary

def artistFilter(response):
    # Json parser to Python Dict
    raw_results = jsonParser(response)
        
    my_new_list=[]
    artists = {}

    for item in raw_results['data']:
        if item['artist']['name'] not in my_new_list:
            my_new_list.append(item['artist'])

    artists['data'] = my_new_list
    artists['next'] = raw_results['next']    

    return artists

def albumFilter(response):
    # Json parser to Python Dict
    raw_results = jsonParser(response)
        
    my_new_list=[]
    albums = {}

    for item in raw_results['data']:
        if item['album']['title'] not in my_new_list:
            my_new_list.append(item['album'])

    albums['data'] = my_new_list
    albums['next'] = raw_results['next']    

    return albums

def songFilter(response):

    # Json parser to Pythons Dict
    raw_results = jsonParser(response)
        
    my_new_list=[]
    albums = {}

    for item in raw_results['data']:
        newitem = {}
        my_new_list.append(item)

    songs['data'] = my_new_list
    songs['next'] = raw_results['next']    

    return raw_results