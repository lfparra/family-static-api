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
def one_member(member_id=None):
    return jsonify({"msg" : "Prueba de mensaje GET"}), 200
    
@app.route('/member', methods=['POST'])
def add_member():
    pass 

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member():
    pass

if __name__ == '__main__':
    manager.run()