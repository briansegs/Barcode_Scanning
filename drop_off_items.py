"Drop off items"
import time as t
from functions import getAgent
from util import getCursorConnection, getDate, getTime

# TODO: Ask if items were dropped off successfully
# TODO: Add options
# TODO: Yes - for each item in pending list - remove from list - add to log
# TODO: No - "please contact HQ for futher steps" - quit
# TODO: quit

# Login
print('Login to start scanning.')
t.sleep(1)

agent, agentId = getAgent()

print(f"Welcome {agent}. Were all items dropped off successfully?")
t.sleep(.5)

while True:
    print("Options: ")
    t.sleep(.5)
    print('''
    1. Yes
    2. No
    3. Quit
    ''')
    t.sleep(.5)
    opt = input(">>> ")

    if opt == "1":
        cur, conn = getCursorConnection()
        getPendingDropOff = '''
        SELECT item_id, quantity FROM pending_drop_off WHERE quantity > 0
        '''
        res = cur.execute(getPendingDropOff)
        lst = res.fetchall()

        insertDropOffLog = '''
        INSERT OR IGNORE INTO drop_off_log (
            date,
            time,
            quantity,
            item_id,
            agent_id
        )
        VALUES (?, ?, ?, ?, ?)
        '''

        clearPendingDropOff = '''
        UPDATE pending_drop_off
        SET quantity = 0
        WHERE item_id = ?
        '''

        for i in lst:
            date = getDate()
            time = getTime()
            cur.execute(insertDropOffLog,
                (date, time, i[1], i[0], agentId))
            cur.execute(clearPendingDropOff, (i[0],))

        conn.commit()
        conn.close()
        t.sleep(1)
        print("Items dropped off successfully.")
        quit()

    elif opt == "2":
        t.sleep(1)
        print("please contact HQ for futher steps.")
        t.sleep(1)
        print("*Application shutting down...*")
        quit()
    elif opt == "3":
        t.sleep(1)
        print("*Application shutting down...*")
        quit()
    else:
        t.sleep(1)
        print("Error: Not an option.")
