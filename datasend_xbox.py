from xboxcontroller import XboxController
import socket
import time

UDP_IP = "192.168.8.104"
UDP_PORT = 12000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

xbox = XboxController()

while True:
    x, y, x2, y2, a, b, btx, bty, rb, lb, tr, tl = xbox.read()
    speed = tr - tl
    data = str(speed)+";"+str(x)+";"+str(x2)
    print(data)
    data = bytes(data,"utf-8")
    sock.sendto(data, (UDP_IP, UDP_PORT))
    time.sleep(0.1)
