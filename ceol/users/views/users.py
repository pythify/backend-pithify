"""Users Views"""

#Django REST
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, viewsets, mixins

#models
from ceol.users.models import User

#Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

#serializers
from ceol.users.serializers import (
    UserModelSerializer,
    UserLoginSerializer,
    UserSignUpSerializer,
    AccountVerificationSerializer)

class UserViewSet(mixins.RetrieveModelMixin,
                viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permission(self):
        """Assigns permissions based on actions."""
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User login."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User signup"""

        serializer = UserSignUpSerializer(data =request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Account verification"""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulations, now you can start to enjoy'}
        return Response(data, status=status.HTTP_200_OK)
