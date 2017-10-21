import socket
import subprocess
from parameter import Parameter

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
currProcess = None
while True:
    data, addr = sock.recvfrom(1024)
    print "received message:", data
    if currProcess is not None:
        currProcess.kill()

    parameter = Parameter(data)
    currProcess = subprocess.Popen("memcached " + parameter.getParam(), shell=True)
