"""App"""
import sqlite3
from scanner import Scanner
from functions import createTables, storeData

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory
# TODO: add print statments to inform the user
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
# TODO: add get location and agent here
scan.startScanner()
data = scan.getData()

# Stores scanned data into database
# TODO: pass location and agent into storeData
storeData(data, cur)
conn.commit()
print('Data stored')
