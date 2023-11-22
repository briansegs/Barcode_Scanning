"""data and functions for app"""
from datetime import datetime

states = {
    'ny' : 'New York',
    'nj' : 'New Jersey',
    'pa' : 'Pennsylvinia',
    'fl' : 'Florida'
}

# TODO: add agent{} that has {barcode : name}
# TODO: add getAgent()

def getLocation():
    """Retuns location from input statment"""
    location = ''
    while location not in states:
        location = input('Enter state: ')
        if location in states:
            location = states[location]
            break
        print('Not a state \nStates: ny, nj, pa, fl \nPlease pick one from the list')
    return location

def getDate():
    'returns current date'
    now = datetime.now()
    date = now.strftime("%m/%d/%Y")
    return date

def getTime():
    'return current Time'
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return time
