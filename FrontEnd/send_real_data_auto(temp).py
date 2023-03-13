import numpy as np
import datetime
import time
import json
import requests
import hashbrown as hashb
import GenerateData as gen


def send_packet_real(packet,key): # for send real packet
    print(f'Send data at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    packet["code"] = hashb.hash(key[np.random.randint(0,len(key))]) # append real hash code
    response = requests.request("POST", "http://192.168.21.211:5000/send", headers={'Content-Type': 'application/json'}, json=packet) #send data to server
    print(response.text) # show response from server


def write_old_data(rawdata : dict): # write new data from sensors to log sensor file
    with open('./OldDataTemp.json') as datafile: # load data before append
        fett = json.load(datafile) # store data in fett(variable)
    fett.append(rawdata) # append new data to fett(variable)
    with open('./OldDataTemp.json', "w") as outfile: # load file in write mode
        json.dump(fett, outfile, indent=4, separators=(",",": ")) # convert list object {fett(variable)} to json format for write to log file(JSON file)




if __name__ == "__main__":
    while True :
        key = ["0000","0001","0010","0011"]
        raw_datastore = gen.create_temp_data()
        write_old_data(raw_datastore)
        send_packet_real(raw_datastore,key)
        time.sleep(10) # wait 10 minutes 