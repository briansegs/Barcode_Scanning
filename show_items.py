"Show items scanned"
import time as t
from functions import (
    showAllScans,
    getScanDate,
    showScans,
    getAgentFromList,
    getLocation
    )
from data import (
    getItemScanAsc,
    getItemScanDesc,
    getItemScanDate,
    getItemScanAgent,
    getItemScanlocation
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
            print("    1. Show asending")
            print("    2. Show desending \n")
            t.sleep(.5)
            opt = input(">>> ")
            t.sleep(1)
            print("")

            if opt == "1":
                # showAllScans(getItemScanAsc)
                showScans("All", getItemScanAsc, None, "Asending")
                break

            elif opt == "2":
                showAllScans(getItemScanDesc)
                break

            else:
                optionError(opt)

    elif opt == "2":
        date = getScanDate()
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
