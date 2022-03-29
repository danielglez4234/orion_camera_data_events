import json
from time import time


class EventDecoder:
    @staticmethod
    def get_code(event):
        begin = event.find("=")
        end = event.find(";")
        return event[begin + 1:end]

    @staticmethod
    def get_action(event):
        begin = event.find("action=")
        end = event.find(";index")
        return event[begin + 7:end]

    @staticmethod
    def get_data(event):
        begin = event.find("data=")
        last = event.__len__()
        return event[begin + 5:last]

    def to_orion_attribute(self, message):
        raise NotImplementedError()


class MotionEventDecoded(EventDecoder):
    def to_orion_attribute(self, message):
        dataJn = json.loads(message)
        payload = {
            "id": id + "_VM",
            "type": type,
            "Event_name": "VideoMotion",
            "State": {
                "type": "String",
                "value": self.get_action(message)
            },
            "RegionName": {
                "type": "ArrayList",
                "value": dataJn["RegionName"]
            }
        }
        # print(str(payload))
        return payload


# ESTE ES EL EJEMPLO BUENO
# Ya no es necesario el id y el type
class CrossRegionDetectionEventDecoded(EventDecoder):
    def to_orion_attribute(self, message):
        dataJn = json.loads(message)
        payload = {
            "crossRegionEvent": {
                "type": "Event",
                "value": {
                    "action": self.get_action(message),
                    "boundingBox": dataJn["DetectRegion"],
                    "type": dataJn["Object"]["Action"],
                    "date": time()
                }
            }
        }
        # print(str(payload))
        return payload


class CrossLineDetectionEventDecoded(EventDecoder):
    def to_orion_attribute(self, message):
        self.id = id
        self.type = type
        dataJn = json.loads(message)
        payload = {
            "id": self.id + "_CL",
            "type": self.type,
            "Event_name": "CrossLineDetection",
            "State": {
                "type": "String",
                "value": self.get_action(message)
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
                    "value": dataJn["Object"]["Action"]
                },
                "ObjectType": {
                    "type": "String",
                    "value": dataJn["Object"]["ObjectType"]
                },
                "Speed": {
                    "type": "String",
                    "value": dataJn["Object"]["Speed"]
                },
                "SpeedTypeInternal": {
                    "type": "String",
                    "value": dataJn["Object"]["SpeedTypeInternal"]
                },
                "FrameLocation": {
                    "type": "Object",
                    "BoundingBox": {
                        "type": "ArrayList",
                        "value": dataJn["Object"]["BoundingBox"]
                    },
                    "Center": {
                        "type": "ArrayList",
                        "value": dataJn["Object"]["Center"]
                    }
                }
            }
        }
        # print(str(payload))
        return payload


class TakenAwayDetectionEventDecoded(EventDecoder):
    def to_orion_attribute(self, message):
        # Decodificar el mensaje
        self.id = id
        self.type = type
        dataJn = json.loads(message)
        payload = {
            "id": self.id + "_TAD",
            "type": self.type,
            "Event_name": "TakenAwayDetection",
            "State": {
                "type": "String",
                "value": self.get_action(message)
            },
            "ObjectDetected": {
                "type": "Object",
                "Action": {
                    "type": "String",
                    "value": dataJn["Object"]["Action"]
                },
                "ObjectType": {
                    "type": "String",
                    "value": dataJn["Object"]["ObjectType"]
                },
                "FrameLocation": {
                    "type": "Object",
                    "BoundingBox": {
                        "type": "ArrayList",
                        "value": dataJn["Object"]["BoundingBox"]
                    },
                    "Center": {
                        "type": "ArrayList",
                        "value": dataJn["Object"]["Center"]
                    }
                }
            }
        }
        # print(str(payload))
        return payload
    
