def getTableWithPandas(pd, connection, table):
    neatTable = pd.read_sql_query(f"SELECT * FROM {table}", connection)
    return neatTable
    
def selectAttribute(cursor, selector, table, column, value):
    query = f"SELECT {selector} FROM {table} WHERE {column} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()
    return result

def selectAttributesWithPandas(pd, connection, selector, table, column, value):
    query = f"SELECT {selector} FROM {table} WHERE {column} = ?"
    results = pd.read_sql_query(query, connection, params=(value,))
    return results

def validateAttributeToSeachBy(cursor, attributeName):
    cursor.execute("""SELECT clientID, clientName, contractStatus, contractStartDate,
                contractEndDate, projectWork, hqLongitude, hqLatitude, estimatedTotalRevenue 
                FROM clients""")
    # Fetch the column names
    columnNames = [description[0] for description in cursor.description]
    for columnName in columnNames:
        if attributeName == columnName:
            return True
        else:
            pass
    return False

# def selectAllCases(cursor, selector, table, condition, value):
#     cursor.execute("SELECT ? FROM ? WHERE ? = ?", (selector, table, condition, value,))
#     result = cursor.fetchall()
#     return result