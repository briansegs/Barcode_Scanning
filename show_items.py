"Show items scanned"
import time as t
from functions import getAgent
from util import getCursorConnection

# TODO: Login agent
# TODO: Show items scanned options:
# TODO: All dates earliest to latest
# TODO: All dates latest to earliest
# TODO: Pick from dates / asending and desending by time
# TODO: By agent / asending and desending by date
# TODO: By location / asending and desending by date
# TODO: Extract function for login
# TODO: Find a better way to display data

# Login
# print("Login to continue. ")
# t.sleep(1)

# agent, agentId = getAgent()

# print(f"Welcome {agent}.")
# t.sleep(.5)

# Options
while True:
    print("Options")
    t.sleep(.5)
    print('''
    1. Show all dates earliest to latest
    2. Show all dates latest to earliest
    3. Show by date
    4. Show by agent
    5. Show by location
    6. Quit
    ''')
    t.sleep(.5)
    opt = input(">>> ")

    if opt == "1":
        getItemScanAsc = '''
        SELECT 
        date,
        time,
        quantity,
        item.name,
        agent.first_name,
        agent.last_name,
        location.name
        FROM item_scan
        JOIN item JOIN agent JOIN location
        ON 
        item_scan.item_id = item.id 
        AND
        item_scan.agent_id = agent.id 
        AND
        item_scan.location_id = location.id
        ORDER BY 
        date, time ASC
        '''
        cur, conn = getCursorConnection()
        res = cur.execute(getItemScanAsc)
        lst = res.fetchall()
        print("Date, Time, Quantity, Item, Agent, location")
        for i in lst:
            date = i[0]
            time = i[1]
            quantity = i[2]
            itemName = i[3]
            agent = i[4] + " " + i[5]
            location = i[6]
            print(date, time, quantity, itemName, agent, location)
        break

    elif opt == "6":
        t.sleep(1)
        print("*Application shutting down...*")
        quit()

    else:
        t.sleep(1)
        print(f'Error: "{opt}" is not an option.')
