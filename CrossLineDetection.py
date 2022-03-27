import json


class CrossLineDetection:
    def __init__(self, info):
        self.data = info["data"]

        datatojson = json.loads(self.data)
        # print(" ------- soy un CrossLineDetection -----------   ")

