"Show pending drop off"
import pandas as pd
from functions import getData

def showPendingDropOff():
    "Prints pending_drop_off table as dataFrame"
    getPendingDropOff = '''
        SELECT
            item.name,
            quantity
        FROM 
            pending_drop_off
        JOIN 
            item
        ON
            pending_drop_off.item_id = item.id
    '''
    data = getData(getPendingDropOff)

    columns = ["Name", "Quantity"]
    df = pd.DataFrame(data=data, columns=columns)
    pd.set_option('display.colheader_justify', 'center')

    print(df)
