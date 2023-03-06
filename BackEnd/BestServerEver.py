# save this as app.py
from flask import Flask,request,jsonify
import requests
import json
import checker
app = Flask(__name__)

@app.route("/")
def hello():
    return "Don't Hack Me"

@app.route("/send", methods=['POST'])
def hear():
    if checker.check(request.json["code"]):
        rawdata = checker.actualdata(request.json)
        checker.writelog(rawdata)
        if request.json["type"]=="light":
            response = requests.request("POST", "http://10.83.124.42:5001/send", headers={'Content-Type': 'application/json'}, data=json.dumps(request.json))
        elif request.json["type"]=="roomoccupancy":
            response = requests.request("POST", "http://10.83.124.42:5002/send", headers={'Content-Type': 'application/json'}, data=json.dumps(request.json))
        elif request.json["type"]=="temp":
            response = requests.request("POST", "http://10.83.124.42:5002/send", headers={'Content-Type': 'application/json'}, data=json.dumps(request.json))
    print(request.json["code"])
    response = jsonify({"message":"ok"})
    response.status_code = 201
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug= True)