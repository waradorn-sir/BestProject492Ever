# save this as app.py
from flask import Flask,request,jsonify
import writerlog
app = Flask(__name__)

@app.route("/")
def hello():
    return "Server Temp"

@app.route("/send", methods=['POST'])
def hear():
    writerlog.writelog(request.json)
    response = jsonify({"message":"ok"})
    response.status_code = 202
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003,debug= True)