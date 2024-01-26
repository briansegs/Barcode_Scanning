"Add data to database"
import sqlite3
import time as t
from management_helpers import (
    agents,
    items,
    locations,
    pendingDropOff,
    createAgentTable,
    addAgents,
    createItemsTable,
    addItems,
    createLocationsTable,
    addLocations,
    createPendingDropOffTable,
    addPendingDropOff,
    createDropOffLogTable,
    createItemScanTable
)
from data import database as db

try:
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    print(f'Connected to database: {db}')
    t.sleep(1)
except sqlite3.Error as error:
    print(f'failed to connect to database: {db}')
    print(error)
    quit()

def insertAgents():
    "inserts agents from data into database" 
    cur.executescript(createAgentTable)
    cur.executemany(addAgents, agents)
    conn.commit()

def insertItems():
    "inserts items from data into database"
    cur.executescript(createItemsTable)
    cur.executemany(addItems, items)
    conn.commit()

def insertLocations():
    "inserts locations from data into database"
    cur.executescript(createLocationsTable)
    cur.executemany(addLocations, [(a,) for a in locations])
    conn.commit()

def insertPendingDropOff():
    "inserts pending drop off from data into database"
    cur.executescript(createPendingDropOffTable)
    cur.executemany(addPendingDropOff, pendingDropOff)
    conn.commit()

def insertDropOffLog():
    "drops and adds drop_off_log table"
    cur.executescript(createDropOffLogTable)
    conn.commit()

def dropCreateItemScan():
    "drops and adds item_scan table"
    cur.executescript(createItemScanTable)
    conn.commit()
