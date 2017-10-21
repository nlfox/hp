import subprocess
import time
import socket

from test_db import Log

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP


def send(message):
    sock.sendto(bytes(message, "utf-8"), (socket.gethostbyname("nsl017"), 5005))


def do(parameter):
    send(parameter)
    time.sleep(3)
    subprocess.call('treadmill_memcached -v 1 --hostname=nsl017 --port=11211 -output_file="/tmp/1.txt" --logtostderr=1')
    tmp_file = open("/tmp/1.txt").readlines()
    result = tmp_file[0]
    Log.create(parameter=parameter, result=result)


do({"t": "4"})
