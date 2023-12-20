"Add data to database"
import sqlite3
from functions import getData

db = 'testDb.sqlite'

try:
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    print(f'Connected to database: {db}')
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
    print("1. Update agents")
    print("2. Update Inventory")
    print("3. Quit")
    opt = input(">>> ")

    if opt == "1":
        insertAgents()
        print("Agents update completed")
        break
    elif opt == "2":
        insertInventory()
        print("Inventory update completed")
        break
    elif opt == "q":
        print("*Quitting program...*")
        quit()

    print("Error: Enter either 1, 2, or q")
