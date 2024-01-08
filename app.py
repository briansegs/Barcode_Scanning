"""App"""
import time as t
from scan_items import scanItems
from drop_off_items import dropOffItems
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
# TODO: Rethink if this app can be more object oriented
# TODO: Make Agent class
# TODO: Make Login function
# TODO: Make it so that only dropoff can happen at the storage facility 

agent = login()

location = agent.location.name

isNotStorage = location != "Storage Facility"

isStorage = location == "Storage Facility"

while True:
    print("Options: ")
    t.sleep(.5)
    print('''
    1. Scan items for pickup
    2. Drop off items
    4. Show items scanned
    3. Show items pending drop off
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
        dropOffItems()
        break

    elif opt == "6":
        shutDown()

    elif opt == "1" and isStorage:
        print("Items can not be picked up from the storage facility. \n")
        t.sleep(1)

    elif opt == "2" and isNotStorage:
        print(f'Items can not be dropped of at the {agent.location.name} location. \n')
        t.sleep(1)

    else:
        optionError(opt)
