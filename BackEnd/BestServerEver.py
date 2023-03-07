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
        print("code accept")
        filter_data = dict(filter(checker.filtering_function,request.json.items()))
        checker.writelog(filter_data)
        if request.json["type"]=="light":
            print("forward light")
            response = requests.request("POST", "http://10.83.126.107:5001/send", headers={'Content-Type': 'application/json'}, json=filter_data)
        elif request.json["type"]=="roomoccupancy":
            print("forward occupancy")
            response = requests.request("POST", "http://10.83.126.107:5002/send", headers={'Content-Type': 'application/json'}, json=filter_data)
        elif request.json["type"]=="temp":
            print("forward temp")
            response = requests.request("POST", "http://10.83.126.107:5003/send", headers={'Content-Type': 'application/json'}, json=filter_data)
        response = jsonify({"message":"ok"})
    else : 
        response = jsonify({"message":"fail !!"})
        print("code reject !!")
    response.status_code = 201
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug= True)