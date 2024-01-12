"Shows drop off log"
import time as t
from util import getOption, shutDown, optionError
from data import dropOffLogOptions

while True:
    opt = getOption("Drop off Log options: ", dropOffLogOptions)

    if opt == "1":
        pass

    elif opt == "2":
        pass

    elif opt == "3":
        pass

    elif opt == "4":
        break

    elif opt == "5":
        shutDown()

    else:
        t.sleep(1)
        optionError(opt)
