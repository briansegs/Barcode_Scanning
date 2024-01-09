"Show items scanned"
import time as t
from functions import (
    showAllScans,
    showScansByLocation,
    getCursorConnection
    )
from data import getItemScanAsc, getItemScanDesc
from util import shutDown, optionError

# TODO: Login agent
# TODO: Show items scanned options:
# TODO: All dates earliest to latest
# TODO: All dates latest to earliest
# TODO: Pick from dates / asending and desending by time
# TODO: By agent / asending and desending by date
# TODO: By location / asending and desending by date
# TODO: Extract function for login
# TODO: Find a better way to display data

# Options
while True:
    print("Options: ")
    t.sleep(.5)
    print('''
    1. Show all dates
    2. Show by date
    3. Show by agent
    4. Show by location
    5. Quit
    ''')
    t.sleep(.5)
    opt = input(">>> ")
    t.sleep(1)
    print("")

    if opt == "1":
        while True:
            print("Options:")
            print("")
            t.sleep(.5)
            print("    1. Show asending")
            print("    2. Show desending")
            print("")
            t.sleep(.5)
            opt = input(">>> ")
            t.sleep(1)
            print("")

            if opt == "1":
                showAllScans(getItemScanAsc)
                break

            elif opt == "2":
                showAllScans(getItemScanDesc)
                break

            else:
                optionError(opt)

    elif opt == "3":
        getAgentList = '''
        SELECT
            id,
            first_name,
            last_name
        FROM 
            agent
        '''
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
                    name = agents[opt][0] + " " + agents[opt][1]
                    break

            except ValueError:
                pass

            optionError(opt)
            t.sleep(1)

        print(agentId, name)

    elif opt == "4":
        showScansByLocation()

    elif opt == "5":
        shutDown()

    else:
        t.sleep(1)
        optionError(opt)
