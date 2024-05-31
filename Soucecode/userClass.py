class User():
    
    def __init__(self) -> None:
        # Initialize a new 'User' instance with default values
        self._userName           = ""
        self._permissionLevel    = []
        self._loginStatus        = False
            
    def setExistingUserName(self, inputName):
        self._userName = inputName
        
    def setExistingPermissionLevel(self, result):
        self._permissionLevel = result     
        
    def setLoginStatus(self, loginStatus):
        self._loginStatus = loginStatus
        
    def getUserName(self):
        return self._userName
    
    def getPermissionLevel(self):
        return self._permissionLevel
    
    def getLoginStatus(self):
        return self._loginStatus
    

def validateUserName(re, inputName):
    # Creating a pattern using the Regular Expressions(RE) library
    # The pattern includes all letters of the alphabet (uppercase and lowercase) and blank spaces
    pattern = r'^[a-zA-Z\s]+$'
    
    # Using the RE library, I have check if the input matches the pattern
    if re.match(pattern, inputName):
        return True
    else:
        return False
    
def isUserNameInTable(result):
    if result:
        return True
    else:
        return False