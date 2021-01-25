from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from . import models as users
from .forms import CustomUserCreationForm


class SiteUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = users.SiteUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'avatar', 'birthday', 'gender', 'country',
                                         'city', 'signature', 'sign_image')}),
        ('Игровые характеристики', {
            'fields': ('faction', 'speciality', 'rank', 'xp', 'level', 'money', 'reputation', 'hp', 'rad',
                       'satiety'),
        }),
        (_('Equipment'), {
            'fields': ('slot1', 'slot2', 'slot3', 'armor', 'helmet', 'backpack', 'device1', 'device2', 'device3',
                       'belt1', 'belt2', 'belt3', 'belt4', 'container1', 'container2', 'container3', 'container4',
                       'container5'),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_online', 'last_login', 'date_joined')}),
    )
    list_display = ['email', 'username']
    # fields = ('username', 'email', 'avatar', 'birthday', 'gender', 'country', 'city', 'signature', 'sign_image',
    #           'rpl_nickname', 'rpl_first_name', 'rpl_second_name', 'rpl_avatar', 'rpl_bio', 'speciality', 'rpl_xp',
    #           'rpl_lvl', 'rank', 'hp', 'rad', 'satiety', 'reputation', 'money', 'xp', 'level', 'equipment')


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


admin.site.unregister(get_user_model())
admin.site.register(users.SiteUser, SiteUserAdmin)
