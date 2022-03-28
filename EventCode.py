import enum
from decodifier import CrossLineDetectionEventDecoded, CrossRegionDetectionEventDecoded, MotionEventDecoded, TakenAwayDetectionEventDecoded


class EventCode(enum.Enum):

    VideoMotion = MotionEventDecoded()
    TakenAwayDetection = TakenAwayDetectionEventDecoded()
    CrossRegionDetection = CrossRegionDetectionEventDecoded() 
    CrossLineDetection = CrossLineDetectionEventDecoded()
    
