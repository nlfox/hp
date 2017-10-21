from peewee import *

db = SqliteDatabase('server.db')


class Person(Model):
    id = IntegerField()
    name = CharField()

    class Meta:
        database = db


person = Person.create(id=1, name="sss")
person.save()
