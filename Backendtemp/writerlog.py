import json
def writelog(obj):
    print(obj)
    with open("./Backendtemp/logtemp.json") as datafile:
        fett = json.load(datafile)
    fett.append(obj)
    with open("./Backendtemp/logtemp.json", "w") as outfile:
        json.dump(fett, outfile, indent=4, separators=(",",": "))