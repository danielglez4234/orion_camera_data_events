import json
import requests
from configparser import ConfigParser


OCB = None

config = ConfigParser()
config.read('config.ini')

HOSTNAME = config['ORION_CONECCTION']['host']
PORT = config['ORION_CONECCTION']['port']
FIWARE_SERVICE = config['ORION_CONECCTION']['fiware_service']
FIWARE_SERVICE_PATH = config['ORION_CONECCTION']['fiware_service_path']


class OrionContextBroker:
    def __init__(self, host, port, fiware_service, fiware_service_path):
        self.host = host
        self.port = port
        self.service = fiware_service
        self.service_path = fiware_service_path
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "fiware-service": self.service ,
            "fiware-servicePath": self.service_path
        }
        
        
    # def create_entity(self, entity):
    #     entitie_model = {
    #         "id": entity["id"], 
    #         "type": "Event"
    #     }
    #     # r = requests.post("http://%s:%s/v2/entities/" % (self.host, self.port), data=entity, headers=HEADERS)
    #     pass


    def update_entity(self, id, attribute):
        r = requests.post("http://%s:%s/v2/entities/%s/attrs" % (self.host, self.port, id), data=json.dumps(attribute), headers=self.headers)

        if r.status_code != 204 and r.status_code != 200:
            print('%s -FAIL %d' % (id, r.status_code))
        else:
            print('%s -UPDATED %d' % (id, r.status_code))


    @staticmethod
    def get_instance():
        global OCB
        if OCB is None:
            OCB = OrionContextBroker(HOSTNAME, PORT, FIWARE_SERVICE, FIWARE_SERVICE_PATH)
        return OCB