from peewee import AutoField, CharField, DateField, SqliteDatabase, Model, ForeignKeyField

# TODO: load the environment variable path
db = SqliteDatabase('sqlite.db')


class Sheep(Model):
    id = AutoField()
    name = CharField()
    birth_date = DateField()
    ewe_id = ForeignKeyField('self', null=True)
    ram_id = ForeignKeyField('self', null=True)
    gender = CharField(choices=["male", "female"])
    tag_number = CharField()

    class Meta:
        database = db


db.connect()

db.create_tables([Sheep])
