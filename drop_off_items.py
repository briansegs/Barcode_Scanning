"Drop off items"
import time as t
from functions import getAgent, updateDropOffLog

# TODO: Refactor option 1

# Login
print("Login to continue. ")
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
        updateDropOffLog(agentId)

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
