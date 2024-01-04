"""data and functions for app"""
import sqlite3
from datetime import datetime
import time as t
from agent_scanner import AgentScanner
from data import (
    insertItemScan,
    getLocations,
    updatePendingDropOff,
    createItemScanTable
    )
from data import database as db

def getCursorConnection():
    "Returns cursor from database"
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    return cur, conn

def getAgent():
    "Returns: agent and agentId from database"
    aScan = AgentScanner()

    print('Scan your user ID.')
    t.sleep(1)

    try:
        agent, agentId = aScan.scanAgent()

    except TypeError:
        print('The program can not proceed without an agent.')
        t.sleep(1)
        print('Start the program over once you have an agent ID.')
        t.sleep(1)
        print('*Application shutting down...*')
        t.sleep(1)
        quit()

    return agent, agentId

def getLocation():
    "Returns location"
    cur, conn = getCursorConnection()
    res = cur.execute(getLocations)
    lst = res.fetchall()
    conn.close()

    locations = {}
    for item in lst:
        locations[item[0]] = item[1]

    while True:
        print("Enter the number of your Location: ")
        print("")
        t.sleep(1)
        for num, location in locations.items():
            print(f'    {num}. {location}')
        print("")
        t.sleep(.5)

        try:
            opt = int(input(">>> "))
            t.sleep(.5)
            if opt in locations:
                locationId = opt
                location = locations[opt]
                break

        except ValueError:
            pass

        print("Error: Not an option.")
        t.sleep(1)

    return locationId, location

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

def storeData(itemData, locationId, agentId):
    "Stores scanned data into database"
    cur, conn = getCursorConnection()

    cur.executescript(createItemScanTable)

    for v in itemData.values():
        date = v["scan_date"]
        time = v["scan_time"]
        quantity = v["quantity"]
        itemId = v["item_id"]
        sAgentId = agentId
        sLocationId = locationId

        cur.execute(insertItemScan,
            (date, time, quantity, itemId, sAgentId, sLocationId))

        cur.execute(updatePendingDropOff,
                    (quantity, itemId))

    conn.commit()
    conn.close()
