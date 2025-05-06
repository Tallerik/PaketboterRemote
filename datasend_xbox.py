from xboxcontroller import XboxController
import socket
import time
from influx import Influx

UDP_IP = "192.168.8.104"
UDP_PORT = 12000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

xbox = XboxController()

infl = Influx(xbox=xbox)
infl.start()

while True:
    #x, y, x2, y2, a, b, btx, bty, rb, lb, tr, tl = xbox.read()
    cmd = ""
    if (xbox.A):
        cmd = "self_drive"
    
    speed = xbox.RightTrigger - xbox.LeftTrigger
    data = str(speed)+";"+str(xbox.LeftJoystickX)+";"+str(xbox.RightJoystickX)+";"+cmd

    #print(data)
    data = bytes(data,"utf-8")
    sock.sendto(data, (UDP_IP, UDP_PORT))
    time.sleep(0.1)
