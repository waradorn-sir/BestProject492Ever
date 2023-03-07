import json
def writelog(obj):
    with open("./logroomoccupancy.json") as datafile:
        fett = json.load(datafile)
    fett.append(obj)
    with open("./logroomoccupancy.json", "w") as outfile:
        json.dump(fett, outfile, indent=4, separators=(",",": "))