import numpy as np
import datetime
import json
import requests
import hashbrown as hashb
import GenerateData as gen


def send_packet_real(packet,key): # for send real packet
    print(f'Send data at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    packet["code"] = hashb.hash(key[np.random.randint(0,len(key))]) # append real hash code
    response = requests.request("POST", "http://192.168.21.211:5000/send", headers={'Content-Type': 'application/json'}, json=packet) #send data to server
    print(response.text) # show response from server


def write_old_data(typedata,rawdata): # write new data from sensors to log sensor file
    with open(f'./{typedata}.json') as datafile: # load data before append
        fett = json.load(datafile) # store data in fett(variable)
    fett.append(rawdata) # append new data to fett(variable)
    with open(f'./{typedata}.json', "w") as outfile: # load file in write mode
        json.dump(fett, outfile, indent=4, separators=(",",": ")) # convert list object {fett(variable)} to json format for write to log file(JSON file)


def collectdata(rawdata): # classify data type
    if rawdata["type"] == "light" :
        write_old_data("OldDataSwitch",rawdata) # call write_old_data ^ for write switch data log
    elif rawdata["type"] == "occupancy" :
        write_old_data("OldDataMotion",rawdata) # call write_old_data ^ for write motion data log
    print("Save success !")



if __name__ == "__main__":
    mode = input("Input IoT data type : ")
    key = ["0000","0001","0010","0011"]
    while mode != "switch" or mode != "motion" :
        if mode == "switch" or mode == "motion" :
            if mode == "switch" :
                raw_datastore = gen.create_switch_data()
            if mode == "motion" :
                raw_datastore = gen.create_motion_data()
            # print(raw_datastore)
            collectdata(raw_datastore)
            send_packet_real(raw_datastore,key)
        else :
            print(f'Undefined !!')
        mode = input("Input IoT data type : ")