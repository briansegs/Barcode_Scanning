"""App"""
import sqlite3
from scanner import Scanner
from functions import createTables, storeData

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory
# TODO: add print statments to inform the user

# Connects to database
conn = sqlite3.connect('testDb.sqlite')
cur = conn.cursor()

# Drops and then creates tables in database
cur.executescript(createTables)

# Scans barcodes and stores in data{}
scan = Scanner()
scan.startScanner()
data = scan.getData()

# Stores scanned data into database
storeData(data, cur)
conn.commit()
