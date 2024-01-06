"Show items scanned"
import time as t
from functions import getAgent, showAllscans
from data import getItemScanAsc, getItemScanDesc
from util import shutDown, optionError

# TODO: Login agent
# TODO: Show items scanned options:
# TODO: All dates earliest to latest
# TODO: All dates latest to earliest
# TODO: Pick from dates / asending and desending by time
# TODO: By agent / asending and desending by date
# TODO: By location / asending and desending by date
# TODO: Extract function for login
# TODO: Find a better way to display data

# Login
print("Login to continue. ")
t.sleep(1)

agent, agentId = getAgent()

print(f"Welcome {agent}.")
t.sleep(.5)

# Options
while True:
    print("Options: ")
    t.sleep(.5)
    print('''
    1. Show all dates
    3. Show by date
    4. Show by agent
    5. Show by location
    6. Quit
    ''')
    t.sleep(.5)
    opt = input(">>> ")
    t.sleep(1)
    print("")

    if opt == "1":
        while True:
            print("Options:")
            t.sleep(.5)
            print("    1. Show asending")
            print("    2. Show desending")
            t.sleep(.5)
            opt = input(">>> ")
            t.sleep(1)
            print("")

            if opt == "1":
                showAllscans(getItemScanAsc)
                shutDown()

            elif opt == "2":
                showAllscans(getItemScanDesc)
                shutDown()
            else:
                optionError(opt)

    elif opt == "6":
        shutDown()

    else:
        t.sleep(1)
        optionError(opt)
