import sqlite3
import pytest
import pandas as pd
from main import *

@pytest.fixture
def dbConnection():
    # Setup: creates a temporary in-memory database and table
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users(
        userID INTEGER PRIMARY KEY AUTOINCREMENT,
        userName TEXT NOT NULL,
        permissionLevel INT NOT NULL
        )""")
    cursor.execute("""CREATE TABLE clients(
        clientID INTEGER PRIMARY KEY AUTOINCREMENT,
        clientName TEXT NOT NULL,
        contractStatus BOOLEAN NOT NULL,
        contractStartDate TEXT,
        contractEndDate TEXT,
        projectWork BOOLEAN NOT NULL,
        hqLongitude REAL,
        hqLatitude REAL,
        estimatedTotalRevenue REAL
        )""")
    
    columns = ["userName", "permissionLevel"]
    rows = [
        ('Isaac Patrickson', 9),
        ('John Doe', 1),
        ('Jane Doe', 2),
        ('Jacob Doe', 3),
        ('Jamie Doe', 4),
        ('Jonathan Doe', 5),
        ('Jemima Doe', 6),
        ('Jade Doe', 7),
        ('Jasper Doe', 8),
        ('Jessie Doe', 1)
    ]

    for row in rows:
        query = f"INSERT INTO users ({', '.join(columns)}) VALUES ({', '.join(['?' for _ in columns])})"
        try:
            cursor.execute(query, row)
        except:
            print("Hardcoded values corrupted, corrupted records may be skipped")
            
    conn.commit()
    
    yield conn, cursor  # Provides the connection and cursor to the test
    # Teardown: closes the cursor and connection
    cursor.close()
    conn.close()

def testGetTableWithPandas(dbConnection):
    conn, cursor = dbConnection
    usersTableWithData = "users"
    clientsTableWithNoData = "clients"
    populatedTable = getTableWithPandas(pd, conn, usersTableWithData)
    nonPopulatedTable = getTableWithPandas(pd, conn, clientsTableWithNoData)
    assert not populatedTable.empty
    assert nonPopulatedTable.empty
    
def testSelectAttribute(dbConnection):
    conn, cursor = dbConnection
    usersTableWithData = "users"
    selector1 = "userName"
    column1 = "userID"
    value1 = 4
    
    clientsTableWithNoData = "clients"
    selector2 = "clientName"
    column2 = "clientID"
    value2 = 1
    assert selectAttribute(cursor, selector1, usersTableWithData, column1, value1) == ('Jacob Doe',)
    assert selectAttribute(cursor, selector2, clientsTableWithNoData, column2, value2) == None
    
def testSelectAttributesWithPandas(dbConnection):
    conn, cursor = dbConnection
    selector = "userName"
    usersTableWithData = "users"
    column1 = "permissionLevel"
    value1 = 1
    column2 = "permissionLevel"
    value2 = 99
    populatedTable = selectAttributesWithPandas(pd, conn, selector, usersTableWithData, column1, value1)
    nonPopulatedTable = selectAttributesWithPandas(pd, conn, selector, usersTableWithData, column2, value2)
    assert not populatedTable.empty
    assert nonPopulatedTable.empty
    
def testGetClientColumnNames(dbConnection):
    conn, cursor = dbConnection
    assert getClientColumnNames(cursor) == ['clientID', 'clientName', 'contractStatus', 
                                            'contractStartDate', 'contractEndDate', 'projectWork', 
                                            'hqLongitude', 'hqLatitude', 'estimatedTotalRevenue']
    
def testCheckIfInputInTable(dbConnection):
    conn, cursor = dbConnection
    selectedValuesInColumn = "userID"
    table = 'users'
    inputValue1 = 4 
    inputValue2 = 1232534
    assert checkIfInputInTable(cursor, selectedValuesInColumn, table, inputValue1) == True
    assert checkIfInputInTable(cursor, selectedValuesInColumn, table, inputValue2) == False
    
def testGetColumnDataType(dbConnection):
    conn, cursor = dbConnection
    tableName = "clients"
    columnName1 = "clientName"
    columnName2 = "clientID"
    columnName3 = "estimatedTotalRevenue"
    columnName4 = "projectWork"
    assert getColumnDataType(cursor, tableName, columnName1) == "TEXT"
    assert getColumnDataType(cursor, tableName, columnName2) == "INTEGER"
    assert getColumnDataType(cursor, tableName, columnName3) == "REAL"
    assert getColumnDataType(cursor, tableName, columnName4) == "BOOLEAN"
    