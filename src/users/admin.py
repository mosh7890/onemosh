from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.utils.translation import gettext as __

from .models import User

_user = get_user_model()

admin.site.empty_value_display = __('(None)')
admin.site.site_header = 'onemosh'

admin.site.unregister(EmailAddress)
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)


@admin.register(User)
class MyUser(UserAdmin):
    fieldsets = (
        (None, {
            'classes': ('extrapretty',),
            'fields': ('username', 'profile_pic', 'date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser',)
        }),
        ('Additional Information', {
            'classes': ('extrapretty', 'collapse',),
            'fields': ('password', 'email', 'first_name', 'last_name',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('extrapretty',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'profile_pic',)
        }),
    )
    list_display = ('id', 'username', 'date_joined', 'last_login',)
    list_display_links = ('id', 'username', 'date_joined', 'last_login',)
    list_filter = ('is_superuser',)
    search_fields = ('^username',)
    ordering = ('-id',)
    show_full_result_count = False
