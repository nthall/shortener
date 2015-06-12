""" admin hookup """
from shorten.models import UrlPair
from django.contrib import admin


class ShortenerAdmin(admin.ModelAdmin):     # pylint: disable-msg=R0904
    """ Administer the Shortener """
    fields = ['code', 'destination_url', 'added', 'last_accessed', 'hits']
    list_filter = ['added', 'last_accessed']
    list_display = ('code',
                    'destination_url', 'added', 'last_accessed', 'hits')
    date_hierarchy = 'added'

admin.site.register(UrlPair, ShortenerAdmin)
