"Drop off items"
import time as t
from functions import updateDropOffLog
from util import shutDown, optionError

def dropOffItems(agent):
    '''
    Handles item drop off 
    Returns nothing 
    '''
    print("Were all items delivered successfully?")
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
            updateDropOffLog(agent.id)
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
