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
        "deviceName":"temp_living_room",
        "deviceId":"017EE55C",
        "deviceType":"Temperature-Sensor",
        "gatewayName":"PRGW-123",
        "location":"living-room",
        "dBm":"-80",
        "security":"Yes",
        "temperature":{
            "value":20,
            "unit":"C"
        },
        "supplyVoltage":{
            "value":3.3,
            "unit":"V"
        }
    }
    obj_temp["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    obj_temp["temperature"]['value'] = np.random.randint(18,30)
    obj_temp["type"] = "temp"
    return obj_temp


def create_switch_data():
    obj_light = {
        "timestamp":"",
        "deviceName":"switch1",
        "deviceId":"01MIS55C",
        "deviceType":"Switch-Sensor",
        "gatewayName":"PRGW-123",
        "location":"living room",
        "dBm":"-80",
        "security":"Yes",
        "interaction":True,
        "supplyVoltage":{
            "value":3.3,
            "unit":"V"
        }
    }
    obj_light["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    obj_light["type"] = "switch"
    return obj_light


def create_motion_data():
    obj_motion = {
        "timestamp":"",
        "deviceName":"motion1",
        "deviceId":"019EE55C",
        "deviceType":"Motion-Sensor",
        "gatewayName":"PRGW-123",
        "location":"living-room",
        "dBm":"-80",
        "security":"Yes",
        "motionDetected": True, 
        "supplyVoltage":{
            "value":3.3,
            "unit":"V"
        }
    }
    obj_motion["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    obj_motion["type"] = "motion"
    return obj_motion

