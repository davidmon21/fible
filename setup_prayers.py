import json

prayers = {
    "OurFather": {
        "Order": ["self"],
        "Supplemental": [],
        "self": "Our Father, who art in heaven hallowed be thy name; thy kingdom come; thy will be done on earth as it is in heaven. Give us this day our daily bread and forgive us our trespasses as we forgive those who trespass against us; and lead us not into temptation, but deliver us from evil. Amen."
    },
    "EternelFather": {
        "Order": ["self"],
        "Supplemental": [],
        "self": "Eternal Father, I offer you the Body and Blood, Soul and Divinity of Your Dearly Beloved Son, Our Lord, Jesus Christ, in atonement for our sins and those of the whole world."
    }
}

out_file = open("prayers.json", "w") 
json.dump(prayers, out_file)