import socket
import subprocess

import time

from parameter import Parameter

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
currProcess = None
while True:
    data, addr = sock.recvfrom(1024)
    print "received message:", data
    if currProcess is not None:
        currProcess.kill()
        time.sleep(2)

    parameter = Parameter(data)
    print "memcached " + parameter.getParam()
    currProcess = subprocess.Popen("exec memcached " + parameter.getParam(),shell=True)
