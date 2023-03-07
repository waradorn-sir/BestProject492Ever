import json

def check(incomingkey:str):
    with open("./ValidateKey.json") as datafile:
        realkey = json.load(datafile)
    for i in realkey:
        if i["key"] == incomingkey:
            return True
    return False

def writelog(obj):
    # print(obj)
    with open("./logdata.json") as datafile:
        fett = json.load(datafile)
    fett.append(obj)
    with open("./logdata.json", "w") as outfile:
        json.dump(fett, outfile, indent=4, separators=(",",": "))
                
def filtering_function(pair):
    unwanted_key = 'code'
    key, value = pair
    if key == unwanted_key:
        return False  # filter pair out of the dictionary
    else:
        return True  # keep pair in the filtered dictionary
    