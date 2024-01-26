"Manage tables"
from management_helpers import (
    insertAgents,
    insertItems,
    insertLocations,
    insertPendingDropOff,
    dropCreateDropOffLog,
    dropCreateItemScan
)
from util import getOption, optionError, shutDown

options = {
    "1" : "Update agents table",
    "2" : "Update items table",
    "3" : "Update locations table",
    "4" : "Update Pending_drop_off",
    "5" : "Drop / create Drop_off_log table",
    "6" : "Drop / create Item_Scan table",
    "7" : "Quit"
}

def manageData():
    "manage data"
    while True:
        opt = getOption("\nOptions: ", options)

        if opt == "1":
            insertAgents()
            print("agents update completed")
            break
        elif opt == "2":
            insertItems()
            print("items update completed")
            break
        elif opt == "3":
            insertLocations()
            print("locations update completed")
            break
        elif opt == "4":
            insertPendingDropOff()
            print("pending_drop_off update completed")
            break
        elif opt == "5":
            dropCreateDropOffLog()
            print("Drop / Create drop_off_log table completed")
            break
        elif opt == "6":
            dropCreateItemScan()
            print("Drop / Create item_scan table completed")
            break
        elif opt == "7":
            shutDown()

        optionError(opt)

if __name__ == "__main__":
    manageData()
