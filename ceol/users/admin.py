"""Users models admin"""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#models
from ceol.users.models import User, Profile

class CustomUserAdmin(UserAdmin):
    """User model admin"""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_premium')
    list_filter = ('is_premium', 'is_staff', 'created', 'modified')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model Admin"""
    list_display = ('user',)
    search_fields = ('user__username', 'user__email', 'user__first_name')

admin.site.register(User, CustomUserAdmin)