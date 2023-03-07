import json
from datetime import datetime
import numpy as np
import time

datalight = "./Front/datalight.json"
dataroomoccupancy = "./Front/dataroomoccupancy.json"
datatemp = "./Front/datatemp.json"



def create_temp_data():
    obj_temp ={
        "timestamp":"",
        "deviceName":"living room",
        "deviceId":"019EE55C",
        "deviceType":"Temperature-Sensor",
        "gatewayName":"PRGW-123",
        "location":"bed room",
        "dBm":"-80",
        "security":"No",
        "temperature":{
            "value":20,
            "unit":"C"
        }
    }
    obj_temp["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    obj_temp["temperature"]['value'] = np.random.randint(18,30)
    obj_temp["type"] = "temp"
    return obj_temp


def create_light_data():
    obj_light = {
        "timestamp":"",
        "deviceName":"LuxSensor",
        "deviceId":"01MIS55C",
        "deviceType":"Light-Sensor",
        "gatewayName":"PRGW-123",
        "location":"living room",
        "dBm":"-80",
        "security":"No",
        "illumination":{
            "value":544,
            "unit":"lx"
        },
        "supplyVoltage":{
            "value":3.3,
            "unit":"V"
        }
    }
    obj_light["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    obj_light["illumination"]['value'] = np.random.randint(150,200)
    obj_light["type"] = "light"
    return obj_light


def create_occupancy_data():
    obj_room = {
        "timestamp":"",
        "deviceName":"occupancy",
        "deviceId":"019EE55C",
        "deviceType":"Occupancy-PIR",
        "gatewayName":"PRGW-123",
        "location":"living room",
        "dBm":"-80",
        "security":"No",
        "motionDetected": True, 
        "supplyVoltage":{
            "value":3.3,
            "unit":"V"
        }
    }
    obj_room["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # obj_room["motionDetected"] = np.random.randint(150,200)
    obj_room["type"] = "occupancy"
    return obj_room

def write_data(rawdata): # write new data from sensors to log sensor file
    with open(f'./FrontEnd/rawdata.json') as datafile: # load data before append
        fett = json.load(datafile) # store data in fett(variable)
        fett.append(rawdata) # append new data to fett(variable)
    with open(f'./FrontEnd/rawdata.json', "w") as outfile: # load file in write mode
        json.dump(fett, outfile, indent=4, separators=(",",": ")) # convert list object {fett(variable)} to json format for write to log file(JSON file)

if __name__ == "__main__":
    # c = 0
    # while c < 500 :
    #     if c%5 == 0 :
    #         write_data(create_temp_data())
    #     if c < 100 and c%4 == 0 :
    #         write_data(create_occupancy_data())
    #     if c > 400 and c%4 == 0:
    #         write_data(create_occupancy_data())
    #     if c == 100 or c == 400 or c == 490 :
    #         write_data(create_light_data)
    #     time.sleep(2)
    #     c += 1
    print(create_light_data())