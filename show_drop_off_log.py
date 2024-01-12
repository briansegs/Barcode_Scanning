"Shows drop off log"
import time as t
from util import getOption, shutDown, optionError
from functions import showDataFrame
from data import dropOffLogOptions, ascOrDescOptions

while True:
    opt = getOption("Drop off Log options: ", dropOffLogOptions)

    if opt == "1":
        while True:
            opt = getOption("options: ", ascOrDescOptions)

            if opt == "1":
                getDropOffLogAsc = '''
                SELECT 
                    drop_off_log.id,
                    date,
                    time,
                    quantity,
                    item.name,
                    agent.first_name,
                    agent.last_name
                FROM 
                    drop_off_log
                JOIN 
                    item 
                JOIN 
                    agent 
                ON 
                    drop_off_log.item_id = item.id 
                AND
                    drop_off_log.agent_id = agent.id
                ORDER BY 
                    date ASC, time ASC
                '''

                dropOffLogColumns = ["ID", "Date", "Time", "Quantity",
                "Item", "Agent", "Name"]

                showDataFrame(
                    "All", 
                    getDropOffLogAsc,
                    None,
                    "Ascending",
                    dropOffLogColumns
                )
                break

            elif opt == "2":
                break

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
