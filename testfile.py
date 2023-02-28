import numpy as np
import datetime
import time
import json
import requests


with open('datatemp.json') as datafile:
        datastoretemp = json.load(datafile)
with open('datalight.json') as datafile:
        datastorelight = json.load(datafile)
with open('dataroomoccupancy.json') as datafile:
        datastoreroom = json.load(datafile)
with open('datareal.json') as datafile:
        datastorereal = json.load(datafile)

url = "http://10.81.64.116:5000/send"


headers = {
  'Content-Type': 'application/json'
}

def sleep_test(datastore,datastorefake,flag):
    start = time.time()
    x = datetime.datetime.now()
    a = np.random.randint(0,9)
    while a != int(x.strftime("%S"))%10 :
        x = datetime.datetime.now()
        #print(int(x.strftime("%S"))%10)
    end = time.time()
    print("Waiting Time",end - start)
    if flag:
        datastore[0]["code"]= [0000,0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1111]
        start_process = time.time()
        payload = json.dumps(datastore[np.random.randint(0,len(datastore))])
        payloadfake = json.dumps(datastorefake[np.random.randint(0,len(datastore))])
        responsefake = requests.request("POST", url, headers=headers, data=payloadfake)
        response = requests.request("POST", url, headers=headers, data=payload)
        end_process = time.time()
        print(responsefake.text)
        print("Fake Transfer Time",(end_process-start_process)*1000)
    else:
        start_process = time.time()
        payload = json.dumps(datastorefake[np.random.randint(0,len(datastorefake))])
        response = requests.request("POST", url, headers=headers, data=payload)
        end_process = time.time()
        print("Transfer Time",(end_process-start_process)*1000)
    print(response.text)

randdata = [datastoretemp,datastorelight,datastoreroom] 
ran = np.random.randint(0,5)
for i in range(5):
    if ran == i:
        sleep_test(datastorereal,randdata[np.random.randint(0,3)],1)
    else:
        sleep_test([],randdata[np.random.randint(0,3)],0)
       



