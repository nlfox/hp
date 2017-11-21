import datetime
from peewee import *
import json
db = SqliteDatabase('server.db')


class Log(Model):
    server_parameter = TextField()
    client_parameter = TextField()
    time = DateTimeField(default=datetime.datetime.now)
    result = TextField()

    class Meta:
        database = db

