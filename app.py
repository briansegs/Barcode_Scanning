"""App"""
import time as t
from items_scanner import ItemScanner
from agent_scanner import AgentScanner
from functions import storeData, getLocation

# TODO: Item dropoff / remove item from inventory after scan
# TODO: Display Inventory
# TODO: Display scans / history
# TODO: Make options / show before login
# TODO: Options: 
# TODO: Scan items for pickup
# TODO: Drop off items 
# TODO: Show items pending dropoff
# TODO: Show items scanned / by date
# TODO: Show items dropped off / by date
# TODO: Spit out options into seperate files

# Create scanners
iScan = ItemScanner()
aScan = AgentScanner()

# Login process
print('Login to start scanning.')
t.sleep(1)

print('Scan your user ID.')
t.sleep(1)
try:
    agent, agentId = aScan.scanAgent()

except TypeError:
    print('The program can not proceed without an agent.')
    t.sleep(1)
    print('Start the program over once you have an agent ID.')
    t.sleep(1)
    print('*Application shutting down...*')
    t.sleep(1)
    quit()

# Scans barcodes and stores in data{}
locationId, location = getLocation()

print(f'Welcome {agent}. You are logged into the {location} location.')
t.sleep(1)
print('*Starting scanner...*')
t.sleep(1)

iScan.scanItems()
itemData = iScan.getScanData()

if len(itemData) == 0:
    print('No Items were scanned.')
    t.sleep(1)
    print('*Application shutting down...*')
    quit()

# Stores scanned data into database
storeData(itemData, locationId, agentId)
t.sleep(1)
print('*Data stored*')
