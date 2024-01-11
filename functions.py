"""data and functions for app"""
import time as t
import pandas as pd
from util import (
    getCursorConnection,
    getDate,
    getTime,
    shutDown,
    optionError
    )
from data import (
    insertItemScan,
    getLocations,
    updatePendingDropOff,
    getPendingDropOff,
    insertDropOffLog,
    clearPendingDropOff,
    getItemName,
    )
from agent_scanner import AgentScanner
from agent import Agent
from location import Location

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
        shutDown()

    return agent, agentId

def login():
    "Returns agent"
    print("Login to continue. ")
    t.sleep(1)

    locationId, locationName = getFromList("Location", getLocations)
    location = Location(locationName, locationId)

    agentName, agentId = getAgent()
    agent = Agent(agentName, agentId, location)

    print(f'Welcome {agent.name}. You are logged into the {agent.location.name} location.')
    t.sleep(1)

    return agent

def storeData(itemData, locationId, agentId):
    "Stores scanned data into database"
    cur, conn = getCursorConnection()

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
    res = cur.execute(getPendingDropOff)
    lst = res.fetchall()

    if len(lst) > 0:
        t.sleep(1)
        print("Items dropped off: \n")

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

    else:
        print("No Items to drop off.")

def getScanDataFrame(data):
    "Returns scan data frame"
    columns = ["ID", "Date", "Time", "Quantity",
                "Item", "Agent", "Name", "location"]

    df = pd.DataFrame(data=data, columns=columns)

    pd.set_option('display.colheader_justify', 'center')

    return df

def showScans(subject, query, para, value):
    "Prints a history of scans"
    t.sleep(1)
    print("")
    t.sleep(.5)

    cur, conn = getCursorConnection()

    if para is None:
        res = cur.execute(query)
    else:
        res = cur.execute(query, (para,))

    data = res.fetchall()
    conn.close()

    if len(data) > 0:
        df = getScanDataFrame(data)

        print(f'{subject}: {value} \n')
        print(df, "\n")

    else:
        print("No data found. \n")

def getFromList(subject, query):
    "Returns selection from List"
    cur, conn = getCursorConnection()
    res = cur.execute(query)
    lst = res.fetchall()
    conn.close()

    if len(lst[0]) == 1:
        obj = {}
        count = 0
        for item in lst:
            if item[0] not in obj.values():
                count += 1
                obj[count] = item[0]

    elif len(lst[0]) == 2:
        obj = {}
        for item in lst:
            obj[item[0]] = item[1]

    elif len(lst[0]) == 3:
        obj = {}
        for item in lst:
            obj[item[0]] = item[1] + " " + item[2]

    while True:
        print(f'Enter the number of {subject}: \n')
        t.sleep(1)
        for num, value in obj.items():
            print(f'    {num}. {value}')
        print("")
        t.sleep(.5)

        try:
            opt = int(input(">>> "))
            t.sleep(.5)
            if opt in obj:
                param = obj[opt]
                break

        except ValueError:
            pass

        optionError(opt)
        t.sleep(1)

    return param, opt
