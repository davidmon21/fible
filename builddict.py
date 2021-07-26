import json

events = {}
events["Jesus of Nazareth"] = ["4 BC -  33 AD", "Most scholars agree he existed in some manner historically.  Galilean Jew that traveled around Israel preaching a new radical form of Judaism. Crucified by Pontius Pilated. No matter the validity of his existence, Judaism and the religion surrounding him shaped the Middle Ages."]
events["Diocletianic Persecution"] = ["303 AD - 313 AD", "Emperors Diocletian, Maximian, Galerius, and Constantius issued a series of edicts rescinding Christians' legal rights and demanding that they comply with traditional religious practices."]
events["Constatine"] = ["272 AD - 337 AD", "Established Constantinople which would become the Center of Christianity for 1000+ years. Declared the Christian God as his Divine Gaurdian when he took power. Developed the Edict of Milan ending persecution of the Christians and Other religions and cults within Rome. Appointed Christians in High Ranking Offices. Helped establish Christian Orthodoxy. Is said to have been Baptised On His Death bed. "]
with open('events.json', 'w') as f:
    json.dump(events, f)

with open('events.json', 'r') as f:
    loaded_events = json.load(f)

print(loaded_events)
