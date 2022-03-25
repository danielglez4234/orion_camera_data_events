import json


class CrossRegionDetection:
    def __init__(self, info):
        self.data = info["data"]

        datatojson = json.loads(self.data)
        print(" ------- soy un CrossRegionDetection -----------   ")

