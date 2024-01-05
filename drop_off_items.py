"Drop off items"
import time as t
from functions import getAgent
from util import getCursorConnection, getDate, getTime

# TODO: Refactor option 1
# TODO: Name items and quantities when dropping off

# Login
print('Login to start scanning.')
t.sleep(1)

agent, agentId = getAgent()

print(f"Welcome {agent}. Were all items delivered successfully?")
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
        getItemName = '''
        SELECT name FROM item WHERE id = ?
        '''

        t.sleep(1)
        print("Items dropped off: ")
        print("")

        for i in lst:
            itemId = i[0]
            quantity = i[1]
            date = getDate()
            time = getTime()

            cur.execute(insertDropOffLog,
                (date, time, quantity, itemId, agentId))

            cur.execute(clearPendingDropOff, (itemId,))

            res = cur.execute(getItemName,(itemId,))
            tup = res.fetchone()
            name = tup[0]

            print(f'    {quantity}  {name}')

        conn.commit()
        conn.close()

        print("")
        t.sleep(1)
        print("Items added to drop off log.")
        t.sleep(1)
        print("*Application shutting down...*")
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
