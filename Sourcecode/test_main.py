import sqlite3
import pytest
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
    conn.commit()
    yield conn, cursor  # Provides the connection and cursor to the test
    # Teardown: closes the cursor and connection
    cursor.close()
    conn.close()


def testCompareDatatypes(dbConnection):
    conn, cursor = dbConnection
    stringTest = "HelloWorld"
    integerTest = 1
    floatTest = 1.1342234
    assert compareDatatypes(cursor, stringTest, "clients", "hqLatitude") == False
    assert compareDatatypes(cursor, integerTest, "clients", "hqLatitude") == False
    assert compareDatatypes(cursor, floatTest, "clients", "hqLatitude") == True
    
def testDetectAndConvertInput():
    stringTest = "HelloWorld"
    integerTest = 1
    floatTest = 1.1342234
    assert detectAndConvertInput(stringTest) == "HelloWorld"
    assert detectAndConvertInput(integerTest) == 1
    assert detectAndConvertInput(floatTest) == 1.1342234
    
def testGetMethodNamesInOrder():
    userMethods = ['setExistingUserName', 'setExistingPermissionLevel', 'setLoginStatus']
    clientMethods = ['setClientName', 'setContractStatus', 'setContractStartDate', 
                     'setContractEndDate', 'setProjectWork', 'setHqLongitude', 
                     'setHqLatitude', 'setEstimatedTotalRevenue']
    assert getMethodNamesInOrder(User) == userMethods
    assert getMethodNamesInOrder(Client) == clientMethods
    
def testAttributeNameMatchClientColumnName(dbConnection):
    conn, cursor = dbConnection
    attributeNameInTable = "clientName"
    attributeNameNotInTable = "Hello World"
    assert attributeNameMatchClientColumnName(cursor, attributeNameInTable) == True
    assert attributeNameMatchClientColumnName(cursor, attributeNameNotInTable) == False