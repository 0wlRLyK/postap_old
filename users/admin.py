from django.contrib import admin

from . import models as users


# FACTIONS


@admin.register(users.Faction)
class FactionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'leader']
    search_fields = ['name', 'leader']
