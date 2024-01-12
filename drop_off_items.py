"Drop off items"
import time as t
from functions import updateDropOffLog
from util import shutDown, optionError, getOption
from data import dropOffOptions

def dropOffItems(agent):
    '''
    Handles item drop off 
    Returns nothing 
    '''
    while True:
        print("Were all items delivered successfully? \n")
        t.sleep(.5)
        opt = getOption("Options: ", dropOffOptions)

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
