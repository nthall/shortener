from zombify.models import Zomburl, Stats
from django.contrib import admin

admin.site.register(Zomburl)

class StatsAdmin(admin.ModelAdmin):
    fields = ['zomblink', 'hits', 'added', 'last_accessed']

admin.site.register(Stats, StatsAdmin)

