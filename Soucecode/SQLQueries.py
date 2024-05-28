def printTableWithPandas(pd, connection):
    neatTable = pd.read_sql_query("SELECT * FROM clients", connection)
    return neatTable
    
def selectOneCase(cursor, selector, table, condition, value):
    cursor.execute("SELECT ? FROM ? WHERE ? = ?", (selector, table, condition, value,))
    result = cursor.fetchone()
    return result

def selectAllCases(cursor, selector, table, condition, value):
    cursor.execute("SELECT ? FROM ? WHERE ? = ?", (selector, table, condition, value,))
    result = cursor.fetchall()
    return result