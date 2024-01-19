"Show pending drop off"
from functions import showDataFrame
from data import getPendingDropOffName, pendingDropOffColumns

def showPendingDropOff():
    "Prints pending_drop_off table as dataFrame"
    showDataFrame(
        "Items pending drop off",
        getPendingDropOffName,
        None,
        "",
        pendingDropOffColumns
    )
