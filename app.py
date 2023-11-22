"""App"""
import sqlite3
from data import getLocation
from scanner import Scanner

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory
# TODO: add scanned data to database

# TODO: put getLocation() into scanner class
# scan = Scanner(getLocation())

# scan.startScanner()

# for value in scan.getData().values():
#     print("----    ----")
#     for k, v in value.items():
#         print(f'{k}: {v}')

conn = sqlite3.connect('testDb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Items;
    
    CREATE TABLE Items (
        "barcode" INTEGER,
        "bar type" TEXT,
        "pickup location" TEXT,
        "pickup date" NUMERIC,
        "pickup time" NUMERIC
    );
''')
