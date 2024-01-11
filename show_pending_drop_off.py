"Show pending drop off"
from functions import getData, getDataFrame
from data import getPendingDropOff, pendingDropOffColumns


def showPendingDropOff():
    "Prints pending_drop_off table as dataFrame"
    data = getData(getPendingDropOff)
    df = getDataFrame(data, pendingDropOffColumns)

    print("")
    print(df, "\n")
