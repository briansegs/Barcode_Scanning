"""App"""
import sqlite3
import time as t
from items_scanner import ItemScanner
from agent_scanner import AgentScanner
from functions import storeData, getLocation, getData

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory
# TODO: add if else statments 

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
agent, agentCode = aScan.scanAgent()
print(f'Welcome {agent}. You are logged into the {location} location.')
t.sleep(1)
print('Starting scanner...')
t.sleep(1)
iScan.scanItems()
itemData = iScan.getScanData()

# Stores scanned data into database
storeData(data, itemData, cur, location, agent, agentCode)
conn.commit()
t.sleep(1)
print('*Data stored*')
