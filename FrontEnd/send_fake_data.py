import numpy as np
import datetime
import time
import json
import requests
import hashbrown as hashb

def send_packet_fake(send_data): #for send fake packet
    x = datetime.datetime.now() # get current time store in x(variable)
    a = np.random.randint(0,9) # random num 0 - 9 store in a(variable)
    while int(x.strftime("%S"))%10 != a : # compare second number with random from a(variable)
        x = datetime.datetime.now() # generate new current time ^

        # to do create exponential for check traffic intensity before send packet

    print("send")
    index = np.random.randint(0,len(send_data)) # random index for send random data
    send_data[index]["code"] = hashb.hash(str(np.random.randint(1000,9999))) # append fake code
    response = requests.request("POST", "http://192.168.21.211:5000/send", json=send_data[index],headers={"Content-Type": "application/json"}) #send data to server
    print(response.text) # show response from server



def load_data(): # load all data
    with open('datatemp.json') as datafile:
            datastoretemp = json.load(datafile)
    with open('datalight.json') as datafile:
            datastorelight = json.load(datafile)
    with open('dataroomoccupancy.json') as datafile:
            datastoreroom = json.load(datafile)
    return datastoreroom,datastorelight,datastoretemp #return all data

if __name__ == "__main__":
    # load data with fetch
    #datastoreroom,datastorelight,datastoretemp = load_data()
    while True :  # loop for use algorithm random to send fake file
        datastoreroom, datastorelight, datastoretemp = load_data()
        rand_data = [datastoretemp,datastorelight,datastoreroom]
        index_for_random_send = np.random.randint(0,len(rand_data))
        send_packet_fake(rand_data[index_for_random_send]) 
        time.sleep(1)
   
