"""
VARIABLES.PY - file with variables of that app.
It's was created with goal to doesn't forget main words and tags of project and save all.
"""
from .models import News, Article, File, Mod, ImageGallery, Guide


class Vars:
    def __init__(self, name="", name_plural="", model=None):
        self.name = name
        self.name_plural = name_plural
        self.model = model

    def get_name(self):
        return self.name_plural

    def set_name(self, value):
        self.name_plural = value

    def count(self):
        return self.model.objects.all().count()

    def mainURL(self):
        return "{0}/".format(self.name_plural)

    def detailURL(self):
        return "{0}/".format(self.name)

    def addURL(self):
        return "{0}/add/".format(self.name_plural)

    def editURL(self):
        return "{0}/edit/".format(self.name_plural)

    def editGalleryURL(self):
        return "{0}/edit_gallery/".format(self.name_plural)

    def delURL(self):
        return "{0}/del/".format(self.name_plural)


NEWS = Vars('news', 'news', News)
ARTICLES = Vars('article', 'articles', Article)
FILES = Vars('file', 'files', File)
MODS = Vars('mod', 'mods', Mod)
IMAGE_GALLERY = Vars('image', 'gallery', ImageGallery)
GUIDES = Vars('guide', 'guides', Guide)
FAQ = Vars('answer', 'faq', Guide)
