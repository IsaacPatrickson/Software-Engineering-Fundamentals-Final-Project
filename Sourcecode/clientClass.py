class Client():
    
    def __init__(self) -> None:
        # Initialize a new 'Client' instance with default values
        self._clientId               = []
        self._clientName             = []
        self._contractStatus         = []
        self._contractStartDate      = []
        self._contractEndDate        = []
        self._projectWork            = []
        self._hqLongitude            = []
        self._hqLatitude             = []
        self._estimatedTotalRevenue  = []
     
    def setClientName(self, clientName):
        self._clientName = clientName
        
    def setContractStatus(self, contractStatus):
        self._contractStatus = contractStatus
     
    def setContractStartDate(self, contractStartDate):
        self._contractStartDate = contractStartDate
        
    def setContractEndDate(self, contractEndDate):
        self._contractEndDate = contractEndDate
        
    def setProjectWork(self, projectWork):
        self._projectWork = projectWork
        
    def setHqLongitude(self, hqLongitude):
        self._hqLongitude = hqLongitude
        
    def setHqLatitude(self, hqLatitude):
        self._hqLatitude = hqLatitude
        
    def setEstimatedTotalRevenue(self, estimatedTotalRevenue):
        self._estimatedTotalRevenue = estimatedTotalRevenue
    
    
    def getClientName(self):
        return self._clientName
        
    def getContractStatus(self):
        return self._contractStatus
     
    def getContractStartDate(self):
        return self._contractStartDate
        
    def getContractEndDate(self):
        return self._contractEndDate
        
    def getProjectBasedWork(self):
        return self._projectWork
        
    def getHqLongitude(self):
        return self._hqLongitude
        
    def getHqLatitude(self):
        return self._hqLatitude
        
    def getEstimatedTotalRevenue(self):
        return self._estimatedTotalRevenue