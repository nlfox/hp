import subprocess
import time
import socket
import datetime
from test_db import Log
from parameter import Parameter

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP


def send(message):
    sock.sendto(bytes(message), (socket.gethostbyname("nsl017"), 5005))


def do(client_parameter, server_parameter, tag="test", server_program="memcached"):
    client_parameter = Parameter(client_parameter)
    client_parameter.setName("treadmill")
    server_parameter = Parameter(server_parameter)
    client_parameter.addParam("logtostderr", 1)
    client_parameter.addParam("number_of_workers", 4)
    server_parameter.setName(server_program)
    send(server_parameter.toJson())
    time.sleep(3)
    time_stamp = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    print client_parameter.getParamCli()
    subprocess.call(
        'treadmill_memcached -v 1 --hostname=nsl017 --port=11211 -output_file="/tmp/' + time_stamp + '.txt" ' +
        client_parameter.getParamCli(),
        shell=True)
    tmp_file = open("/tmp/" + time_stamp + ".txt").readlines()
    result = tmp_file[0]
    Log.create(client_parameter=client_parameter.toJson(), server_parameter=server_parameter.toJson(), result=result,
               tag=tag)


confstr = """'{"pools":{"A":{"servers":["127.0.0.1:5001"]}},"route":"PoolRoute|A"}'"""

for j in xrange(5):
    for i in range(100000, 800000, 25000):
        do({"request_per_second": i}, {"p": 5000, "-config-str": confstr}, "multiprocess", "mcrouter")
