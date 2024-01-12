"Show items scanned"
import time as t
from functions import showDataFrame, getFromList
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
    ascOrDescOptions,
    itemColumns
    )
from util import shutDown, optionError, getOption

def showItemsScanned():
    "Prints recorded items from the database"
    while True:
        opt = getOption("Scanned items options: ", scannedItemsOptions)

        if opt == "1":
            while True:
                opt = getOption("Options: ", ascOrDescOptions)

                if opt == "1":
                    showDataFrame(
                        "All",
                        getItemScansAsc,
                        None,
                        "Ascending",
                        itemColumns
                    )
                    break

                elif opt == "2":
                    showDataFrame(
                        "All",
                        getItemScansDesc,
                        None,
                        "Descending",
                        itemColumns
                    )
                    break

                else:
                    optionError(opt)

        elif opt == "2":
            date, _ = getFromList("Date", getScanDates)
            showDataFrame("Date", getScansByDate, date, date, itemColumns)

        elif opt == "3":
            agentName, agentId = getFromList("Agent", getAgents)
            showDataFrame(
                "Agent",
                getScansByAgentId,
                agentId,
                agentName,
                itemColumns
            )

        elif opt == "4":
            locationName, locationId = getFromList(
                "Location", 
                getLocations
            )
            showDataFrame(
                "Location", 
                getScansBylocationId,
                locationId,
                locationName,
                itemColumns
            )

        elif opt == "5":
            break

        elif opt == "6":
            shutDown()

        else:
            t.sleep(1)
            optionError(opt)
