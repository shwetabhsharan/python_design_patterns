# -*- coding: utf-8 -*-
"""
Create object without exposing the creation logic to
the client and refer to newly created object using a
common interface
"""

class GreekGetter(object):
    """
    A simple localizer a la gettext
    """

    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        """
        We'll get screwed if we don't have a translation
        """
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):
    """
    Simply echoes the msg ids
    """

    def get(self, msgid):
        return str(msgid)


def get_localizer(language):
    """
    The factory method
    """

#     if language == "English":
#         return EnglishGetter()
# 
#     if language == "Green":
#         return GreekGetter()

    languages = dict(English=EnglishGetter, Greek=GreekGetter)

    return languages[language]()

e = get_localizer(language="English")
g = get_localizer(language="Greek")

for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))
