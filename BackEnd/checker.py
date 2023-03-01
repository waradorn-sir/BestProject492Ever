import json

def check(incomingkey:str):
    with open("./BackEnd/ValidateKey.json") as datafile:
        realkey = json.load(datafile)
    for i in realkey:
        if i["key"] == incomingkey:
            return True
    return False

def writelog(obj):
    json_object = json.dumps(obj, indent=4)
    with open("./BackEnd/logdata.json", "w") as outfile:
        outfile.write(json_object)
                