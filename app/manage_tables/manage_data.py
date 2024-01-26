"Add data to database"
import sqlite3
import time as t
from app.manage_tables import agents, items, locations, pendingDropOff

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

def insertPendingDropOff():
    "inserts pending drop off from data into database"
    createPendingDropOffTable = '''
        DROP TABLE IF EXISTS pending_drop_off;
        CREATE TABLE pending_drop_off (
            'item_id' INTEGER,
            'quantity' INTEGER
        );
    '''
    addPendingDropOff = '''
        INSERT OR IGNORE INTO pending_drop_off (item_id, quantity) 
        VALUES (:item_id, :quantity)
    '''
    cur.executescript(createPendingDropOffTable)
    cur.executemany(addPendingDropOff, pendingDropOff)
    conn.commit()

def insertDropOffLog():
    "drops and adds drop_off_log table"
    createDropOffLogTable = '''
        DROP TABLE IF EXISTS drop_off_log;
        CREATE TABLE drop_off_log (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'date' NUMERIC, 
            'time' NUMERIC,
            'quantity' INTEGER, 
            'item_id' INTEGER, 
            'agent_id' INTEGER
        );
    '''
    cur.executescript(createDropOffLogTable)
    conn.commit()

def dropCreateItemScan():
    "drops and adds item_scan table"
    createItemScanTable = '''
    DROP TABLE IF EXISTS item_scan;
    CREATE TABLE item_scan (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'date' NUMERIC, 
        'time' NUMERIC,
        'quantity' INTEGER, 
        'item_id' INTEGER, 
        'agent_id' INTEGER, 
        'location_id' INTEGER
        )
    '''
    cur.executescript(createItemScanTable)
    conn.commit()

while True:
    print("Options: ")
    t.sleep(.5)
    print('''
    1. Update agents table
    2. Update items table
    3. Update locations table
    4. Update Pending_drop_off
    5. Drop / create Drop_off_log table 
    6. Drop / create Item_Scan table
    7. Quit
    ''')
    t.sleep(.5)
    opt = input(">>> ")
    t.sleep(.5)

    if opt == "1":
        insertAgents()
        print("agents update completed")
        break
    elif opt == "2":
        insertItems()
        print("items update completed")
        break
    elif opt == "3":
        insertLocations()
        print("locations update completed")
        break
    elif opt == "4":
        insertPendingDropOff()
        print("pending_drop_off update completed")
        break
    elif opt == "5":
        insertDropOffLog()
        print("Drop / Create drop_off_log table completed")
        break
    elif opt == "6":
        dropCreateItemScan()
        print("Drop / Create item_scan table completed")
        break
    elif opt == "7":
        print("*Quitting program...*")
        quit()

    print("Error: Enter either 1, 2, 3, 4, 5, 6, or 7")
    t.sleep(1)
