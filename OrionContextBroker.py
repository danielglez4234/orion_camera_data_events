import requests
from configparser import ConfigParser

HEADERS = {
    "Accept": "application/json",
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
        # self.payload = payload
        # config = ConfigParser()
        # config.read('config.ini')
        #
        # host = config['ORION_CONECCTION']['host']
        # port = config['ORION_CONECCTION']['port']
        # print(url)

        # url_update = 'localhost:1026/v2/entities/'+self.payload["id"]+'/attrs?options=append'
        
        #
    def create_entity(self, entity):
        pass

    def update_entity(self, id, attribute):
        r = requests.get("http://%s:%s/v2/entities/%s/attrs" % (self.host, self.port, id), attribute, headers=HEADERS)
        print(r.text)

    @staticmethod
    def get_instance():
        global OCB
        if OCB is None:
            OCB = OrionContextBroker(HOSTNAME, PORT)
        return OCB

