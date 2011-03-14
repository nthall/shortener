from zombify.models import Zomburl
from django.contrib import admin

class ZombAdmin(admin.ModelAdmin):
    fields = ['zomblink', 'destination_url', 'added', 'last_accessed', 'hits']
    list_filter = ['added', 'last_accessed']

admin.site.register(Zomburl, ZombAdmin)



