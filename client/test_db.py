import datetime
from peewee import *
import json
db = SqliteDatabase('/Users/nlfox/server.db')


class Log(Model):
    server_parameter = TextField()
    client_parameter = TextField()
    time = DateTimeField(default=datetime.datetime.now)
    result = TextField()
    tag = TextField()

    class Meta:
        database = db


for log in Log.select():
    print log.parameter,
    res = json.loads(log.result)
    print res["request_latency"]["average"], res["request_latency"]["p99"]

