from django import template
from django.contrib.auth import get_user_model

register = template.Library()
User = get_user_model()


@register.filter("check")
def check(value, user_id):
    user = User.objects.get(id=user_id)

    slots = [user.slot1, user.slot2, user.slot3, user.armor]
    quantity = value.quantity
    for el in slots:
        if el is not None:
            if value.id is el.id:
                quantity -= 1
    return quantity


@register.simple_tag()
def assign(obj):
    """
    Alias Tag
    """
    return obj
