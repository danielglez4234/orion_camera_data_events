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
        self.id = id
        dataJn = json.loads(self.data)
        payload = {
            "id": self.id,
            "Type": "camera_events",
            "Event_name": "VideoMotion",
            "State": {
                "type": "String",
                "value": self.action
            },
            "RegionName": {
                "type": "ArrayList",
                "value": dataJn["RegionName"]
            }
        }
        # print(str(payload))
        return payload
        
        
class CrossRegionDetection(Event):
    def toOrionEntitie(self, id): 
        self.id = id
        dataJn = json.loads(self.data)
        payload = {
            "id": self.id,
            "Type": "camera_events",
            "Event_name": "CrossRegionDetection",
            "State": {
                "type": "String",
                "value": self.action
            },
            "DetectRegion": {
                "type": "ArrayList",
                "value": dataJn["DetectRegion"]
            },
            "ObjectDetected": {
                "type": "Object",
                "Action": {
                    "type": "String",
                    "value": dataJn["Object.Action"]
                },
                "ObjectType" :{
                    "type": "String",
                    "value": dataJn["Object.ObjectType"]
                },
                "Speed": {
                    "type": "String",
                    "value": dataJn["Object.Speed"]
                },
                "SpeedTypeInternal":{
                    "type": "String",
                    "value": dataJn["Object.SpeedTypeInternal"]
                },
                "FrameLocation": {
                    "type": "Object",
                    "BoundingBox" : {
                        "type": "ArrayList",
                        "value": dataJn["Object.BoundingBox"]
                    },
                    "Center" : {
                        "type": "ArrayList",
                        "value": dataJn["Object.Center"]
                    }
                }
            }
        }
        # print(str(payload))
        return payload



class CrossLineDetection(Event):
    def toOrionEntitie(self, id): 
        self.id = id
        dataJn = json.loads(self.data)
        payload = {
            "id": self.id,
            "Type": "camera_events",
            "Event_name": "CrossLineDetection",
            "State": {
                "type": "String",
                "value": self.action
            },
            "DetectLine": {
                "type": "ArrayList",
                "value": dataJn["DetectLine"]
            },
            "Direction": {
                "type": "String",
                "value": dataJn["Direction"]
            },
            "ObjectDetected": {
                "type": "Object",
                "Action": {
                    "type": "String",
                    "value": dataJn["Object.Action"]
                },
                "ObjectType" :{
                    "type": "String",
                    "value": dataJn["Object.ObjectType"]
                },
                "Speed": {
                    "type": "String",
                    "value": dataJn["Object.Speed"]
                },
                "SpeedTypeInternal":{
                    "type": "String",
                    "value": dataJn["Object.SpeedTypeInternal"]
                },
                "FrameLocation": {
                    "type": "Object",
                    "BoundingBox" : {
                        "type": "ArrayList",
                        "value": dataJn["Object.BoundingBox"]
                    },
                    "Center" : {
                        "type": "ArrayList",
                        "value": dataJn["Object.Center"]
                    }
                }
            }
        }
        # print(str(payload))
        return payload


class TakenAwayDetection(Event):
    def toOrionEntitie(self, id): 
        self.id = id
        dataJn = json.loads(self.data)
        payload = {
            "id": self.id,
            "Type": "camera_events",
            "Event_name": "TakenAwayDetection",
            "State": {
                "type": "String",
                "value": self.action
            },
            "ObjectDetected": {
                "type": "Object",
                "Action": {
                    "type": "String",
                    "value": dataJn["Object.Action"]
                },
                "ObjectType" :{
                    "type": "String",
                    "value": dataJn["Object.ObjectType"]
                },
                "FrameLocation": {
                    "type": "Object",
                    "BoundingBox" : {
                        "type": "ArrayList",
                        "value": dataJn["Object.BoundingBox"]
                    },
                    "Center" : {
                        "type": "ArrayList",
                        "value": dataJn["Object.Center"]
                    }
                }
            }
        }
        # print(str(payload))
        return payload