"""Users url"""

#django 
from django.urls import path, include

#Django REST
from rest_framework.routers import DefaultRouter

#Views
from .views import users as users_views

router = DefaultRouter()
router.register(r'users', users_views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
