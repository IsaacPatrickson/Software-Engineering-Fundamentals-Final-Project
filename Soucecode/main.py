import sqlite3
import time
import pandas as pd
from SQLiteDatabase.InitDatabase import *
from SQLQueries import *
from userClass import *
from clientClass import *

# Connect to a (new) database
try:
    connection = sqlite3.connect("SQLiteDatabase/mediaworksUsersAndClients.db")
    cursor = connection.cursor()
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")
    
createUsersTable(cursor)
createClientsTable(cursor)
hardcodeValues(cursor, isTablePopulated(cursor, "users") and isTablePopulated(cursor, "clients"))
# checkTableContents(cursor)

# Displays the login menu   
def login_menu():
    # This while loop will validate the user's choice of action at the Login Menu
    loginMenuValid = False
    while loginMenuValid == False:
        print()
        print("MAIN MENU")
        print()
        print(" 1. Login")
        print(" 0. Quit")
        print()
        choice = input("Select 1 or 0: ")
        
        if choice == "1":
            loginMenuValid = True
            
            login = User()
            userNameInput = False
            while userNameInput == False:
                inputName = input("(Enter '0' to Abort) Enter your username: ")
                if login.validateUserName(inputName):
                    if login.isUserNameInTable(selectAttribute(cursor, "userName", "users", "userName", inputName)):
                        login.setExistingUserName(inputName)
                        login.setLoginStatus(True)
                        print()
                        print(f"Welcome to the Client Information Management System, {inputName}")
                        userNameInput = True
                    else:
                        print("The entered username is not in our database")
                        time.sleep(3)
                else:
                    if inputName == "0":
                        login_menu()
                    else:
                        print("Characters must belong to the alphabet (spaces included)")
                        time.sleep(3)
            
            while login.getLoginStatus() == True:
                permissionLevel = []
                clientsTable = getTableWithPandas(pd, connection, "clients")
                
                print()
                print(clientsTable)
                print()
                values = selectAttribute(cursor, "permissionLevel", "users", "userName", inputName)
                for value in values:
                    login.setExistingPermissionLevel(value)
                permissionLevel = login.getPermissionLevel()
                if permissionLevel == 9:
                    choice = []
                    print("ADMIN MENU")
                    print()
                    print("(1) Amend client information")
                    print("(2) Add a client")
                    print("(3) Remove a client")
                    print("(4) Search for clients")
                    print("(0) Log out")
                    print()
                    choice = int(input("Enter (0-4) to select an option: "))
                    if choice == 1:
                        print("Amend")
                    elif choice == 2:
                        print("Add")   
                    elif choice == 3:
                        print("Remove")   
                    elif choice == 4:
                        print("Search")
                    elif choice == 0:
                        print()
                        login.setLoginStatus(False) 
                        
                elif permissionLevel == 1:
                    choice = []
                    print("EMPLOYEE MENU")
                    print()
                    print("(1) Search for clients")
                    print("(0) Log out")
                    print()
                    choice = int(input("Enter (0-1) to select an option: "))
                    if choice == 1:
                        print("Search")
                    elif choice == 0:
                        print()
                        login.setLoginStatus(False) 
            
            loginMenuValid = False            
                        
            
            
            # if login.setExistingUserName(login.isUserNameInTable(cursor, inputName), inputName):
            #     print(f"Welcome, {inputName}")
            # else:
            #     pass
                
            # if login.validateUserName(inputName):
            #     try:
            #         login.isUserNameInTable(cursor, inputName)
            #     except sqlite3.OperationalError as e:
            #         print(f"An error occurred: {e}")
            # else:
            #     print("Invalid name! Please enter only alphabetic characters and spaces.")
            
            # print(login.getUserName)
            #         print()
            #         login.set_email(input("Email address: "))
            #         userEmail = login.get_email()
            #         query = "SELECT salt FROM user WHERE email = %s"
            #         cursor.execute(query, (userEmail,))
            #         for salt in cursor:
            #             userSalt = ("{}".format(salt))
            #             userSalt = userSalt.replace("'","")
            #             userSalt = userSalt.replace("(","")
            #             userSalt = userSalt.replace(")","")
            #             userSalt = userSalt.replace(",","")
            #         query = "SELECT passwordHash FROM user WHERE email = %s"
            #         cursor.execute(query, (userEmail,))
            #         for passwordHash in cursor:
            #             userHPassword = ("{}".format(passwordHash))
            #             userHPassword = userHPassword.replace("'","")
            #             userHPassword = userHPassword.replace("(","")
            #             userHPassword = userHPassword.replace(")","")
            #             userHPassword = userHPassword.replace(",","")
            #         check = check_password(userSalt, userHPassword, input("Password: "))
            #         break
            # #     # If the email entered does not exist and a salt cannot be selected,
            # #     # the error will be dealt with using exception handling
                # except:
                #     print("Error! An account with this email does not exist")
                #     print()
                #     login_menu()

            # # If the email does exist in the database and the passwords match,
            # # the user is sent to the User Menu        
            # if check == True:
            #     email = login.get_email()
            #     login.set_user_id(email)
            #     name = name_selector(login.get_user_id())
            #     print()
            #     print("Login Successful")
            #     print("Welcome,", name)
            #     user_menu(login.get_email(), login.get_user_id())

            # If the password does not match, the user is sent back to the Login Menu    
            # else:
            #     print("Error! Incorrect username")
            #     print()
            #     login_menu()
                
        # If the User has chosen to exit the program, the program will close    
        elif choice == "0":
            loginMenuValid = True
            exit()
            
        else:
            print("Error! Input must be an integer preceding one of the options above")   
    
    
    
    
    
login_menu()
    
    
# Committing all changes to the database
connection.commit()

# Close connection
connection.close()