"""App"""
from datetime import datetime
from data import states

now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")

location = ''
while location not in states:
    location = input('Enter state: ')
    if location in states:
        location = states[location]
        break
    print('Not a state \nStates: ny, nj, pa, fl \nPlease pick one from the list')
print(location)
        