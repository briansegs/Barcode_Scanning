"App data"

database = 'testDb.sqlite'

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

items = [
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

pendingDropoff = [
    {
        "item_id" : 1,
        "quantity" : 0
    },
    {
        "item_id" : 2,
        "quantity" : 0
    },
    {
        "item_id" : 3,
        "quantity" : 0
    },
    {
        "item_id" : 4,
        "quantity" : 0
    },
    {
        "item_id" : 5,
        "quantity" : 0
    },
    {
        "item_id" : 6,
        "quantity" : 0
    }
]

createPendingScanTable = '''
    DROP TABLE IF EXISTS pending_scan; 
    CREATE TABLE pending_scan (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'date' NUMERIC, 
        'time' NUMERIC,
        'quantity' INTEGER, 
        'item_id' INTEGER, 
        'agent_id' INTEGER, 
        'location_id' INTEGER
        )
    '''

insertPendingScan = '''
    INSERT OR IGNORE INTO pending_scan (
        date,
        time,
        quantity,
        item_id,
        agent_id,
        location_id
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    '''

getAgent = '''
    SELECT
        id,
        first_name, 
        last_name, 
        barcode 
    FROM agent 
    WHERE barcode = ?
    '''

getLocations = '''
    SELECT 
        id, 
        name 
    FROM location
    '''

updatePendingDropoff = '''
        UPDATE pending_dropoff 
        SET quantity = quantity + ? 
        WHERE item_id = ?
    '''
