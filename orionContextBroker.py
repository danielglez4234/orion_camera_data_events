import requests

from configparser import ConfigParser

class orionContextBroker:
    def __init__(self, payload):
        
        self.payload = payload
        config = ConfigParser()
        config.read('config.ini')
        
        host = config['ORION_CONECCTION']['host']
        port = config['ORION_CONECCTION']['port']
        # print(url)

        # url_update = 'localhost:1026/v2/entities/'+self.payload["id"]+'/attrs?options=append'
        
        headers = {
            "Accept": "application/json",
            "fiware-service": "gtc",
            "fiware-servicePath": "/"
        }
        
        r = requests.get("http://localhost:1026/v2/entities/", headers=headers)
        
        
        print(r.text)
        
        
        # print("CRUD", str(self.payload))
    
        # try:
        #     r = requests.patch(url, data=self.payload, headers=setheader)
        #     print(str(r.text))
        # except requests.exceptions.RequestException as e:
        #     # print("The entitie requested does not exsist... Proceeding to create a new entitie")    
        #     r = requests.patch(url, json=self.payload, headers=setheader)
        # except requests.exceptions.Timeout:
        #     # Maybe set up for a retry, or continue in a retry loop
        # except requests.exceptions.TooManyRedirects:
        #     # Tell the user their URL was bad and try a different one
        # except requests.exceptions.RequestException as e:
        #     # catastrophic error. bail.
        #     raise SystemExit(e)


        # r = requests.post(url, json = self.payload, headers = setheader)
