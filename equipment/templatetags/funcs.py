from django import template
from django.contrib.auth import get_user_model
from equipment import models as equip

register = template.Library()
User = get_user_model()


@register.filter("check")
def check(value, user_id):
    user = User.objects.get(id=user_id)

    slots = [user.slot1, user.slot2, user.slot3, user.armor, user.helmet,
             user.device1, user.device2, user.device3, user.backpack,
             user.container1, user.container2, user.container3, user.container4, user.container5]
    quantity = value.quantity
    for el in slots:
        if el is not None:
            if value.id is el.id:
                quantity -= 1
    return quantity


@register.filter("get_ids")
def get_ids(value, type):
    if value == "":
        return ""
    weapon = equip.Weapon.objects.get(id=value);
    ammo_types = weapon.ammo_type.all()
    return ",".join([str(el.id) for el in ammo_types])


@register.simple_tag()
def assign(obj):
    """
    Alias Tag
    """
    return obj
