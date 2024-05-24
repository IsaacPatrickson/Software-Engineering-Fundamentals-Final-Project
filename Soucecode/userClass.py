import re

class User():
    
    def __init__(self) -> None:
        self.userName        = ""
        self.permissionLevel = ""
        self.loginStatus     = ""
        
    def validateUserName(self, inputName):
        # Creating a pattern using the Regular Expressions(RE) library
        # The pattern includes all letters of the alphabet (uppercase and lowercase) and blank spaces
        pattern = r'^[a-zA-Z\s]+$'
        
        # Using the RE library, I have check if the input matches the pattern
        if re.match(pattern, inputName):
            return True
        else:
            return False
        
    def isUserNameInTable(self, cursor, inputName):
        cursor.execute("SELECT userName FROM users WHERE userName = ?", (inputName,))
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False
            
    def setExistingUserName(self, inputName):
        self.userName = inputName
        
    def getUserName(self):
        return self.userName