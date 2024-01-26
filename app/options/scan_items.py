"Scan items"
import time as t
from scanners.items_scanner import ItemScanner
from functions import storeData

def scanItems(agent):
    '''
    Scans items by barcode
    Stores data into a database
    '''
    # Create scanners
    iScan = ItemScanner()

    # Scans barcodes and stores in data{}
    print('*Starting scanner...*')
    t.sleep(1)

    iScan.scanItems()
    itemData = iScan.getScanData()

    if len(itemData) > 0:
        # Stores scanned data into database
        storeData(itemData, agent.location.id, agent.id)
        t.sleep(1)
        print('\n*Data stored*\n')

    else:
        t.sleep(.5)
        print('\nNo Items were stored.\n')
        t.sleep(1)
