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
        filter_data = dict(filter(checker.filtering_function,request.json.items())) #filter code ทิ้ง 
        checker.writelog(filter_data) #write ตัวที่ filter code ออก
        if request.json["type"]=="switch":
            print("forward light")
            response = requests.request("POST", "http://192.168.21.211:5001/send", headers={'Content-Type': 'application/json'}, json=filter_data)
        elif request.json["type"]=="motion":
            print("forward occupancy")
            response = requests.request("POST", "http://192.168.21.211:5002/send", headers={'Content-Type': 'application/json'}, json=filter_data)
        elif request.json["type"]=="temp":
            print("forward temp")
            response = requests.request("POST", "http://192.168.21.211:5003/send", headers={'Content-Type': 'application/json'}, json=filter_data)
        response = jsonify({"message":"ok"}) #แปลง dict ให้เป็น json
        response.status_code = 202
    else : 
        response = jsonify({"message":"fail !!"})
        print("code reject !!")
        response.status_code = 403
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug= True)