import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv
from threading import Thread
from xboxcontroller import XboxController
from time import sleep
load_dotenv()




class Influx:

    def __init__(self, xbox: XboxController):
        token = os.getenv("INFLUXDB_TOKEN")
        self.org = os.getenv("INFLUXDB_ORG")
        url = os.getenv("INFLUXDB_URL")
        self.bucket = os.getenv("INFLUXDB_BUCKET")

        self.xbox = xbox

        self.client = InfluxDBClient(url=url, token=token, org=self.org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def start(self):
        self.thread = Thread(target=self.collect)
        self.thread.start()


    def collect(self):
        while True:
            p = Point("Remote")\
                .field("LeftJoystickX", float(self.xbox.LeftJoystickX))\
                .field("RightJoystickX", float(self.xbox.RightJoystickX))\
                .field("LeftTrigger", float(self.xbox.LeftTrigger))\
                .field("RightTrigger", float(self.xbox.RightTrigger))\
                .field("A", float(self.xbox.A))\
                .field("LeftJoystickX", float(self.xbox.LeftJoystickX))
        
            self.write_api.write(bucket=self.bucket, org=self.org, record=p)
            sleep(0.1)

