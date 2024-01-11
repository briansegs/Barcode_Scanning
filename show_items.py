"Show items scanned"
import time as t
from functions import (
    showScans,
    getAgentFromList,
    getLocation,
    getParamFromList
    )
from data import (
    getItemScanAsc,
    getItemScanDesc,
    getItemScanDate,
    getItemScanAgent,
    getItemScanlocation,
    getScanDates
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
                showScans("All", getItemScanAsc, None, "Ascending")
                break

            elif opt == "2":
                showScans("All", getItemScanDesc, None, "Descending")
                break

            else:
                optionError(opt)

    elif opt == "2":
        date = getParamFromList(getScanDates, "Date")
        showScans("Date", getItemScanDate, date, date)

    elif opt == "3":
        agentId, agentName = getAgentFromList()
        showScans("Agent",getItemScanAgent, agentId, agentName)

    elif opt == "4":
        locationId, locationName = getLocation()
        showScans("Location", getItemScanlocation, locationId, locationName)

    elif opt == "5":
        shutDown()

    else:
        t.sleep(1)
        optionError(opt)
