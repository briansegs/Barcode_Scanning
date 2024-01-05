"""data and functions for app"""
import time as t
from util import getCursorConnection, getDate, getTime
from data import (
    insertItemScan,
    getLocations,
    updatePendingDropOff,
    createItemScanTable
    )
from agent_scanner import AgentScanner

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

def updateDropOffLog(agentId):
    '''
    Updates the drop_off_log table in the database
    Clears the pending_drop_off table in the database
    '''

    cur, conn = getCursorConnection()
    getPendingDropOff = '''
    SELECT item_id, quantity FROM pending_drop_off WHERE quantity > 0
    '''
    res = cur.execute(getPendingDropOff)
    lst = res.fetchall()

    insertDropOffLog = '''
    INSERT OR IGNORE INTO drop_off_log (
        date,
        time,
        quantity,
        item_id,
        agent_id
    )
    VALUES (?, ?, ?, ?, ?)
    '''

    clearPendingDropOff = '''
    UPDATE pending_drop_off
    SET quantity = 0
    WHERE item_id = ?
    '''
    getItemName = '''
    SELECT name FROM item WHERE id = ?
    '''

    t.sleep(1)
    print("Items dropped off: ")
    print("")

    for i in lst:
        itemId = i[0]
        quantity = i[1]
        date = getDate()
        time = getTime()

        cur.execute(insertDropOffLog,
            (date, time, quantity, itemId, agentId))

        cur.execute(clearPendingDropOff, (itemId,))

        res = cur.execute(getItemName,(itemId,))
        tup = res.fetchone()
        name = tup[0]

        print(f'    {quantity}  {name}')

    conn.commit()
    conn.close()

    print("")
    t.sleep(1)
    print("Items added to drop off log.")
    t.sleep(1)
    print("*Application shutting down...*")
    quit()
