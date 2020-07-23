"""Main URLs module."""
from django.urls import path, include

from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    #CEOL users
    path('', include(('ceol.users.urls', 'users'), namespace='users')),
    path('', include(('ceol.player.urls', 'player'), namespace='player')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
