import random
import json

with open('data.json') as datafile:
        datastore = json.load(datafile)

# Initialize variables
padStart = 0
padEnd = 0

def decisionFn(q, prev_activity):
    return random.random() < q

# Function to inject fake traffic at the padding rate R
def padTraffic(R):
    # code inject fake traffic
    #TODO
    # print("padingpadingpadingpadingpadingpadingpadingpadingpadingpadingpadingpading")
    pass

# Function check if user activity occurr in current time
def userActivityOccurring(t):
    # code to check for user activity
    # return true if user activity occur at time t,otherwise false 
    return random.random() < 0.5

def STP(t, q, T, R):
    global padStart, padEnd
    
    # Check if it's time to pad
    if t % T == 0 and decisionFn(q, ...):
        # Generate a random offset within the padding period
        padOffset = random.uniform(0, T)
        if t + padOffset > padEnd:
            # Start a new padding interval
            padStart = t + padOffset
            padEnd = padStart + T
        else:
            # Continue the current padding interval
            padEnd += T
        
        # Inject fake traffic if the current time is within the padding interval
        if padStart <= t <= padEnd:
            padTraffic(R)
        
    # Start a new padding interval if user activity is occurring
    elif userActivityOccurring(t):
        padStart = t
        padEnd = t + T
        padTraffic(R)

STP(1,1,1,1)


print(datastore[0])








# import random

# # Initialize variables
# padStart = 0
# padEnd = 0

# # Function to generate a random Boolean based on the probability q and previous user activity
# def decisionFn(q, prev_activity):
#     return random.random() < q

# # Function to inject fake traffic at the padding rate R
# def padTraffic(R):
#     # code to inject fake traffic goes here
#     #TODO
#     print("padingpadingpadingpadingpadingpadingpadingpadingpadingpadingpadingpading")
#     # pass

# # Function to check if user activity is occurring at the current time
# def userActivityOccurring(t):
#     # code to check for user activity goes here
#     # return True if user activity is occurring at time t, False otherwise
#     return random.random() < 0.5

# def STP(t, q, T, R):
#     global padStart, padEnd
    
#     # Check if it's time to pad
#     if t % T == 0 and decisionFn(q, ...):
#         # Generate a random offset within the padding period
#         padOffset = random.uniform(0, T)
#         if t + padOffset > padEnd:
#             # Start a new padding interval
#             padStart = t + padOffset
#             padEnd = padStart + T
#         else:
#             # Continue the current padding interval
#             padEnd += T
        
#         # Inject fake traffic if the current time is within the padding interval
#         if padStart <= t <= padEnd:
#             padTraffic(R)
        
#     # Start a new padding interval if user activity is occurring
#     elif userActivityOccurring(t):
#         padStart = t
#         padEnd = t + T
#         padTraffic(R)

# # STP(1,1,1,1)



#ภาษาไทย

# import random

# # กำหนดตัวแปรเริ่มต้น
# padStart = 0
# padEnd = 0

# # ฟังก์ชันสำหรับสุ่มค่า Boolean โดยใช้ความน่าจะเป็น q และกิจกรรมก่อนหน้านี้
# def decisionFn(q, prev_activity):
#     return random.random() < q

# # ฟังก์ชันสำหรับเพิ่มการเข้าชมเทียบกับอัตราการเข้าชมปกติที่อยู่ในอัตราส่วน R
# def padTraffic(R):
#     # โค้ดสำหรับเพิ่มการเข้าชมเทียบกับอัตราการเข้าชมปกติจะอยู่ที่นี่
#     #TODO
#     print("padingpadingpadingpadingpadingpadingpadingpadingpadingpadingpadingpading")
#     # pass

# # ฟังก์ชันสำหรับตรวจสอบว่ามีกิจกรรมของผู้ใช้ที่เกิดขึ้นในเวลาปัจจุบันหรือไม่
# def userActivityOccurring(t):
#     # โค้ดสำหรับตรวจสอบกิจกรรมของผู้ใช้จะอยู่ที่นี่
#     # ส่งคืน True หากมีกิจกรรมของผู้ใช้เกิดขึ้นในเวลา t และ False ในกรณีอื่นๆ
#     return random.random() < 0.5

# def STP(t, q, T, R):
#     global padStart, padEnd
    
#     # ตรวจสอบว่าถึงเวลาเพิ่มการเข้าชมเทียบกับอัตราการเข้าชมปกติหรือไม่
#     if t % T == 0 and decisionFn(q, ...):
#         # สร้างการเลื่อนแบบสุ่มภายในช่วงการเพิ่มการเข้าชมเทียบกับอัตราการเข้าชมปกติ
#         padOffset = random.uniform(0, T)
#         if t + padOffset > padEnd:
#             # เริ่มช่วงการเพิ่มการเข้าชมเทียบกับอัตราการเข้าชมปกติใหม่
#             padStart = t + padOffset
#             padEnd = padStart + T