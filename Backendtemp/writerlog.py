import json

def writelog(obj):
    with open("./LogTemp.json") as datafile:
        fett = json.load(datafile)
    fett.append(obj)
    with open("./LogTemp.json", "w") as outfile:
        json.dump(fett, outfile, indent=4, separators=(",",": "))