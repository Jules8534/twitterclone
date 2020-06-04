from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import TwitterUser
# Register your models here.

class TwitterUserAdmin(UserAdmin):
    list_display = ('username', 'display_name', 'is_staff', 'is_active',)
    list_filter = ('username', 'display_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'display_name', 'following', 'slug')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

admin.site.register(TwitterUser, TwitterUserAdmin)

