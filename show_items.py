"Show items scanned"
import time as t
from functions import showScans, getFromList
from data import (
    getItemScansAsc,
    getItemScansDesc,
    getScansByDate,
    getScansByAgentId,
    getScansBylocationId,
    getScanDates,
    getAgents,
    getLocations,
    scannedItemsOptions,
    ascOrDescOptions
    )
from util import shutDown, optionError, getOption

def showItemsScanned():
    "Prints recorded items from the database"

    # Options
    while True:
        opt = getOption("Scanned items options: ", scannedItemsOptions)

        if opt == "1":
            while True:
                opt = getOption("Options: ", ascOrDescOptions)

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
            break

        elif opt == "6":
            shutDown()

        else:
            t.sleep(1)
            optionError(opt)
