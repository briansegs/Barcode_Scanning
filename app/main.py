"Main"
import time as t
from util import shutDown, optionError, getOption
from functions import login
from data import mainMenueOptions
from options import (
    showPendingDropOff,
    showDropOffLog,
    showItemsScanned,
    dropOffItems,
    scanItems
)

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
