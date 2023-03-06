import numpy as np
import datetime
import time
import json
import requests
import hashbrown as hashb


def send_packet_fake(send_data): 
    x = datetime.datetime.now()
    a = np.random.randint(0,9)
    while a != int(x.strftime("%S"))%10 :
        x = datetime.datetime.now()
        # to do create exponential for check traffic intensity before send packet
    index = np.random.randint(0,len(send_data))
    send_data[index]["code"] = hashb.hash(str(np.random.randint(1000,9999)))
    response = requests.request("POST", "http://10.83.124.42:5000/send", headers={'Content-Type': 'application/json'}, data=json.dumps(send_data))
    print(response.text)

def send_packet_real(packet,key):
    packet["code"]= hashb.hash(key[np.random.randint(0,len(key))])
    response = requests.request("POST", "http://10.83.124.42:5000/send", headers={'Content-Type': 'application/json'}, data=json.dumps(packet))
    print(response.text)


def write_old_data(typedata,rawdata):
    with open(f'./FrontEnd/{typedata}.json') as datafile:
        fett = json.load(datafile)
        fett.append(rawdata)
    with open(f'./FrontEnd/{typedata}.json', "w") as outfile:
        json.dump(fett, outfile, indent=4, separators=(",",": "))

# to do fix 
def collectdata(rawdata):
    if rawdata["type"] == "light" :
        write_old_data("datalight",rawdata)
    elif rawdata["type"] == "light" :
        write_old_data("dataroomoccupancy",rawdata)
    elif rawdata["type"] == "light" :
        write_old_data("datatemp",rawdata)


def load_data():
    with open('datatemp.json') as datafile:
            datastoretemp = json.load(datafile)
    with open('datalight.json') as datafile:
            datastorelight = json.load(datafile)
    with open('dataroomoccupancy.json') as datafile:
            datastoreroom = json.load(datafile)
    with open('rawdata.json') as datafile:
            raw_datastore = json.load(datafile)
    return raw_datastore,datastoreroom,datastorelight,datastoretemp
       
def main():
    # load data with fetch
    raw_datastore,datastoreroom,datastorelight,datastoretemp = load_data()
    key = ["0000","0001","0010"]
    # alg random for send fake file
    # create multithread to random send & send real packet
    # thread random
    # .............
    rand_data = [datastoretemp,datastorelight,datastoreroom]
    index_for_random_send = np.random.randint(0,len(rand_data))
    send_packet_fake(rand_data[index_for_random_send])
    # thread send real packet
    # .............
    send_packet_real(raw_datastore,key)

main()