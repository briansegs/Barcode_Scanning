"""App"""
import time as t
from scan_items import scanItems
from drop_off_items import dropOffItems
from show_items import showItemsScanned
from util import shutDown, optionError
from functions import login

# TODO: Item drop off / remove item from inventory after scan
# TODO: Display Inventory
# TODO: Display scans / history
# TODO: Options:
# TODO: Scan items for pickup
# TODO: Drop off items
# TODO: Show items pending drop off
# TODO: Show items scanned / by date
# TODO: Show items dropped off / by date
# TODO: Spit out options into seperate files
# TODO: Add spacing when items are being scanned and printed
# TODO: See if showScans functions can be reduced into one function
# TODO: See if getScan functions can be reduced into one function

agent = login()

locationName = agent.location.name

isNotStorage = locationName != "Storage Facility"

isStorage = locationName == "Storage Facility"

while True:
    print(" Main options: ")
    t.sleep(.5)
    print('''
    1. Scan items for pickup
    2. Drop off items
    3. Show items scanned
    4. Show items pending drop off
    5. Show items drop off log
    6. Quit
    ''')
    t.sleep(.5)
    opt = input(">>> ")
    print("")
    t.sleep(1)

    if opt == "1" and isNotStorage:
        scanItems(agent)
        break

    elif opt == "2" and isStorage:
        dropOffItems(agent)
        break

    elif opt == "3":
        showItemsScanned()

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
