"App Utilities"
import sqlite3
import time as t
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

def shutDown():
    "Exits the application"
    t.sleep(1)
    newLine()
    print("*Application shutting down...*")
    quit()

def optionError(opt):
    "Option error message"
    print(f'Error: "{opt}" is not an option.')
    t.sleep(1)

def getOption(title, options):
    '''
    prints list of options
    Returns selected option
    '''
    print(title, "\n")
    t.sleep(.5)

    for num, option in options.items():
        print(f'    {num}. {option}')
    newLine()

    t.sleep(.5)
    opt = input(">>> ")
    newLine()
    t.sleep(1)

    return opt

def newLine():
    "Prints a new line"
    print("")
