"Add data to database"
import sqlite3
import time as t
from data import agents, items, locations

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
        DROP TABLE IF EXISTS Agents;
        CREATE TABLE Agents (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'barcode' TEXT,
            'first_name' TEXT,
            'last_name' TEXT
            );
    '''
    cur.executescript(createAgentTable)

    addAgents = '''
        INSERT OR IGNORE INTO Agents (barcode, first_name, last_name) 
        VALUES (:barcode, :first_name, :last_name)
        '''

    cur.executemany(addAgents, agents)
    conn.commit()

def insertItems():
    "inserts items from data into database"
    createItemsTable = '''
        DROP TABLE IF EXISTS Items;
        CREATE TABLE Items (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'barcode' TEXT,
            'name' TEXT
        );
    '''

    cur.executescript(createItemsTable)

    addItems = '''
        INSERT OR IGNORE INTO Items (barcode, name) 
        VALUES (:barcode, :name)
        '''

    cur.executemany(addItems, items)
    conn.commit()

def insertLocations():
    "inserts locations from data into database"
    createLocationsTable = '''
        DROP TABLE IF EXISTS Locations;
        CREATE TABLE Locations (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'name' TEXT
        );
    '''
    addLocations = '''
        INSERT OR IGNORE INTO Locations (name) 
        VALUES (?)
    '''
    cur.executescript(createLocationsTable)
    cur.executemany(addLocations, [(a,) for a in locations])
    conn.commit()

while True:
    print("Options: ")
    print("1. Update agents")
    print("2. Update Items")
    print("3. Update Locations")
    print("4. Quit")
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
        print("*Quitting program...*")
        quit()

    print("Error: Enter either 1, 2, 3, or 4")
    t.sleep(1)
