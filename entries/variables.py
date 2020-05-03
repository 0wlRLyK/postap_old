"""
VARIABLES.PY - file with variables of that app.
It's was created with goal to doesn't forget main words and tags of project and save all.
"""
from .models import EntryNews, EntryArticle, EntryFile


class Vars:
    def __init__(self, name="", model=None):
        self.name = name
        self.model = model

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def count(self):
        return self.model.objects.all().count()

    def mainURL(self):
        return "{0}/".format(self.name)

    def addURL(self):
        return "{0}/add/".format(self.name)

    def editURL(self):
        return "{0}/edit/".format(self.name)

    def editGalleryURL(self):
        return "{0}/edit_gallery/".format(self.name)

    def delURL(self):
        return "{0}/del/".format(self.name)


NEWS = Vars('news', EntryNews)
ARTICLES = Vars('articles', EntryArticle)
FILES = Vars('files', EntryFile)
