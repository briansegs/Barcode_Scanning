"""App"""
import sqlite3
import json
import time as t
from items_scanner import ItemScanner
from functions import storeData, getAgent, getLocation

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory
# TODO: rethink how to store data & make scanner more generic

# Connects to database
conn = sqlite3.connect('testDb.sqlite')
cur = conn.cursor()
print('*Connected to database*')
t.sleep(1)

# Drops and then creates tables in database
with open("data.json", "r", encoding="utf-8") as f:
    jdata = json.load(f)
cur.executescript(jdata["createTables"])
print('*Tables created*')
t.sleep(1)

# Scans barcodes and stores in data{}
scan = ItemScanner()
print('*Starting scanner*')
t.sleep(1)
location = getLocation()
agent = getAgent()
scan.scanItems()
itemData = scan.getItemData()

# Stores scanned data into database
storeData(itemData, cur, location, agent)
conn.commit()
t.sleep(1)
print('*Data stored*')
