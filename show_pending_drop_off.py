"Show pending drop off"
from functions import showDataFrame
from data import getPendingDropOff, pendingDropOffColumns

def showPendingDropOff():
    "Prints pending_drop_off table as dataFrame"
    showDataFrame(
        "Items pending drop off",
        getPendingDropOff,
        None,
        "",
        pendingDropOffColumns
    )
