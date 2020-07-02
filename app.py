from flask import Flask, request, jsonify, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, Family

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = "development"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"

db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)
CORS(app)

family = Family("Jackson")

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/members', methods=['GET'])
def all_members():
    return jsonify(family.get_all_members()), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def one_member(member_id):
    if member_id:
        return jsonify(family.get_member(member_id)), 200
    else:
        return jsonify({"msg": "Error en id"}), 400

@app.route('/member', methods=['POST'])
def add_member():
    # new_member datos son extraidos desde el body
    #new_member = request.get_json()
    id = family._generateId()
    new_member = {"first_name":"Otro familiar", "age": 2, "lucky_numbers": [1,2],  "id": f"{id}"}
    family.add_member(new_member)
    return jsonify({"msg" : f"Familiar con id {id} agregado correctamente"}), 200

@app.route('/member/<int:member_id>', methods=['PUT'])
def up_member(member_id):
    if member_id:
        
        data = request.get_json()
        if data["first_name"] == None or data["first_name"] == "":
            return jsonify({"msg" : "Debe ingresar nombre"})
        if data["age"] == None or type(data["age"]) is not int:
            return jsonify({"msg" : "Debe ingresar una edad"})
        if data["last_name"] == None or data["last_name"] == "":
            return jsonify({"msg" : "Debe ingresar apellido"})
        if data["lucky_numbers"] == None or len(data["lucky_numbers"]) == 0:
            return jsonify({"msg" : "Debe ingresar lucky numbers"})   
        
        update = {
            "age" : data["age"],
            "first_name" : data["first_name"],
            "last_name": data["last_name"],
            "lucky_numbers": data["lucky_numbers"]
        }

        family.update_member(member_id, update)
        return jsonify({"Actualización" : f"{update}"}), 200
    else:
        return jsonify({"msg": "Error en id"}), 400

@app.route('/member/<int:member_id>', methods=['DELETE'])
def del_member(member_id):
    if member_id:
        family.delete_member(member_id)
        return jsonify({"msg" : "Familiar borrado"}), 200
    else:
        return jsonify({"msg": "Error en id"}), 400

if __name__ == '__main__':
    manager.run()