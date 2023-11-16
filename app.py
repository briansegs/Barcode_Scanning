"""App"""
from datetime import datetime

now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")

states = {
    'ny' : 'New York',
    'nj' : 'New Jersey',
    'pa' : 'Pennsylvinia',
    'fl' : 'Florida'
}

location = ''
while location not in states:
    location = input('Enter state: ')
    if location in states:
        location = states[location]
        break
    print('Not a state \nStates: ny, nj, pa, fl \nPlease pick one from the list')
print(location)
        