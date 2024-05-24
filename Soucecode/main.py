import sqlite3
from SQLiteDatabase.InitDatabase import *

# Connect to a (new) database
try:
    connection = sqlite3.connect("SQLiteDatabase/mediaworksUsersAndClients.db")
    cursor = connection.cursor()
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")
    
createUsersTable(cursor)
createClientsTable(cursor)
hardcodeValues(cursor, isTablePopulated(cursor, "users") and isTablePopulated(cursor, "clients"))
tempCheckTableContents(cursor)
    
    
    
    
    
    
    
    
    
    
    
    
    
# Committing all changes to the database
connection.commit()

# Close connection
connection.close()