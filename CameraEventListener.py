from __future__ import annotations

import threading

import pycurl
import yaml

from EventCode import EventCode
from EventDecoder import EventDecoder
from OrionContextBroker import OrionContextBroker

connected = False
USERNAME = "admin"
PASSWORD = "1IoTIC21"


class EventListener(threading.Thread):
    def __init__(self, camera):
        super().__init__()
        self.connection = None
        self.camera = camera


    def start(self) -> None:
        self.open_connection()
        super().start()

    def run(self) -> None:
        try:
            self.connection.perform()
        except pycurl.error:
            print("Error while trying to connect to %s" % self.camera['host'])

    def join(self, timeout: float | None = ...) -> None:
        super().join(timeout)

    def open_connection(self):
        self.connection = pycurl.Curl()
        url = "http://%s:%s@%s/cgi-bin/eventManager.cgi?action=attach&codes=[All]&heartbeat=5." % (
            self.camera['user'], self.camera['password'], self.camera['host'])

        print("Connecting to %s" % url)

        try:
            self.connection.setopt(pycurl.URL, url)
            self.connection.setopt(pycurl.CONNECTTIMEOUT, 10)
            self.connection.setopt(pycurl.TCP_KEEPALIVE, 1)
            self.connection.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_DIGEST)
            # Message receiver function
            self.connection.setopt(pycurl.WRITEFUNCTION, self.on_event)
        except pycurl.error as e:
            print(e)
        except Exception as e:
            print(e)

    def on_event(self, event):
        d = event.decode()
        for line in d.split("\r\n"):
            if "HTTP/1.1 200 OK" == line:
                global connected
                connected = True
            elif line.startswith("Code=") and "data=" in line:
                code = EventDecoder.get_code(d)
            
                # if code in EventCode:
                    # event_model = EventCode[code].value.decode(EventDecoder.get_data(d))
                    # OrionContextBroker.get_instance().update_entity(self.camera.id, event_model.to_orion_attribute())
                
                if code in self.camera["events"]:
                    if code in EventCode._member_names_:
                        event_model = EventCode[code].value.to_orion_attribute(d)                                          
                        OrionContextBroker.get_instance().update_entity(self.camera["id"], event_model)
                    else: 
                        print("Event not supported!")