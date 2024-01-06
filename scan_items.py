"Scan items"
import time as t
from items_scanner import ItemScanner
from functions import storeData, getLocation, getAgent
from util import shutDown

def scanItems():
    '''
    Logs in an Agent
    Scans items by barcode
    Stores data into a database
    Returns nothing
    '''

    # Create scanners
    iScan = ItemScanner()

    # Login process
    print('Login to start scanning.')
    t.sleep(1)

    agent, agentId = getAgent()

    locationId, location = getLocation()

    print(f'Welcome {agent}. You are logged into the {location} location.')
    t.sleep(1)

    # Scans barcodes and stores in data{}
    print('*Starting scanner...*')
    t.sleep(1)

    iScan.scanItems()
    itemData = iScan.getScanData()

    if len(itemData) == 0:
        print('No Items were scanned.')
        shutDown()

    # Stores scanned data into database
    storeData(itemData, locationId, agentId)
    t.sleep(1)
    print('*Data stored*')
