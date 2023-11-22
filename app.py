"""App"""
import sqlite3
from scanner import Scanner
from functions import createTables

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory

conn = sqlite3.connect('testDb.sqlite')
cur = conn.cursor()

cur.executescript(createTables)

scan = Scanner()

scan.startScanner()

data = scan.getData()

# TODO: turn into a function that can be imported
for v in data.values():
    barcode = v["barcode"]
    barType = v["bar_type"]
    scanAgent = v["scan_agent"]
    scanLocation = v["scan_location"]
    scanDate = v["scan_date"]
    scanTime = v["scan_time"]

    cur.execute('''INSERT OR IGNORE INTO Items
        (barcode, bar_type, scan_agent,
        scan_location, scan_date, scan_time) VALUES
        (?, ?, ?, ?, ?, ?)''',
        (barcode, barType, scanAgent, scanLocation, scanDate, scanTime))

conn.commit()
