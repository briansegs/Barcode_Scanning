"Show items scanned"
import time as t
import pandas as pd
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
print("Login to continue. ")
t.sleep(1)

agent, agentId = getAgent()

print(f"Welcome {agent}.")
t.sleep(.5)

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
    t.sleep(1)
    print("")

    if opt == "1":
        getItemScanAsc = '''
        SELECT 
        item_scan.id,
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
        scans = res.fetchall()
        columns = ["ID", "Date", "Time", "Quantity",
                   "Item", "Agent", "Name", "location"]
        df = pd.DataFrame(data=scans, columns=columns)
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        t.sleep(1)
        print("*Application shutting down...*")
        quit()

    elif opt == "6":
        t.sleep(1)
        print("*Application shutting down...*")
        quit()

    else:
        t.sleep(1)
        print(f'Error: "{opt}" is not an option.')
