"Add data to database"
import sqlite3

db = 'testDb.sqlite'

try:
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    print(f'Connected to database: {db}')
except sqlite3.Error as error:
    print(f'failed to connect to database: {db}')
    print(error)
    quit()
