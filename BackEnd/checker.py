import json

def check(incomingkey:str):
    with open("./BackEnd/ValidateKey.json") as datafile:
        realkey = json.load(datafile)
    for i in realkey:
        if i["key"] == incomingkey:
            return True
    return False

def writelog(obj):
    print(obj)
    with open("./BackEnd/logdata.json") as datafile:
        fett = json.load(datafile)
    fett.append(obj)
    with open("./BackEnd/logdata.json", "w") as outfile:
        json.dump(fett, outfile, indent=4, separators=(",",": "))
                
# def actualdata(obj):
    