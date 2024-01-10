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
    getItemScanlocation,
    getAgentList,
    getItemScanAgent,
    getScanDates,
    getItemScanDate
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
        print("Enter the number of your Location: \n")
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

        optionError(opt)
        t.sleep(1)

    return locationId, location

def login():
    "Returns agent"
    print("Login to continue. ")
    t.sleep(1)

    locationId, locationName = getLocation()
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

def showAllScans(sql):
    "Prints a history of scans"
    cur, conn = getCursorConnection()
    res = cur.execute(sql)
    data = res.fetchall()
    conn.close()

    if len(data) > 0:
        df = getScanDataFrame(data)

        print(df, "\n")

    else:
        print("No data found.")

def showScansByLocation():
    "Prints a history of scans by location"
    locationId, location = getLocation()
    t.sleep(1)
    print("")
    t.sleep(.5)

    cur, conn = getCursorConnection()
    res = cur.execute(getItemScanlocation, (locationId,))
    data = res.fetchall()
    conn.close()

    if len(data) > 0:
        df = getScanDataFrame(data)

        print(f'Location: {location} \n')
        print(df, "\n")

    else:
        print("No data found.")

def getAgentFromList():
    "Returns agent id and name"
    cur, conn = getCursorConnection()
    res = cur.execute(getAgentList)
    lst = res.fetchall()
    conn.close()

    agents = {}
    for agent in lst:
        agents[agent[0]] = [agent[1], agent[2]]

    while True:
        print("Enter the number of agent: \n")
        t.sleep(1)
        for num, name in agents.items():
            print(f'    {num}. {name[0]} {name[1]}')
        print("")
        t.sleep(.5)

        try:
            opt = int(input(">>> "))
            t.sleep(.5)
            if opt in agents:
                agentId = opt
                agentName = agents[opt][0] + " " + agents[opt][1]
                break

        except ValueError:
            pass

        optionError(opt)
        t.sleep(1)

    return agentId, agentName

def showScansByAgent():
    "Prints a history of scans by Agent"
    agentId, agentName = getAgentFromList()
    t.sleep(1)
    print("")
    t.sleep(.5)

    cur, conn = getCursorConnection()
    res = cur.execute(getItemScanAgent, (agentId,))
    data = res.fetchall()
    conn.close()

    if len(data) > 0:
        df = getScanDataFrame(data)

        print(f'Agent: {agentName} \n')
        print(df, "\n")

    else:
        print("No data found")

def getScanDate():
    "returns selected date"
    cur, conn = getCursorConnection()
    res = cur.execute(getScanDates)
    lst = res.fetchall()
    conn.close()

    dates = {}
    count = 0
    for item in lst:
        if item[0] not in dates.values():
            count += 1
            dates[count] = item[0]

    while True:
        print("Enter the number of date: \n")
        t.sleep(1)
        for num, date in dates.items():
            print(f'    {num}. {date}')
        print("")
        t.sleep(.5)

        try:
            opt = int(input(">>> "))
            t.sleep(.5)
            if opt in dates:
                date = dates[opt]
                break

        except ValueError:
            pass

        optionError(opt)
        t.sleep(1)

    return date

def showScansByDate():
    "Prints a history of scans by Agent"
    date = getScanDate()
    t.sleep(1)
    print("")
    t.sleep(.5)

    cur, conn = getCursorConnection()
    res = cur.execute(getItemScanDate, (date,))
    data = res.fetchall()
    conn.close()

    if len(data) > 0:
        df = getScanDataFrame(data)

        print(f'Date: {date} \n')
        print(df, "\n")

    else:
        print("No data found.")

# TODO: See if showScans functions can be reduced into one function
# Example of generic function

# date = getScanDate()

# def showScans(subject, query, para):
#     "Prints a history of scans"
#     t.sleep(1)
#     print("")
#     t.sleep(.5)

#     cur, conn = getCursorConnection()
#     res = cur.execute(query, (para,))
#     data = res.fetchall()
#     conn.close()

#     if len(data) > 0:
#         df = getScanDataFrame(data)

#         print(f'{subject}: {date} \n')
#         print(df, "\n")

#     else:
#         print("No data found.")

# showScans("Date", getItemScanDate, date)
