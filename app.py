"""App"""
import sqlite3
from scanner import Scanner
from functions import createTables, storeData, getAgent, getLocation

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory
# TODO: rethink how to store data & make scanner more generic

# Connects to database
conn = sqlite3.connect('testDb.sqlite')
cur = conn.cursor()
print('Connected to database')

# Drops and then creates tables in database
cur.executescript(createTables)
print('Tables created')

# Scans barcodes and stores in data{}
scan = Scanner()
print('Starting scanner')
location = getLocation()
agent = getAgent()
scan.startScanner()
data = scan.getData()

# Stores scanned data into database
storeData(data, cur, location, agent)
conn.commit()
print('Data stored')
