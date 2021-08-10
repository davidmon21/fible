import json
from typing import DefaultDict

class Prayers:
    with open('prayers.json', 'r') as f:
        prayer_data = json.load(f)
    prayers = prayer_data.keys()

    def compile_prayer(self,name,supplemental):
        prayer = DefaultDict()
        prayer["name"] = self.prayer_data[name]["NiceName"]
        prayer["text"]=""
        for item in self.prayer_data[name]["Order"]:
            if item == "self":
                prayer["text"]+=self.prayer_data[name]["self"]+"\n"
            else:
                prayer["text"]+=self.prayer_data[item]["self"]+"\n"
        return prayer





