"""data for app"""
states = {
    'ny' : 'New York',
    'nj' : 'New Jersey',
    'pa' : 'Pennsylvinia',
    'fl' : 'Florida'
}

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
