import numpy as np
import datetime
import time
import json
import requests
import hashbrown as hashb
from scipy.stats import expon
import datetime

def generate_waiting_time():
    avg_waiting_time = 15 # set average waiting time
    random_time = round(expon.rvs(scale=avg_waiting_time,size=1)[0],2) #random number by exponential distribution [second] (if want minute *60)
    print(f'Waiting time : {random_time}')
    return random_time

def send_packet_fake(send_data): #for send fake packet
    print(f'Send data at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    index = np.random.randint(0,len(send_data)) # random index for send random data
    send_data[index]["code"] = hashb.hash(str(np.random.randint(1000,9999))) # append fake code
    send_data[index]["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # append current tine
    response = requests.request("POST", "http://192.168.21.211:5000/send", json=send_data[index],headers={"Content-Type": "application/json"}) #send data to server
    print(response.text) # show response from server



def load_data(): # load all data
    with open('OldDataSwitch.json') as datafile:
            datastorelight = json.load(datafile)
    with open('OldDataMotion.json') as datafile:
            datastoreroom = json.load(datafile)
    return datastoreroom,datastorelight #return all data

if __name__ == "__main__":
    while True :  # loop for use random algorithm to send fake packet
        datastoreroom, datastorelight= load_data() # fetch data
        rand_data = [datastorelight,datastoreroom]
        index_for_random_send = np.random.randint(0,len(rand_data)) # random for choose light data or motion data
        send_packet_fake(rand_data[index_for_random_send]) # send fake packet 
        time.sleep(generate_waiting_time()) # wait for send new fake packet
   
