"queries"

createAgentTable = '''
        DROP TABLE IF EXISTS agent;
        CREATE TABLE agent (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'barcode' TEXT,
            'first_name' TEXT,
            'last_name' TEXT
            );
    '''

addAgents = '''
        INSERT OR IGNORE INTO agent (barcode, first_name, last_name) 
        VALUES (:barcode, :first_name, :last_name)
        '''

createItemsTable = '''
        DROP TABLE IF EXISTS item;
        CREATE TABLE item (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'barcode' TEXT,
            'name' TEXT
        );
    '''

addItems = '''
        INSERT OR IGNORE INTO item (barcode, name) 
        VALUES (:barcode, :name)
        '''

createLocationsTable = '''
        DROP TABLE IF EXISTS location;
        CREATE TABLE location (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'name' TEXT
        );
    '''

addLocations = '''
    INSERT OR IGNORE INTO location (name) 
    VALUES (?)
'''

createPendingDropOffTable = '''
        DROP TABLE IF EXISTS pending_drop_off;
        CREATE TABLE pending_drop_off (
            'item_id' INTEGER,
            'quantity' INTEGER
        );
    '''

addPendingDropOff = '''
    INSERT OR IGNORE INTO pending_drop_off (item_id, quantity) 
    VALUES (:item_id, :quantity)
'''

createDropOffLogTable = '''
        DROP TABLE IF EXISTS drop_off_log;
        CREATE TABLE drop_off_log (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'date' NUMERIC, 
            'time' NUMERIC,
            'quantity' INTEGER, 
            'item_id' INTEGER, 
            'agent_id' INTEGER
        );
    '''

createItemScanTable = '''
    DROP TABLE IF EXISTS item_scan;
    CREATE TABLE item_scan (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'date' NUMERIC, 
        'time' NUMERIC,
        'quantity' INTEGER, 
        'item_id' INTEGER, 
        'agent_id' INTEGER, 
        'location_id' INTEGER
        )
    '''
