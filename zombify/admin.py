from zombify.models import Zomburl
from django.contrib import admin

class ZombAdmin(admin.ModelAdmin):
    fields = ['zomblink', 'destination_url', 'added', 'last_accessed', 'hits']
    list_filter = ['added', 'last_accessed']
    list_display = ('zomblink', 'destination_url', 'added', 'last_accessed', 'hits')
    date_hierarchy = 'added'

admin.site.register(Zomburl, ZombAdmin)



