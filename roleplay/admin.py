from django.contrib import admin

from . import models as rp


@admin.register(rp.Trader)
class NPCTraderAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Персональные данные", {'fields': ('name', 'full_name', 'bio')}),
        ("Игровые характеристики", {'fields': ('faction', 'rank', 'money', 'inf', 'sublocation')}),
        ("Изображения", {'fields': ('avatar', 'image',)}),
        ("Ассортимент", {'fields': ('items', 'coef_trade', 'coef_buy',)}),
    )

    list_display = ['name', 'faction', 'rank', 'avatar_adm']
