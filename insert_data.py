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

createAgentTable = '''
    DROP TABLE IF EXISTS Agents;
    CREATE TABLE Agents (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'barcode' TEXT,
        'name' TEXT
        );
'''
cur.executescript(createAgentTable)

insertAgents = "INSERT OR IGNORE INTO Agents (barcode, name) VALUES (:barcode, :name)"

cur.executemany(insertAgents, data["agents"])
conn.commit()

# code = (data["agents"][0]["barcode"],)

# res = cur.execute("SELECT name, barcode FROM Agents WHERE barcode = ?", code)
# print(res.fetchone())
