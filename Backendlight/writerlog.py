import json
def writelog(obj):
    print(obj)
    with open("./Backendlight/loglight.json") as datafile:
        fett = json.load(datafile)
    fett.append(obj)
    with open("./Backendlight/loglight.json", "w") as outfile:
        json.dump(fett, outfile, indent=4, separators=(",",": "))