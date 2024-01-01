"""App"""
import time as t
from items_scanner import ItemScanner
from agent_scanner import AgentScanner
from functions import storeData, getLocation

# TODO: Item dropoff / remove item from inventory after scan
# TODO: Display Inventory
# TODO: Display scans / history

# Create scanners
iScan = ItemScanner()
aScan = AgentScanner()

# Login process
print('Login to start scanning.')
t.sleep(1)
locationId, location = getLocation()

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
