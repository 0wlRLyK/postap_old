from django.contrib import admin

from . import models as rp


class AreaInline(admin.StackedInline):
    model = rp.Area


class SubLocationInline(admin.StackedInline):
    model = rp.SubLocation


@admin.register(rp.Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [AreaInline]
    list_display = ['name', 'icon_admin']


@admin.register(rp.Area)
class AreaAdmin(admin.ModelAdmin):
    inlines = [SubLocationInline]
    list_display = ['name', 'icon_admin']


@admin.register(rp.SubLocation)
class SubLocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'type_of_subloc', 'icon_admin']


@admin.register(rp.Trader)
class NPCTraderAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Персональные данные", {'fields': ('name', 'full_name', 'bio')}),
        ("Игровые характеристики", {'fields': ('faction', 'rank', 'money', 'inf', 'sublocation')}),
        ("Изображения", {'fields': ('avatar', 'image',)}),
        ("Ассортимент", {'fields': ('items', 'coef_trade', 'coef_buy',)}),
    )

    list_display = ['name', 'faction', 'rank', 'avatar_adm']

    @admin.register(rp.NPCMinigame)
    class NPCMinigameAdmin(admin.ModelAdmin):
        fieldsets = (
            ("Персональные данные", {'fields': ('name', 'full_name', 'bio')}),
            ("Игровые характеристики", {'fields': ('faction', 'spec', 'rank', 'money', 'inf', 'sublocation')}),
            ("Изображения", {'fields': ('avatar', 'image',)}),
            ("Ассортимент", {'fields': ('items', 'coef_trade', 'coef_buy',)}),
        )

        list_display = ['name', 'faction', 'rank', 'avatar_adm']

    @admin.register(rp.Mechanic)
    class MechanicAdmin(admin.ModelAdmin):
        fieldsets = (
            ("Персональные данные", {'fields': ('name', 'full_name', 'bio')}),
            ("Игровые характеристики", {'fields': ('faction', 'rank', 'money', 'inf', 'sublocation')}),
            ("Изображения", {'fields': ('avatar', 'image',)}),
            ("Ассортимент", {'fields': ('items', 'coef_trade', 'coef_buy', 'coef_repair')}),
        )

        list_display = ['name', 'faction', 'rank', 'avatar_adm']
