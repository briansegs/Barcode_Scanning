"""data and functions for app"""
from datetime import datetime

def getLocation():
    "Retuns location from input statment"
    location = ''
    while location not in states:
        location = input('Enter state: ')

        # To speed up testing (remove for production version)
        if location == '':
            location = 'ny'

        if location in states:
            location = states[location]
            break
        print('Not a state \nStates: ny, nj, pa, fl \nPlease pick one from the list')
    return location

def getAgent():
    "Retuns agent from input statment"
    # TODO: Scan a barcode to find agent name
    agent = ''
    while agent not in agents:
        agent = input('Enter your agent code: ')

        # To speed up testing (remove for production version)
        if agent == '':
            agent = '1'

        if agent in agents:
            agent = agents[agent]
            break
        print('Agent not found')
    return agent

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

def storeData(data, cur, location, agent):
    "Stores scanned data into database"
    for v in data.values():
        scanAgent = agent
        scanLocation = location
        barcode = v["barcode"]
        barType = v["bar_type"]
        scanDate = v["scan_date"]
        scanTime = v["scan_time"]

        cur.execute('''INSERT OR IGNORE INTO Items
            (barcode, bar_type, scan_agent,
            scan_location, scan_date, scan_time) VALUES
            (?, ?, ?, ?, ?, ?)''',
            (barcode, barType, scanAgent, scanLocation, scanDate, scanTime))
