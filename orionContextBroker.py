import requests

class orionContextBroker:
    def __init__(self, payload):
        
        self.payload = payload
        print("CRUD", str(self.payload))
        
        # r = requests.patch('http://localhost:1026/v2/entities/')
        
