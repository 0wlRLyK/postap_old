from django.contrib import admin

from . import models as vote


# ------------
#  Inlines
# ------------

class ChoiceInline(admin.StackedInline):
    model = vote.Choice
    extra = 3


class ModChoiceInline(admin.StackedInline):
    model = vote.ModChoice
    extra = 3


class VoteInline(admin.StackedInline):
    model = vote.Vote
    extra = 3


# ------------
# //////--------
# POLLS: ОПРОСЫ
# //////--------


@admin.register(vote.PollCategories)
class CategoriesPollAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(vote.Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['title', 'category', ]
    search_fields = ['title', 'category', 'pub_date']


# ////////////--------------------
# MOD VOTING: ГОЛОСОВАНИЕ ЗА МОДЫ
# ////////////--------------------


@admin.register(vote.ModVotingCategories)
class CategoriesModVotingAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(vote.ModVoting)
class ModVotingAdmin(admin.ModelAdmin):
    inlines = [ModChoiceInline]
    list_display = ['title', 'category', ]
    search_fields = ['title', 'category', 'pub_date']


# ////////--------
# VOTING: ГОЛОСОВАНИЕ
# ////////--------


@admin.register(vote.VotingCategories)
class CategoriesVotingAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


@admin.register(vote.Voting)
class VotingAdmin(admin.ModelAdmin):
    inlines = [VoteInline]
    list_display = ['title', 'category', ]
    search_fields = ['title', 'category', 'pub_date']
