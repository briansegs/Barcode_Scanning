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

inventory = [
    {
        "item_id" : 1,
        "quantity" : 100
    },
    {
        "item_id" : 2,
        "quantity" : 100
    },
    {
        "item_id" : 3,
        "quantity" : 100
    },
    {
        "item_id" : 4,
        "quantity" : 100
    },
    {
        "item_id" : 5,
        "quantity" : 100
    },
    {
        "item_id" : 6,
        "quantity" : 100
    }
]

createTables = '''
    DROP TABLE IF EXISTS Scan; 
    CREATE TABLE Scan (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'date' NUMERIC, 
        'time' NUMERIC,
        'quantity' INTEGER, 
        'item_id' INTEGER, 
        'agent_id' INTEGER, 
        'location_id' INTEGER
        )
    '''

insertScan = '''
    INSERT OR IGNORE INTO Scan (
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
    FROM Agents 
    WHERE barcode = ?
    '''

getLocations = '''
    SELECT 
        id, 
        name 
    FROM Locations
    '''

updateInventory = '''
        UPDATE Inventory 
        SET quantity = quantity + ? 
        WHERE Item_id = ?
    '''
