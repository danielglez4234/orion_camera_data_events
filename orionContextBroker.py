import requests

class orionContextBroker:
    def __init__(self, payload):
        
        self.payload = payload
        url = 'localhost:1026/v2/entities/'+self.payload["id"]+'/attrs?options=append'
        setheader = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        
        print("CRUD", str(self.payload))
    
        try:
            r = requests.patch(url, json=self.payload, headers=setheader)
        except requests.exceptions.RequestException as e:
            # print("The entitie requested does not exsist... Proceeding to create a new entitie")    
            raise SystemExit(e)
        # except requests.exceptions.Timeout:
        #     # Maybe set up for a retry, or continue in a retry loop
        # except requests.exceptions.TooManyRedirects:
        #     # Tell the user their URL was bad and try a different one
        # except requests.exceptions.RequestException as e:
        #     # catastrophic error. bail.
        #     raise SystemExit(e)


        # r = requests.post(url, json = self.payload, headers = setheader)
