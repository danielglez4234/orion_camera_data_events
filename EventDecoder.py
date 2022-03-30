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
        action = self.get_action(message)
        dataJn = json.loads(self.get_data(message))
        payload = {
            "MotionEvent": {
                "type": "Event",
                "value": {
                    "action": action,
                    "RegionName": dataJn["RegionName"],
                    "timestamp": time()
                }
            }
        }
        return payload


# ESTE ES EL EJEMPLO BUENO
# Ya no es necesario el id y el type
class CrossRegionDetectionEventDecoded(EventDecoder):
    def to_orion_attribute(self, message):
        action = self.get_action(message)
        dataJn = json.loads(self.get_data(message))
        payload = {
            "crossRegionEvent": {
                "type": "Event",
                "value": {
                    "action": action,
                    "boundingBox": dataJn["Object"]["BoundingBox"],
                    "type": dataJn["Object"]["ObjectType"],
                    "timestamp": time()
                }
            }
        }
        return payload


class CrossLineDetectionEventDecoded(EventDecoder):
    def to_orion_attribute(self, message):
        action = self.get_action(message)
        dataJn = json.loads(self.get_data(message))
        payload = {
            "CrossLineEvent": {
                "type": "Event",
                "value": {
                    "action": action,
                    "boundingBox":  dataJn["Object"]["BoundingBox"],
                    "DetectLine": dataJn["DetectLine"],
                    "Direction": dataJn["Direction"],
                    "type": dataJn["Object"]["ObjectType"],
                    "timestamp": time()
                }
            }
        }
        return payload


class TakenAwayDetectionEventDecoded(EventDecoder):
    def to_orion_attribute(self, message):
        action = self.get_action(message)
        dataJn = json.loads(self.get_data(message))
        payload = {
            "TakenAwayEvent": {
                "type": "Event",
                "value": {
                    "action": action,
                    "boundingBox": dataJn["Object"]["BoundingBox"],
                    "objectAction": dataJn["Object"]["Action"],
                    "type": dataJn["Object"]["ObjectType"],
                    "timestamp": time()
                }
            }
        }
        return payload
    
