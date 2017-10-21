import datetime
from peewee import *

db = SqliteDatabase('server.db')


class Log(Model):
    parameter = TextField()
    time = DateTimeField(default=datetime.datetime.now)
    result = TextField()

    class Meta:
        database = db


