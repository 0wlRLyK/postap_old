from ajax_select import register, LookupChannel

from .models import UsersProfiles


@register('users')
class TagsLookup(LookupChannel):
    model = UsersProfiles

    def get_query(self, q, request):
        return self.model.objects.filter(citi=q).order_by('name')[:50]

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.name
