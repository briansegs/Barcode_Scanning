"Add data to database"
import sqlite3
import time as t
from data import agents, items, locations, pendingDropoff

db = 'testDb.sqlite'

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
    createAgentTable = '''
        DROP TABLE IF EXISTS agent;
        CREATE TABLE agent (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'barcode' TEXT,
            'first_name' TEXT,
            'last_name' TEXT
            );
    '''
    cur.executescript(createAgentTable)

    addAgents = '''
        INSERT OR IGNORE INTO agent (barcode, first_name, last_name) 
        VALUES (:barcode, :first_name, :last_name)
        '''

    cur.executemany(addAgents, agents)
    conn.commit()

def insertItems():
    "inserts items from data into database"
    createItemsTable = '''
        DROP TABLE IF EXISTS item;
        CREATE TABLE item (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'barcode' TEXT,
            'name' TEXT
        );
    '''

    cur.executescript(createItemsTable)

    addItems = '''
        INSERT OR IGNORE INTO item (barcode, name) 
        VALUES (:barcode, :name)
        '''

    cur.executemany(addItems, items)
    conn.commit()

def insertLocations():
    "inserts locations from data into database"
    createLocationsTable = '''
        DROP TABLE IF EXISTS location;
        CREATE TABLE location (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'name' TEXT
        );
    '''
    addLocations = '''
        INSERT OR IGNORE INTO location (name) 
        VALUES (?)
    '''
    cur.executescript(createLocationsTable)
    cur.executemany(addLocations, [(a,) for a in locations])
    conn.commit()

def insertPendingDropoff():
    "inserts pending dropoff from data into database"
    createPendingDropoffTable = '''
        DROP TABLE IF EXISTS pending_dropoff;
        CREATE TABLE pending_dropoff (
            'item_id' INTEGER,
            'quantity' INTEGER
        );
    '''
    addPendingDropoff = '''
        INSERT OR IGNORE INTO pending_dropoff (item_id, quantity) 
        VALUES (:item_id, :quantity)
    '''
    cur.executescript(createPendingDropoffTable)
    cur.executemany(addPendingDropoff, pendingDropoff)
    conn.commit()

def insertDropoffLog():
    "drops and adds dropoff log table"
    createDropoffLogTable = '''
        DROP TABLE IF EXISTS dropoff_log;
        CREATE TABLE dropoff_log (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'date' NUMERIC, 
            'time' NUMERIC,
            'quantity' INTEGER, 
            'item_id' INTEGER, 
            'agent_id' INTEGER
        );
    '''
    cur.executescript(createDropoffLogTable)
    conn.commit()

while True:
    print("Options: ")
    t.sleep(.5)
    print('''
    1. Update agents
    2. Update Items
    3. Update Locations
    4. Update Pending Dropoff
    5. Drop / Add Dropoff log
    6. Quit
    ''')
    t.sleep(.5)
    opt = input(">>> ")
    t.sleep(.5)

    if opt == "1":
        insertAgents()
        print("Agents update completed")
        break
    elif opt == "2":
        insertItems()
        print("Items update completed")
        break
    elif opt == "3":
        insertLocations()
        print("Locations update completed")
        break
    elif opt == "4":
        insertPendingDropoff()
        print("Pending Dropoff update completed")
        break
    elif opt == "5":
        insertDropoffLog()
        print("Drop / Add Dropoff log completed")
        break
    elif opt == "6":
        print("*Quitting program...*")
        quit()

    print("Error: Enter either 1, 2, 3, or 4")
    t.sleep(1)
