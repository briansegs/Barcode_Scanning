"Shows drop off log"
import time as t
from util import getOption, shutDown, optionError
from functions import showDataFrame, getFromList
from data import (
    dropOffLogOptions,
    ascOrDescOptions,
    getDropOffLogAsc,
    dropOffLogColumns,
    getDropOffLogDesc,
    getdropOffLogDates,
    getDropOffLogsByDate
)

while True:
    opt = getOption("Drop off Log options: ", dropOffLogOptions)

    if opt == "1":
        while True:
            opt = getOption("options: ", ascOrDescOptions)

            if opt == "1":
                showDataFrame(
                    "All", 
                    getDropOffLogAsc,
                    None,
                    "Ascending",
                    dropOffLogColumns
                )
                break

            elif opt == "2":
                showDataFrame(
                    "All", 
                    getDropOffLogDesc,
                    None,
                    "Descending",
                    dropOffLogColumns
                )
                break

    elif opt == "2":
        date, _ = getFromList("Date", getdropOffLogDates)
        showDataFrame(
            "Date",
            getDropOffLogsByDate,
            date,
            date,
            dropOffLogColumns
        )

    elif opt == "3":
        pass

    elif opt == "4":
        break

    elif opt == "5":
        shutDown()

    else:
        t.sleep(1)
        optionError(opt)
