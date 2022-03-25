import json


class VideoMotion:
    def __init__(self, info):
        self.data = info["data"]
        self.action = info["action"]

        datatojson = json.loads(self.data)
        # print(" ------- soy un VideoMotion -----------")

