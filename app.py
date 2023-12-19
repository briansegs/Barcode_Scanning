"""App"""
import sqlite3
import time as t
from items_scanner import ItemScanner
from agent_scanner import AgentScanner
from functions import storeData, getLocation, getData

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory

# Connects to database
conn = sqlite3.connect('testDb.sqlite')
cur = conn.cursor()
print('*Connected to database*')
t.sleep(1)

# Drops and then creates tables in database
data = getData()
cur.executescript(data["createTables"])
print('*Tables created*')
t.sleep(1)

# Scans barcodes and stores in data{}
iScan = ItemScanner()
aScan = AgentScanner()

print('Login to start scanning.')
t.sleep(1)
location = getLocation()
print('Scan your user ID.')
t.sleep(1)

try:
    agent, agentCode = aScan.scanAgent()

except TypeError:
    print('The program can not proceed without an agent.')
    t.sleep(1)
    print('Start the program over once you have an agent ID.')
    t.sleep(1)
    print('*Application shutting down...*')
    t.sleep(1)
    quit()

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
storeData(data, itemData, cur, location, agent, agentCode)
conn.commit()
t.sleep(1)
print('*Data stored*')
