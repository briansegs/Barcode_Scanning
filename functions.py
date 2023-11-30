"""data and functions for app"""
import json
from datetime import datetime

def getData():
    "gets data from local json file"
    dataFile = "data.json"
    with open(dataFile, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()
    return data

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

def getAgent():
    "Retuns agent from input statment"
    # TODO: Scan a barcode to find agent name
    data = getData()
    agent = ''
    while agent not in data["agents"]:
        agent = input('Enter your agent code: ')

        # To speed up testing (remove for production version)
        if agent == '':
            agent = '1'

        if agent in data["agents"]:
            agent = data["agents"][agent]
            break
        print('Agent not found')
    return agent

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

def storeData(data, itemData, cur, location, agent):
    "Stores scanned data into database"
    for v in itemData.values():
        scanAgent = agent
        scanLocation = location
        barcode = v["barcode"]
        barType = v["bar_type"]
        scanDate = v["scan_date"]
        scanTime = v["scan_time"]

        cur.execute(data["insertItems"],
            (barcode, barType, scanAgent, scanLocation, scanDate, scanTime))
