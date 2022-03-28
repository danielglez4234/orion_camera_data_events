import json
from orionContextBroker import orionContextBroker


class Event:
    def __init__(self, message):
        
        self.data = message["data"]
        self.action = message["action"]
        
    def toOrionEntitie(self, id):
        raise NotImplementedError()
    
    
class VideoMotion(Event): 
    def toOrionEntitie(self, id): 
        print("videoMo")
        dataJn = json.loads(self.data)
        payload = {
            "state": {
                "type": "String",
                "value": self.action
            },
            "regionName": {
                "type": "ArrayList",
                "value": dataJn["RegionName"]
            }
        }
        print(str(payload))
        return payload
        
        
class CrossRegionDetection(Event):
    def toOrionEntitie(self, id): 
        dataJn = json.loads(self.data)
        payload = {
            "state": {
                "type": "String",
                "value": self.action
            },
            "regionName": {
                "type": "ArrayList",
            }
        }
        print(str(payload))
        return payload



class CrossLineDetection(Event):
    def toOrionEntitie(self, id): 
        payload = {
            "state": {
                "type": "String",
                "value": self.action
            },
            "regionName": {
                "type": "ArrayList",
            }
        }
        print(str(payload))
        return payload


class TakenAwayDetection(Event):
    def toOrionEntitie(self, id): 
        payload = {
            "state": {
                "type": "String",
                "value": self.action
            },
            "regionName": {
                "type": "ArrayList",
  
            }
        }
        print(str(payload))
        return payload