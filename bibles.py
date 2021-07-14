from typing import DefaultDict
from pysword.modules import SwordModules
from pysword.bible import SwordBible
import pysword

class Bible:
    bible = None
    def __init__(self, name):
        bible_collection = Bibles("/Users/david/.sword")
        self.bible = bible_collection.get_book(name)
    
    def _populate(self):
        pass

    def return_books(self):
        return self.bible.get_structure().get_books()

class Bibles:
    bibles = DefaultDict
    configuration = DefaultDict
    modules = None
    def __init__(self, configer):
        self._process_config(configer)

    def _process_config(self, configer):
        self.modules = SwordModules(configer)
        self.modules.parse_modules()
    
    def get_book(self, name):
        return self.modules.get_bible_from_module(name)