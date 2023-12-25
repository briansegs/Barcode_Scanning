"""data and functions for app"""
import sqlite3
from datetime import datetime
import time as t
from data import insertScan, getLocations
from data import database as db

def getCursorConnection():
    "Returns cursor from database"
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    return cur, conn

def getLocation():
    "Returns location"
    cur, conn = getCursorConnection()
    res = cur.execute(getLocations)
    conn.close()
    lst = res.fetchall()

    locations = {}
    for item in lst:
        locations[item[0]] = item[1]

    while True:
        print("Enter the number of your Location: ")
        t.sleep(1)
        for num, location in locations.items():
            print(f'{num}. {location}')
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

def storeData(itemData, cur, locationId, agentId):
    "Stores scanned data into database"
    cur, conn = getCursorConnection()
    for v in itemData.values():
        date = v["scan_date"]
        time = v["scan_time"]
        quantity = v["quantity"]
        itemId = v["item_id"]
        sAgentId = agentId
        sLocationId = locationId

        cur.execute(insertScan,
            (date, time, quantity, itemId, sAgentId, sLocationId))

        updateInventory = '''
            UPDATE Inventory 
            SET quantity = quantity + ? 
            WHERE Item_id = ?
        '''
        cur.execute(updateInventory,
                    (quantity, itemId))

    conn.commit()
    conn.close()
