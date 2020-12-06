from django import template

register = template.Library()


@register.filter
def in_list(value, the_list):
    value = str(value)
    return value in the_list.split(',')


@register.filter
def get_uf(user, field):
    """Get User Field"""
    return user.field


@register.filter
def get_ufid(user, field):
    """Get User Field from ID for label"""
    field = str(field[3:])
    return user.field.value
