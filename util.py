"App Utilities"
import sqlite3
from datetime import datetime
from data import database as db

def getCursorConnection():
    "Returns cursor from database"
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    return cur, conn

def getDate():
    "returns current date"
    now = datetime.now()
    date = now.strftime("%m/%d/%Y")
    return date

def getTime():
    "return current Time"
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return time