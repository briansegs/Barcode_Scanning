"Scan items"
import time as t
from items_scanner import ItemScanner
from functions import storeData
from util import shutDown

def scanItems(agent):
    '''
    Logs in an Agent
    Scans items by barcode
    Stores data into a database
    Returns nothing
    '''

    # Create scanners
    iScan = ItemScanner()

    # Scans barcodes and stores in data{}
    print('*Starting scanner...*')
    t.sleep(1)

    iScan.scanItems()
    itemData = iScan.getScanData()

    if len(itemData) == 0:
        print('No Items were scanned.')
        shutDown()

    # Stores scanned data into database
    storeData(itemData, agent.location.id, agent.id)
    t.sleep(1)
    print('*Data stored*')
