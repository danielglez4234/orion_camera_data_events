from Event import *


class EventDecoder():
    def decode(self, message):
        raise NotImplementedError()


class MotionEventDecoded(EventDecoder):
    def decode(self, message):
        # Decodificar el mensaje
        return VideoMotion(message)


class CrossRegionDetectionEventDecoded(EventDecoder):
    def decode(self, message):
        # Decodificar el mensaje
        return CrossRegionDetection(message)


class CrossLineDetectionEventDecoded(EventDecoder):
    def decode(self, message):
        # Decodificar el mensaje
        return CrossLineDetection(message)


class TakenAwayDetectionEventDecoded(EventDecoder):
    def decode(self, message):
        # Decodificar el mensaje
        return TakenAwayDetection(message)
    
