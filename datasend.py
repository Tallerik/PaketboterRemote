from joystick import JoyStick
import socket
import time

UDP_IP = "192.168.8.104"
UDP_PORT = 12000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
thumbstick = JoyStick ("A0")  
panstick = JoyStick("A1")

while True:
    valuex,valuey = thumbstick .read_normal()
    x, pan = panstick.read_normal()
    data = str(valuex)+";"+str(valuey)+";"+str(pan)
    data = bytes(data,"utf-8")
    sock.sendto(data, (UDP_IP, UDP_PORT))
    time.sleep(0.1)
