import json
def writelog(obj):
    with open("./loglight.json") as datafile:
        fett = json.load(datafile)
    fett.append(obj)
    with open("./loglight.json", "w") as outfile:
        json.dump(fett, outfile, indent=4, separators=(",",": "))