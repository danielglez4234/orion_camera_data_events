import pycurl
import yaml

from EventCode import EventCode
from orionContextBroker import orionContextBroker



connected = False
USERNAME = "admin"
PASSWORD = "1IoTIC21"


def yaml_loader():
    with open("event_parameters.yaml", 'r') as file_descriptor:
        data = yaml.safe_load(file_descriptor)
    return data

yamlparams = yaml_loader()


def event_identifier(message):
    try: 
        eventDecoder = EventCode[message["type"]]
    except KeyError:
        print("Exeption: ", str(message["type"]), " is not registered")
    else: 
        event = eventDecoder.value.decode(message)
        id = yamlparams["entitie"]["id"]
        type = yamlparams["entitie"]["type"]
        orionContextBroker(event.toOrionEntitie(id, type))
        

def get_event_type(event):
    # print(str(event))
    begin = event.find("=")
    end = event.find(";")
    return event[begin+1:end]


def get_event_action(event):
    begin = event.find("action=")
    end = event.find(";index")
    return event[begin+7:end]


def get_event_data(event):
    begin = event.find("data=")
    last = event.__len__()
    return event[begin+5:last]


def on_receive(data):
    d = data.decode()
    for line in d.split("\r\n"):
        if "HTTP/1.1 200 OK" == line:
            global connected
            connected = True
        elif line.startswith("Code=") and "data=" in line:
            info = {
               "type": get_event_type(line),
               "action": get_event_action(line),
               "data": get_event_data(line)
            }
            event_identifier(info)


def start():  
    url = "http://%s:%s@161.72.123.249/cgi-bin/eventManager.cgi?action=attach&codes=[All]&heartbeat=5." % (USERNAME, PASSWORD)
    # url = yamlparams.camera.url
    
    try:
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.CONNECTTIMEOUT, 10)
        c.setopt(pycurl.TCP_KEEPALIVE, 1)
        c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_DIGEST)
        # Message receiver function
        c.setopt(pycurl.WRITEFUNCTION, on_receive)
        # perform
        c.perform()
        # close connection
        c.close()
    except pycurl.error as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    USERNAME = "admin"
    PASSWORD = "1IoTIC21"

    start()
