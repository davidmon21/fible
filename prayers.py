import json
from typing import DefaultDict

class Prayers:
    with open('prayers.json', 'r') as f:
        prayer_data = json.load(f)
    prayers = prayer_data

    def compile_prayer(self,name,supplemental):
        prayer = DefaultDict()
        prayer["name"] = self.prayer_data[name]["NiceName"]
        prayer["text"]=[]
        for key,item in self.prayer_data[name]["Order"].items():
            if key == "self":
                prayer["text"]+=[self.prayer_data[name][key]]*item
            else:
                prayer["text"]+=self.compile_prayer(key,supplemental)["text"]*item
        return prayer





