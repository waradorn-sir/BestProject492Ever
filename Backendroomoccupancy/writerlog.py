import json
def writelog(obj):
    print(obj)
    with open("./Backendlight/logroomoccupancy.json") as datafile:
        fett = json.load(datafile)
    fett.append(obj)
    with open("./Backendlight/logroomoccupancy.json", "w") as outfile:
        json.dump(fett, outfile, indent=4, separators=(",",": "))