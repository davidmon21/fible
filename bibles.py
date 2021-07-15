from typing import DefaultDict
from pysword.modules import SwordModules
from pysword.bible import SwordBible
import pysword

class Bibles:
    open_bible = None
    bible_collection = None
    sword = None
    def __init__(self, bibles_path):
        self.sword = SwordModules(bibles_path)
        self.bible_collection = self.sword.parse_modules()

    def collection(self):
        return self.bible_collection
    
    def ready_bible(self,version):
        self.open_bible = self.sword.get_bible_from_module(version)
        return self.open_bible
    
    def _populate(self):
        pass

    def return_books(self):
        return self.open_bible.get_structure().get_books()
