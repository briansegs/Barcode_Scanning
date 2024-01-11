"Show items scanned"
import time as t
from functions import (
    showScans,
    getFromList
    )
from data import (
    getItemScansAsc,
    getItemScansDesc,
    getScansByDate,
    getScansByAgentId,
    getScansBylocationId,
    getScanDates,
    getAgents,
    getLocations
    )
from util import shutDown, optionError

# TODO: Show items scanned options:
# TODO: All dates earliest to latest
# TODO: All dates latest to earliest
# TODO: Pick from dates / asending and desending by time
# TODO: By agent / asending and desending by date
# TODO: By location / asending and desending by date

# Options
while True:
    print("Options: ")
    t.sleep(.5)
    print('''
    1. Show all
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
            print("Options: \n")
            t.sleep(.5)
            print("    1. Show ascending")
            print("    2. Show descending \n")
            t.sleep(.5)
            opt = input(">>> ")
            t.sleep(1)
            print("")

            if opt == "1":
                showScans("All", getItemScansAsc, None, "Ascending")
                break

            elif opt == "2":
                showScans("All", getItemScansDesc, None, "Descending")
                break

            else:
                optionError(opt)

    elif opt == "2":
        date, _ = getFromList("Date", getScanDates)
        showScans("Date", getScansByDate, date, date)

    elif opt == "3":
        agentName, agentId = getFromList("Agent", getAgents)
        showScans("Agent",getScansByAgentId, agentId, agentName)

    elif opt == "4":
        locationName, locationId = getFromList("Location", getLocations)
        showScans("Location", getScansBylocationId, locationId, locationName)

    elif opt == "5":
        shutDown()

    else:
        t.sleep(1)
        optionError(opt)
