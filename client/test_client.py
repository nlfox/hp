import subprocess
import time
import socket
import datetime
from test_db import Log

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP


def send(message):
    sock.sendto(bytes(message), (socket.gethostbyname("nsl017"), 5005))


def do(parameter):
    send(parameter)
    time.sleep(3)
    time_stamp = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    subprocess.call('treadmill_memcached -v 1 --hostname=nsl017 --port=11211 -output_file="/tmp/'+time_stamp+'.txt" --logtostderr=1',shell=True)
    tmp_file = open("/tmp/"+time_stamp+".txt").readlines()
    result = tmp_file[0]
    Log.create(parameter=parameter, result=result)
for j in xrange(1,5):
    for i in xrange(1,10):
        do('{"t": "'+str(i)+'"}')
