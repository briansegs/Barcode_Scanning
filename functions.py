"""data and functions for app"""
import time as t
import pandas as pd
from util import (
    getCursorConnection,
    getDate,
    getTime,
    shutDown,
    optionError,
    newLine
    )
from data import (
    insertItemScan,
    getLocations,
    updatePendingDropOff,
    getPendingDropOff,
    pendingDropOffColumns,
    insertDropOffLog,
    clearPendingDropOff
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
        newLine()
        print('The program can not proceed without an agent.')
        t.sleep(1)
        print('Start the program over once you have an agent ID.')
        shutDown()

    return agent, agentId

def login():
    "Returns agent"
    print("Login to continue. ")
    t.sleep(1)

    agentName, agentId = getAgent()

    locationName, locationId  = getFromList("Location", getLocations)

    location = Location(locationName, locationId)
    agent = Agent(agentName, agentId, location)

    print(f'Welcome {agent.name}. You are logged into the {agent.location.name} location. \n')
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
        data = []

        for i in lst:
            itemId = i[2]
            quantity = i[1]
            name = i[0]
            date = getDate()
            time = getTime()

            cur.execute(insertDropOffLog,
                (date, time, quantity, itemId, agentId))

            cur.execute(clearPendingDropOff, (itemId,))

            data.append((name, quantity, itemId))

        conn.commit()
        conn.close()

        df = getDataFrame(data, pendingDropOffColumns)

        print("Items dropped off: \n")
        print(df, "\n")

        t.sleep(.5)
        print("Items added to drop off log. \n")
        t.sleep(1)

    else:
        print("No Items to drop off. \n")
        t.sleep(1)

def getDataFrame(data, columns):
    "Returns data frame with centered column names"
    df = pd.DataFrame(data=data, columns=columns)
    df.index = [" "] * len(df)
    pd.set_option('display.colheader_justify', 'center')

    if len(df.columns) == 3:
        # Hides the "Item_ID" column when -
        # showing Items pending dropped off
        df = df.iloc[:, [0, 1]]

    return df

def showDataFrame(topic, query, param, value, columns):
    "Prints a history of scans"
    t.sleep(1)

    cur, conn = getCursorConnection()

    if param is None:
        res = cur.execute(query)
    else:
        res = cur.execute(query, (param,))

    data = res.fetchall()
    conn.close()

    if len(data) > 0:
        df = getDataFrame(data, columns)

        print(f'{topic}: {value} \n')
        print(df, "\n \n")

    else:
        print("No data found. \n")

def getFromList(topic, query):
    "Returns selection from List"
    data = getData(query)

    if len(data[0]) == 1:
        dic = {}
        count = 0
        for item in data:
            if item[0] not in dic.values():
                count += 1
                dic[count] = item[0]

    elif len(data[0]) == 2:
        dic = {}
        for item in data:
            dic[item[0]] = item[1]

    elif len(data[0]) == 3:
        dic = {}
        for item in data:
            dic[item[0]] = item[1] + " " + item[2]

    while True:
        print(f'Enter the number of {topic}: \n')
        t.sleep(1)
        for num, value in dic.items():
            print(f'    {num}. {value}')
        newLine()
        t.sleep(.5)

        opt = input(">>> ")
        newLine()
        try:
            opt = int(opt)
            t.sleep(.5)
            if opt in dic:
                param = opt
                value = dic[opt]
                break

        except ValueError:
            pass

        optionError(opt)
        t.sleep(1)

    return value, param

def getData(query):
    "Returns data from query"
    cur, conn = getCursorConnection()
    res = cur.execute(query)
    data = res.fetchall()
    conn.close()

    return data
