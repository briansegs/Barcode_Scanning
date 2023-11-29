"""App"""
import sqlite3
import time as t
from items_scanner import ItemScanner
from functions import createTables, storeData, getAgent, getLocation

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory
# TODO: rethink how to store data & make scanner more generic

# Connects to database
conn = sqlite3.connect('testDb.sqlite')
cur = conn.cursor()
print('*Connected to database*')
t.sleep(1)

# Drops and then creates tables in database
cur.executescript(createTables)
print('*Tables created*')
t.sleep(1)

# Scans barcodes and stores in data{}
scan = ItemScanner()
print('*Starting scanner*')
t.sleep(1)
location = getLocation()
agent = getAgent()
scan.scanItems()
data = scan.getData()

# Stores scanned data into database
storeData(data, cur, location, agent)
conn.commit()
t.sleep(1)
print('*Data stored*')
