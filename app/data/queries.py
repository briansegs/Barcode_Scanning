"queries"

insertItemScan = '''
    INSERT OR IGNORE INTO item_scan (
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

updatePendingDropOff = '''
        UPDATE pending_drop_off 
        SET quantity = quantity + ? 
        WHERE item_id = ?
    '''

getPendingDropOff = '''
        SELECT
            item.name,
            quantity,
            item_id
        FROM 
            pending_drop_off
        JOIN 
            item
        ON
            pending_drop_off.item_id = item.id
        WHERE 
            quantity > 0
    '''

insertDropOffLog = '''
    INSERT OR IGNORE INTO drop_off_log (
        date,
        time,
        quantity,
        item_id,
        agent_id
    )
    VALUES (?, ?, ?, ?, ?)
    '''

clearPendingDropOff = '''
    UPDATE pending_drop_off
    SET quantity = 0
    WHERE item_id = ?
    '''

getItemName = '''
    SELECT name FROM item WHERE id = ?
    '''

getItemScansAsc = '''
    SELECT 
    item_scan.id,
    date,
    time,
    quantity,
    item.name,
    agent.first_name,
    agent.last_name,
    location.name
    FROM item_scan
    JOIN item JOIN agent JOIN location
    ON 
    item_scan.item_id = item.id 
    AND
    item_scan.agent_id = agent.id 
    AND
    item_scan.location_id = location.id
    ORDER BY 
    date ASC, time ASC
    '''

getItemScansDesc = '''
    SELECT 
    item_scan.id,
    date,
    time,
    quantity,
    item.name,
    agent.first_name,
    agent.last_name,
    location.name
    FROM item_scan
    JOIN item JOIN agent JOIN location
    ON 
    item_scan.item_id = item.id 
    AND
    item_scan.agent_id = agent.id 
    AND
    item_scan.location_id = location.id
    ORDER BY 
    date DESC, time DESC
    '''

getScansBylocationId = '''
    SELECT 
    item_scan.id,
    date,
    time,
    quantity,
    item.name,
    agent.first_name,
    agent.last_name,
    location.name
    FROM item_scan
    JOIN item JOIN agent JOIN location
    ON 
    item_scan.item_id = item.id 
    AND
    item_scan.agent_id = agent.id 
    AND
    item_scan.location_id = location.id
    WHERE location_id = ? 
    '''

getAgents = '''
    SELECT
        id,
        first_name,
        last_name
    FROM 
        agent
    '''

getScansByAgentId = '''
    SELECT 
    item_scan.id,
    date,
    time,
    quantity,
    item.name,
    agent.first_name,
    agent.last_name,
    location.name
    FROM item_scan
    JOIN item JOIN agent JOIN location
    ON 
    item_scan.item_id = item.id 
    AND
    item_scan.agent_id = agent.id 
    AND
    item_scan.location_id = location.id
    WHERE agent_id = ? 
    '''

getScanDates = '''
    SELECT
        date
    FROM
        item_scan
    '''

getScansByDate = '''
        SELECT 
        item_scan.id,
        date,
        time,
        quantity,
        item.name,
        agent.first_name,
        agent.last_name,
        location.name
        FROM item_scan
        JOIN item JOIN agent JOIN location
        ON 
        item_scan.item_id = item.id 
        AND
        item_scan.agent_id = agent.id 
        AND
        item_scan.location_id = location.id
        WHERE date = ? 
        '''

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

getDropOffLogDesc = '''
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
            date DESC, time DESC
        '''

getdropOffLogDates = '''
    SELECT
        date
    FROM
        drop_off_log
    '''

getDropOffLogsByDate = '''
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
        WHERE date = ? 
        '''

getDropOffLogsByAgent = '''
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
        WHERE agent_id = ? 
        '''
