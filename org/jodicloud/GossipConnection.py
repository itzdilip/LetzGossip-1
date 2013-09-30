import ConfigParser

class GossipConnection():
    
    
    def __init__(self):
        
        # Reading the configuration file
        self.config = ConfigParser.ConfigParser()
        self.config.read('gossip.conf')
        self.reqConnection = self.config.get('GOSSIP_SEND', 'tcp_connect')   
        self.recvConnection = self.config.get('GOSSIP_RECIVE', 'tcp_bind')  
        self.port = self.config.get('DEFAULT','PORT')
        
    def getConnection(self,ipAddr=0):
        
        if ipAddr != 0:
            self.connectionStr = self.reqConnection + ipAddr + self.port
            
        else:
             self.connectionStr = self.recvConnection + self.port
         
        return (self.connectionStr)     
    
    def getPort(self):
        return (self.port)

        
    
