"Drop off items"
import time as t
from functions import getAgent, updateDropOffLog
from util import shutDown, optionError

def dropOffItems():
    '''
    Handles item drop off 
    Returns nothing 
    '''

    # Login
    print("Login to continue. ")
    t.sleep(1)

    agent, agentId = getAgent()

    print(f"Welcome {agent}. Were all items delivered successfully?")
    t.sleep(.5)

    # Options
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
            shutDown()

        elif opt == "2":
            t.sleep(1)
            print("please contact HQ for futher steps.")
            shutDown()

        elif opt == "3":
            shutDown()

        else:
            t.sleep(1)
            optionError(opt)
