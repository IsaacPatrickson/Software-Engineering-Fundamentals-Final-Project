def getTableWithPandas(pd, connection, table):
    neatTable = pd.read_sql_query(f"SELECT * FROM {table}", connection)
    return neatTable
    
def selectAttribute(cursor, selector, table, column, value):
    query = f"SELECT {selector} FROM {table} WHERE {column} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()
    return result

# def selectAllCases(cursor, selector, table, condition, value):
#     cursor.execute("SELECT ? FROM ? WHERE ? = ?", (selector, table, condition, value,))
#     result = cursor.fetchall()
#     return result