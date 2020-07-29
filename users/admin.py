from django.contrib import admin

from . import models as users


# FACTIONS


@admin.register(users.Faction)
class FactionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'leader']
    search_fields = ['name', 'leader']


# MONEY AND REPUTATION transactions

@admin.register(users.MoneyTransaction)
class MoneyAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'amount', 'comment']
    search_fields = ['sender', 'recipient', 'amount', 'comment']
    list_filter = ('sender', 'recipient', 'amount')


@admin.register(users.ReputationTransaction)
class ReputationAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'amount', 'comment']
    search_fields = ['sender', 'recipient', 'amount', 'comment']
    list_filter = ('sender', 'recipient', 'amount')
