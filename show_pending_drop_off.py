"Show pending drop off"
import time as t
from functions import getData, getDataFrame
from data import getPendingDropOff, pendingDropOffColumns


def showPendingDropOff():
    "Prints pending_drop_off table as dataFrame"
    data = getData(getPendingDropOff)
    df = getDataFrame(data, pendingDropOffColumns)

    t.sleep(1)
    print("   Items pending drop off: \n")
    print(df, "\n")
    t.sleep(1)
