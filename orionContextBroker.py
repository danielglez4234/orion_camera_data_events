import requests

class orionContextBroker:
    def __init__(self, payload):
        
        self.payload = payload
        
        r = requests.patch('http://localhost:1026/v2/entities/')
        
        print("CRUD", str(self.payload))
