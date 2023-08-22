from peewee import *

db = SqliteDatabase('sqlite.db')


class Sheep(Model):
    id = AutoField()
    name = CharField()
    birth_date = DateField()
    ewe = ForeignKeyField('self', null=True)
    ram = ForeignKeyField('self', null=True)
    gender = CharField(choices=["male", "female"])
    tag_number = CharField()

    class Meta:
        database = db  # Replace db with your database instance


# Not creating a BaseModel, not necessary for one table.
class Sheep(Model):
    id = AutoField()
    name = CharField()
    birth_date = DateField()
    ewe = ForeignKeyField('self', null=True)
    ram = ForeignKeyField('self', null=True)
    gender = CharField(choices=["male", "female"])
    tag_number = CharField()

    class Meta:
        database = db
