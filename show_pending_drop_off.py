"Show pending drop off"
import pandas as pd
from functions import getData
from data import getPendingDropOff


def showPendingDropOff():
    "Prints pending_drop_off table as dataFrame"
    data = getData(getPendingDropOff)

    columns = ["Name", "Quantity"]
    df = pd.DataFrame(data=data, columns=columns)
    pd.set_option('display.colheader_justify', 'center')

    print(df)
