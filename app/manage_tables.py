"Manage tables"
import time as t
from management_helpers import (
    insertAgents,
    insertItems,
    insertLocations,
    insertPendingDropOff,
    insertDropOffLog,
    dropCreateItemScan
)
# TODO: Rework manage_data.py
# TODO: Make this the file that runs manage tables
# TODO: Put menue into this file
# TODO: Refactor

def manageData():
    "manage data"
    while True:
        print("Options: ")
        t.sleep(.5)
        print('''
        1. Update agents table
        2. Update items table
        3. Update locations table
        4. Update Pending_drop_off
        5. Drop / create Drop_off_log table 
        6. Drop / create Item_Scan table
        7. Quit
        ''')
        t.sleep(.5)
        opt = input(">>> ")
        t.sleep(.5)

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
            insertDropOffLog()
            print("Drop / Create drop_off_log table completed")
            break
        elif opt == "6":
            dropCreateItemScan()
            print("Drop / Create item_scan table completed")
            break
        elif opt == "7":
            print("*Quitting program...*")
            quit()

        print("Error: Enter either 1, 2, 3, 4, 5, 6, or 7")
        t.sleep(1)


if __name__ == "__main__":
    manageData()
