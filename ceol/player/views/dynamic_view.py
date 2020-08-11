""" Dynamic View """

# Django
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

#Celery
from ceol.taskapp.tasks import search_query

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_query_view(request, type_of_search, query_string):
    """
    Function that recieves a string for search, and obtain 
    all the data for each kind of search, it can be albums, artist
    or song.
    """
    response = search_query(query_string, type_of_search)
    return Response(response)
