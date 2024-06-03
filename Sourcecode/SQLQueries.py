# Using pandas to return a formatted table that can neatly displayed in the console
def getTableWithPandas(pd, connection, table):
    neatTable = pd.read_sql_query(f"SELECT * FROM {table}", connection)
    return neatTable

# Reusable SQL select command
def selectAttribute(cursor, selector, table, column, value):
    query = f"SELECT {selector} FROM {table} WHERE {column} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()
    return result

# Using pandas to select specific records in a table
# Used for search function
def selectAttributesWithPandas(pd, connection, selector, table, column, value):
    query = f"SELECT {selector} FROM {table} WHERE {column} = ?"
    results = pd.read_sql_query(query, connection, params=(value,))
    return results

# Reusable SQL command that gets all the column names in a table
def getClientColumnNames(cursor):
    cursor.execute("""SELECT clientID, clientName, contractStatus, contractStartDate,
                contractEndDate, projectWork, hqLongitude, hqLatitude, estimatedTotalRevenue 
                FROM clients""")
    # Fetch the column names
    columnNames = [description[0] for description in cursor.description]
    return columnNames

# Selects all records from a table that matches the users input value
def checkIfInputInTable(cursor, selectedValuesInColumn, table, inputValue):
    query = f"SELECT {selectedValuesInColumn} FROM {table}"
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        if str(inputValue) == str(result[0]):
            return True
        else:
            pass
    return False

# Update an attribute value in a table
def replaceAttribute(cursor, table, columnToUpdate, newValue, conditionColumn, conditionValue):
    query = f"""
    UPDATE {table} 
    SET {columnToUpdate} = ? 
    WHERE {conditionColumn} = ?
    """
    cursor.execute(query, (newValue, conditionValue))
    
# Gathering table info and iterating through each item in the list generated
# If the column name matches the user input column name
# return the column's datatype    
def getColumnDataType(cursor, tableName, columnName):
    cursor.execute(f"PRAGMA table_info({tableName})")
    columnsInfo = cursor.fetchall()
        
    for column in columnsInfo:
        if column[1] == columnName:
            typeName = []
            for char in column[2]:
                if char == "(":
                    break
                else:
                    typeName.append(char)
            typeName = "".join(typeName)
            return typeName
        
    return None    

# Adding a record to a table
def insertInto(cursor, tableName, columns, values):
    query = f"INSERT INTO {tableName} ({', '.join(columns)}) VALUES ({', '.join(['?' for _ in values])})"
    cursor.execute(query, values)

# removing a record from a table
def removeRecord(cursor, tableName, column, value):
    query = f"DELETE FROM {tableName} WHERE {column} = ?"
    cursor.execute(query, (value,))