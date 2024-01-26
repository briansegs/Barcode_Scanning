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
from util import getCursorConnection

def createTable(query1, query2, param):
    "Creates tables"
    try:
        cur, conn = getCursorConnection()
        print(f'Connected to database: {db} \n')
        t.sleep(1)
    except sqlite3.Error as error:
        print(f'failed to connect to database: {db} \n')
        print(error)
        quit()

    cur.executescript(query1)

    if query2 is not None:
        cur.executemany(query2, param)

    conn.commit()
    conn.close()


def insertAgents():
    "inserts agents from data into database"
    createTable(
        createAgentTable,
        addAgents,
        agents
    )

def insertItems():
    "inserts items from data into database"
    createTable(
        createItemsTable,
        addItems,
        items
    )

def insertLocations():
    "inserts locations from data into database"
    createTable(
        createLocationsTable,
        addLocations,
        [(a,) for a in locations]
    )

def insertPendingDropOff():
    "inserts pending drop off from data into database"
    createTable(
        createPendingDropOffTable,
        addPendingDropOff,
        pendingDropOff
    )

def insertDropOffLog():
    "drops and adds drop_off_log table"
    createTable(
        createDropOffLogTable,
        None,
        None
    )

def dropCreateItemScan():
    "drops and adds item_scan table"
    createTable(
        createItemScanTable,
        None,
        None
    )
