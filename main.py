"""App"""
import time as t
from scan_items import scanItems
from drop_off_items import dropOffItems
from show_items import showItemsScanned
from show_pending_drop_off import showPendingDropOff
from show_drop_off_log import showDropOffLog
from util import shutDown, optionError, getOption
from functions import login
from data import mainMenueOptions

# TODO: Spit out options into seperate files
# TODO: Test features of app
# TODO: Split data into different files
# TODO: Split functions into different files
# TODO: Add classes to one folder

def main():
    "main function"
    agent = login()

    locationName = agent.location.name

    isNotStorage = locationName != "Storage Facility"

    isStorage = locationName == "Storage Facility"

    while True:
        opt = getOption("Main menue options: ", mainMenueOptions)

        if opt == "1" and isNotStorage:
            scanItems(agent)

        elif opt == "2" and isStorage:
            dropOffItems(agent)

        elif opt == "3":
            showItemsScanned()

        elif opt == "4":
            showPendingDropOff()

        elif opt == "5":
            showDropOffLog()

        elif opt == "6":
            shutDown()

        elif opt == "1" and isStorage:
            print("Items can not be picked up from the storage facility. \n")
            t.sleep(1)

        elif opt == "2" and isNotStorage:
            print(f'Items can not be dropped of at the {locationName} location. \n')
            t.sleep(1)

        else:
            optionError(opt)
            
if __name__ == '__main__':
    main()
