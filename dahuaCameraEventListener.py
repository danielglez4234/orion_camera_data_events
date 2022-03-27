import pycurl
import argparse
import yaml

from CrossLineDetection import CrossLineDetection
from CrossRegionDetection import CrossRegionDetection
from TakenAwayDetection import TakenAwayDetection
from VideoMotion import VideoMotion


connected = False
USERNAME = "admin"
PASSWORD = "1IoTIC21"


"""yaml declaration"""

def yaml_loader():
    with open("event_parameters.yaml", 'r') as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

yamlparams = yaml_loader()

"""----------"""


def event_identifier(info):
    if info["type"] == "VideoMotion":
        VideoMotion(info)
    elif info["type"] == "CrossRegionDetection":
        CrossRegionDetection(info)
    elif info["type"] == "CrossLineDetection":
        CrossLineDetection(info)
    elif info["type"] == "TakenAwayDetection":
        TakenAwayDetection(info)
    

def get_event_type(event):
    print(str(event))
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
            event_type = get_event_type(line)
            # print("type --> ", str(event_type))

            event_action = get_event_action(line)
            # print("action --> ", str(event_action))

            event_data = get_event_data(line)
            # print("data --> ", str(event_data))

            info = {
               "type": event_type,
               "action": event_action,
               "data": event_data
            }
            event_identifier(info)


def start():  
    # url = "http://%s:%s@161.72.123.249/cgi-bin/eventManager.cgi?action=attach&codes=[All]&heartbeat=5." % (USERNAME, PASSWORD)
    url = yamlparams.camera.url
    
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
