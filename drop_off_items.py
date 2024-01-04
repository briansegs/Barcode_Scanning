"Drop off items"
import time as t
from functions import getAgent

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
        break
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
