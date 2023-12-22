"App data"

database = 'testDb.sqlite'

states = {
        "ny" : "New York",
        "nj" : "New Jersey",
        "pa" : "Pennsylvinia",
        "fl" : "Florida"
    }

agents = [
        {
            "barcode" : "1017574074152",
            "first_name" : "Brian",
            "last_name" : "Segs"
        },
        {
            "barcode" : "1013447692447",
            "first_name" : "Tom",
            "last_name" : "Mango"
        },
        {
            "barcode" : "1015241102962",
            "first_name" : "Ron",
            "last_name" : "Law"
        },
        {
            "barcode" : "1019148016353",
            "first_name" : "Barb",
            "last_name" : "Beetle"
        }
    ]

inventory = [
        {
            "barcode" : "0052000135138",
            "name" : "Gatorade Fruit Punch"
        },
        {
            "barcode" : "0049000079388",
            "name" : "Power ADE Fruit Punch"
        },
        {
            "barcode" : "0012000811197",
            "name" : "Pepsi Wild Cherry"
        },
        {
            "barcode" : "0050428327937",
            "name" : "Caliber Composition Book"
        },
        {
            "barcode" : "0012546011075",
            "name" : "Trident Spearmint"
        },
        {
            "barcode" : "0070330000025",
            "name" : "BIC Lighter Blk sm"
        }
    ]

locations = [
        "New York",
        "New Jersey",
        "Pennsylvinia",
        "Florida"
    ]

createTables = '''
    DROP TABLE IF EXISTS Items; 
    CREATE TABLE Items (
        'scan_agent' TEXT, 
        'scan_agent_code' TEXT, 
        'scan_location' TEXT, 
        'barcode' TEXT, 
        'name' TEXT, 
        'quantity' INTEGER, 
        'scan_date' NUMERIC, 
        'scan_time' NUMERIC
        )
    '''

insertItems = '''
    INSERT OR IGNORE INTO Items (
        scan_agent, 
        scan_agent_code, 
        scan_location, 
        barcode, 
        name, 
        quantity, 
        scan_date, 
        scan_time
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''

getAgent = '''
    SELECT 
        first_name, 
        last_name, 
        barcode 
    FROM Agents 
    WHERE barcode = ?
    '''

getLocations = '''
    SELECT 
        id, 
        name 
    FROM Locations
    '''
