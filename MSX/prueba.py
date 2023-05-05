import json

with open("msx.json") as juegos:
    data = json.load(juegos)

for i in data:
    print()