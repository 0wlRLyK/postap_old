from django.contrib import admin

from . import models as equip


# ITEM

@admin.register(equip.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'mass', 'icon_admin')
    search_fields = ('id', 'name', 'description', 'cost')
    ordering = ('id',)


# AMMO


@admin.register(equip.Ammo)
class AmmoAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'mass', 'quantity', 'icon_admin')
    search_fields = ('name', 'description', 'cost')


# ADD ON

@admin.register(equip.Addon)
class AddonAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'mass', 'icon_admin')
    search_fields = ('name', 'description', 'cost')


# ADD ON

@admin.register(equip.AddonOutfit)
class AddonOutfitAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'mass', 'icon_admin')
    search_fields = ('name', 'description', 'cost')


# Weapon

@admin.register(equip.Weapon)
class WeaponAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Дескрипт", {
            'fields': ('name', 'icon', 'description', 'cost', 'mass')
        }),
        ("Характеристики оружия", {
            'fields': ('sort', 'one_handed', 'accuracy', 'damage', 'convenience', 'pace_of_fire', 'capacity')
        }),
        ("Патроны и аддоны", {
            'fields': ('ammo_type', 'addons', 'addon1open', 'addon2open', 'addon3open')
        }),
        ("Уникальность", {
            'fields': ('unique',)
        }),
    )
    list_display = ('name', 'sort', 'one_handed', 'cost', 'mass', 'icon_admin')
    search_fields = ('name', 'description', 'cost')
    list_filter = ['sort', 'one_handed']


# OUTFIT

@admin.register(equip.Outfit)
class OutfitAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Дескрипт", {
            'fields': ('name', 'icon', 'equipped_icon', 'description', 'cost', 'mass')
        }),
        ("Вид, шлем, колличество контейнеров, прочее", {
            'fields': ('sort', 'helmet_built_in', 'containers', 'weight', 'running',)
        }),
        ("Характеристики костюма", {
            'fields': ('ballistic', 'burst', 'kick', 'explosion', 'thermal', 'electrical', 'chemical', 'radioactive',
                       'psi')
        }),
        ("Уникальность", {
            'fields': ('unique',)
        }),
    )
    list_display = ('name', 'sort', 'running', 'cost', 'mass', 'icon_admin', 'equipped_icon_admin')
    search_fields = ('name', 'description', 'cost')
    list_filter = ['sort', 'containers', 'running']


# HELMET

@admin.register(equip.Helmet)
class HelmetAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Дескрипт", {
            'fields': ('name', 'icon', 'description', 'cost', 'mass')
        }),
        ("Характеристики шлема", {
            'fields': ('ballistic', 'burst', 'kick', 'explosion', 'thermal', 'electrical', 'chemical', 'radioactive',
                       'psi')
        }),
        ("Уникальность", {
            'fields': ('unique',)
        }),
    )
    list_display = ('name', 'sort', 'cost', 'mass', 'icon_admin')
    search_fields = ('name', 'description', 'cost')
    list_filter = ['sort']


# BACKPACK

@admin.register(equip.Backpack)
class BackpackAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'weight', 'mass', 'icon_admin')
    search_fields = ('name', 'description', 'cost')


# DEVICE

@admin.register(equip.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'sort', 'actions', 'slot_setting', 'mass', 'icon_admin')
    search_fields = ('name', 'description', 'cost')


# FOOD AND MEDICINE

@admin.register(equip.FoodAndMedicine)
class FoodAndMedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'actions', 'mass', 'icon_admin')
    search_fields = ('name', 'description', 'cost')


# Misc

@admin.register(equip.Misc)
class MiscAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'mass', 'icon_admin')
    search_fields = ('name', 'description', 'cost')


# ARTIFACT

@admin.register(equip.Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'mass', 'icon_admin')
    fieldsets = (
        ("Дескрипт", {
            'fields': ('name', 'icon', 'description', 'cost', 'mass', 'sort',)
        }),
        ("Характеристики костюма", {
            'fields': ('ballistic', 'burst', 'kick', 'explosion', 'thermal', 'electrical', 'chemical', 'radioactive',
                       'psi', 'weight', 'healing', 'satiety', 'energy')
        }),
    )
    search_fields = ('name', 'description', 'cost')


# QuestItem

@admin.register(equip.QuestItem)
class QuestItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'mass', 'icon_admin')
    search_fields = ('name', 'description', 'cost')


# EQUIP_ITEM

@admin.register(equip.EquipItem)
class EquipItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'quantity', 'condition', 'cost')
    search_fields = ('name',)
    list_filter = ['name']
