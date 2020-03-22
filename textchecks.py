import re

class SearchingPro:
    """class for searching"""

    def __init__(self):
        """initialize regex"""

        self.urlCheck = re.compile(r'http(s)?')

    def isUrl(self, text):

        if self.urlCheck.search(text) != None:
            return True
        else:
            return False

