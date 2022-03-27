import json


class TakenAwayDetection:
    def __init__(self, info):
        self.data = info["data"]

        datatojson = json.loads(self.data)
        # print(" ------- soy un TakenAwayDetection -----------   ")

