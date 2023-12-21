"""data and functions for app"""
from datetime import datetime

def getLocation():
    "Retuns location from input statment"
    data = getData()
    location = ''
    while location not in data["states"]:
        location = input('Enter state: ')

        # To speed up testing (remove for production version)
        if location == '':
            location = 'ny'

        if location in data["states"]:
            location = data["states"][location]
            break
        print('Not a state \nStates: ny, nj, pa, fl \nPlease pick one from the list')
    return location

def getDate():
    "returns current date"
    now = datetime.now()
    date = now.strftime("%m/%d/%Y")
    return date

def getTime():
    "return current Time"
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return time

def storeData(data, itemData, cur, location, agent, agentCode):
    "Stores scanned data into database"
    for v in itemData.values():
        scanAgent = agent
        scanAgentCode = agentCode
        scanLocation = location
        barcode = v["barcode"]
        name = v["name"]
        quantity = v["quantity"]
        scanDate = v["scan_date"]
        scanTime = v["scan_time"]

        cur.execute(data["insertItems"],
            (scanAgent, scanAgentCode, scanLocation, barcode, name, quantity, scanDate, scanTime))
