import pycurl
import yaml

import OrionContextBroker
from CameraEventListener import EventListener


def get_config(path):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
    return data


def init():
    config = get_config("config.yaml")['dahua']

    OrionContextBroker.HOSTNAME = config['orion']['host']
    OrionContextBroker.PORT = config['orion']['port']

    listeners = []
    cameras = config['cameras']

    for camera_id in cameras:
        camera = cameras[camera_id]
        camera['id'] = camera_id

        listener = EventListener(camera)
        listener.start()

        listeners.append(listener)


if __name__ == '__main__':
    USERNAME = "admin"
    PASSWORD = "1IoTIC21"

    init()