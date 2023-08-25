import flask
from flask import jsonify, request, render_template, redirect, url_for
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


@app.route('/')
def index():
    sheeps = Sheep.select()
    return render_template('landing_page.html', sheeps=sheeps)


@app.route('/sheep/<int:id>', methods=["GET"])
def get_sheep(id):
    try:
        sheep = Sheep.get_by_id(id)
        return render_template('sheep.html', sheep=sheep)
    except Sheep.DoesNotExist:
        return jsonify({"error": "Sheep not found"}), 404
    except Exception as e:
        error_message = str(e)
        return jsonify({"error": error_message}), 500


@app.route('/sheep/<int:id>', methods=['POST'])
# Rename to update_sheep, try to figure out how to use PUT
def edit_sheep(id):
    try:
        sheep = Sheep.get_by_id(id)
        updated_values = {
            'name': request.form['name'],
            'gender': request.form['gender'],
            'tag_number': request.form['tag_number'],
            'birth_date': request.form['birth_date'],
            'ewe_id': request.form['ewe_id'] if request.form['ewe_id'] else None,
            'ram_id': request.form['ram_id'] if request.form['ram_id'] else None,
        }
        for key, value in updated_values.items():
            setattr(sheep, key, value)
        sheep.save()
        return redirect(url_for('get_sheep', id=sheep.id))
    except Sheep.DoesNotExist:
        return jsonify({"error": "Sheep not found"}), 404
    except Exception as e:
        error_message = str(e)
        return jsonify({"error": error_message}), 500


@app.route('/sheep/<int:id>', methods=["DELETE"])
def delete_sheep(id):
    try:
        Sheep.delete_by_id(id)
        return jsonify({"message": "Sheep deleted successfully."})
    except Sheep.DoesNotExist:
        return jsonify({"error": "Sheep not found"}), 404
    except Exception as e:
        error_message = str(e)
        return jsonify({"error": error_message}), 500


@app.route('/sheep', methods=["POST"])
def create_sheep():
    try:
        sheep_data = request.get_json(force=True)
        if not sheep_data['name']:
            return jsonify({"error": "No sheep name provided."}), 400
        sheep = Sheep(**sheep_data)
        sheep.save()
        response_data = {"message": "Sheep created successfully.", "id": sheep.id}
        return jsonify(response_data)
    except Exception as e:
        error_message = str(e)
        response = jsonify({"error": error_message})
        response.status_code = 500
        return response
