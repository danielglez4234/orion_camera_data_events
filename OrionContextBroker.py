import json
import requests
# from configparser import ConfigParser


HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "fiware-service": "gtc",
    "fiware-servicePath": "/"
}

OCB = None

HOSTNAME = "localhost"
PORT = "1026"


class OrionContextBroker:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    # def create_entity(self, entity):
    #     # r = requests.patch("http://%s:%s/v2/entities/" % (self.host, self.port), data=entity, headers=HEADERS)
    #     pass


    def update_entity(self, id, attribute):
        # print("id: ", id, "attr: ", attribute)

        r = requests.post("http://%s:%s/v2/entities/%s/attrs" % (self.host, self.port, id), data=json.dumps(attribute), headers=HEADERS)

        if r.status_code != 204 and r.status_code != 200:
            print('%s -FAIL %d' % (id, r.status_code))
        else:
            print('%s -UPDATED %d' % (id, r.status_code))


    @staticmethod
    def get_instance():
        global OCB
        if OCB is None:
            OCB = OrionContextBroker(HOSTNAME, PORT)
        return OCB