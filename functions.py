"""data and functions for app"""
from datetime import datetime

states = {
    'ny' : 'New York',
    'nj' : 'New Jersey',
    'pa' : 'Pennsylvinia',
    'fl' : 'Florida'
}

# TODO: change to {barcode : name} when I can generate barcodes
agents = {
    '1' : 'Brian',
    '2' : 'Tom',
    '3' : 'Ron',
    '4' : 'Barb'
}

# TODO: split up tables. plan and structure table relationships
createTables = '''
    DROP TABLE IF EXISTS Items;
    
    CREATE TABLE Items (
        "barcode" INTEGER,
        "bar_type" TEXT,
        "scan_agent" TEXT,
        "scan_location" TEXT,
        "scan_date" NUMERIC,
        "scan_time" NUMERIC
    )'''

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
