"Add data to database"
import sqlite3
import time as t
from functions import getData

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

data = getData()

def insertAgents():
    "inserts agents from data into database"
    createAgentTable = '''
        DROP TABLE IF EXISTS Agents;
        CREATE TABLE Agents (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'barcode' TEXT,
            'name' TEXT
            );
    '''
    cur.executescript(createAgentTable)

    addAgents = "INSERT OR IGNORE INTO Agents (barcode, name) VALUES (:barcode, :name)"

    cur.executemany(addAgents, data["agents"])
    conn.commit()

def insertInventory():
    "inserts items from data into database"
    createInventoryTable = '''
        DROP TABLE IF EXISTS Inventory;
        CREATE TABLE Inventory (
            'barcode' TEXT,
            'name' TEXT
        );
    '''

    cur.executescript(createInventoryTable)

    addInventory = "INSERT OR IGNORE INTO Inventory (barcode, name) VALUES (:barcode, :name)"

    cur.executemany(addInventory, data["inventory"])
    conn.commit()

while True:
    print("Options: ")
    t.sleep(1)
    print("1. Update agents")
    t.sleep(1)
    print("2. Update Inventory")
    t.sleep(1)
    print("3. Quit")
    t.sleep(.5)
    opt = input(">>> ")
    t.sleep(1)

    if opt == "1":
        insertAgents()
        print("Agents update completed")
        break
    elif opt == "2":
        insertInventory()
        print("Inventory update completed")
        break
    elif opt == "3":
        print("*Quitting program...*")
        quit()

    print("Error: Enter either 1, 2, or 3")
    t.sleep(1)
