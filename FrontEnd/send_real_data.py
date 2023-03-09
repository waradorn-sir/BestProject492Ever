import numpy as np
import datetime
import time
import json
import requests
import hashbrown as hashb


def send_packet_real(packet,key): # for send real packet
    print("send !!")
    packet["code"] = hashb.hash(key[np.random.randint(0,len(key))]) # append real hash code
    response = requests.request("POST", "http://10.83.124.165:5000/send", headers={'Content-Type': 'application/json'}, json=packet) #send data to server
    print(response.text) # show response from server


def write_old_data(typedata,rawdata): # write new data from sensors to log sensor file
    with open(f'./{typedata}.json') as datafile: # load data before append
        fett = json.load(datafile) # store data in fett(variable)
        fett.append(rawdata) # append new data to fett(variable)
    with open(f'./{typedata}.json', "w") as outfile: # load file in write mode
        json.dump(fett, outfile, indent=4, separators=(",",": ")) # convert list object {fett(variable)} to json format for write to log file(JSON file)


def collectdata(rawdata): # classify data type
    if rawdata["type"] == "light" :
        write_old_data("olddatalight",rawdata) # call write_old_data ^ for write light data log
    elif rawdata["type"] == "occupancy" :
        write_old_data("olddataroomoccupancy",rawdata) # call write_old_data ^ for write dataroomoccupancy data log
    elif rawdata["type"] == "temp" :
        write_old_data("olddatatemp",rawdata) # call write_old_data ^ for write temp data log
    print("success !")


def load_data(): # load all data
    with open('rawdata.json') as datafile:
            raw_datastore = json.load(datafile)
    return raw_datastore #return all data


if __name__ == "__main__":
    key = ["0000","0001","0010","0011"]
    raw_datastore = load_data()
    collectdata(raw_datastore[0])
    send_packet_real(raw_datastore[0],key)