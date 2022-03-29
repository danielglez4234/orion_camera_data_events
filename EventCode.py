import enum
from EventDecoder import CrossLineDetectionEventDecoded, CrossRegionDetectionEventDecoded, MotionEventDecoded, \
    TakenAwayDetectionEventDecoded


class EventCode(enum.Enum):

    VideoMotion = MotionEventDecoded()
    TakenAwayDetection = TakenAwayDetectionEventDecoded()
    CrossRegionDetection = CrossRegionDetectionEventDecoded() 
    CrossLineDetection = CrossLineDetectionEventDecoded()
    
