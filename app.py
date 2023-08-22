import flask
from flask import jsonify, request
from peewee import AutoField, CharField, DateField, SqliteDatabase, Model, ForeignKeyField

app = flask.Flask(__name__)

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


@app.route('/sheep', methods=["POST"])
def create_sheep():
    try:
        sheep_data = request.get_json(force=True)
        sheep = Sheep(**sheep_data)
        sheep.save()
        return "Sheep created successfully."
    except Exception as e:
        error_message = str(e)
        response = jsonify({"error": error_message})
        response.status_code = 500  # Set the HTTP status code to 500 (Internal Server Error)
        return response


@app.route('/sheep/<int:id>', methods=["PUT"])
def update_sheep(id):
    try:
        update_data = sheep_data = request.get_json(force=True)
        update_query = Sheep.update(update_data).where(Sheep.id == id)
        print(update_query.sql())
        update_query.execute()
        return jsonify(sheep_data)
    except Sheep.DoesNotExist:
        return jsonify({"error": "Sheep not found"}), 404
    except Exception as e:
        error_message = str(e)
        return jsonify({"error": error_message}), 500
