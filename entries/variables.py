"""
VARIABLES.PY - file with variables of that app.
It's was created with goal to doesn't forget main words and tags of project and save all.
"""


class Vars:
    def __init__(self, name=""):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def module_list(self):
        return "{0}/".format(self.name)

    def module_adding(self):
        return "{0}/add/".format(self.name)

    def module_editing(self):
        return "{0}/edit/".format(self.name)


NEWS = Vars('news')
