"""App"""
import sqlite3
import time as t
from items_scanner import ItemScanner
from agent_scanner import AgentScanner
from functions import storeData, getLocation, getData

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory
# TODO: rethink how to store data & make scanner more generic

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
scan = ItemScanner()
print('*Starting scanner*')
t.sleep(1)
location = getLocation()
aScan = AgentScanner()
agent, agentCode = aScan.scanAgent()
print(f'Welcome {agent}')
scan.scanItems()
itemData = scan.getScanData()

# Stores scanned data into database
storeData(data, itemData, cur, location, agent)
conn.commit()
t.sleep(1)
print('*Data stored*')
