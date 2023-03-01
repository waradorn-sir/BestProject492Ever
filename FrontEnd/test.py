import json
with open('datareal.json') as datafile:
        datastorereal = json.load(datafile)
print(datastorereal[0])
datastorereal[0]["code"]=987654
print(datastorereal[0])