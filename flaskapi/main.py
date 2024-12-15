from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import json
import os
load_dotenv()  
username = os.getenv("POSTGRES_USERNAME")
password = os.getenv("POSTGRES_PASSWORD")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@localhost:5432/app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=True)

with app.app_context():
    db.create_all()

@app.route("/add-app", methods=['POST'])
def index():
    data = request.json
    try:
        app_name = data['app_name']
        version = data['version']
        description = data.get('description', '')  # Optional field
        new_app = App(app_name=app_name, version=version, description=description)
        db.session.add(new_app) 
        db.session.commit()
        print(new_app)
        return jsonify({"message": "App added successfully!", "id": new_app.id}), 201
    
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {e.args[0]}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def get_all():
    app_entry = App.query.all()
    
    if app_entry:
        list_of_elements = []
        for entry in app_entry:
            obj = {"id": entry.id,
                "app_name": entry.app_name,
                    "version": entry.version,
                    "description": entry.description}
            list_of_elements.append(obj)
        return jsonify(list_of_elements), 200
    return jsonify({"error": "App not found."}), 404
    
@app.route("/get-app/<int:id>", methods=["GET"])
def get_app(id):
    app_entry = App.query.get(id)
    if app_entry:
        return jsonify({
            "id": app_entry.id,
            "app_name": app_entry.app_name,
            "version": app_entry.version,
            "description": app_entry.description
        }), 200
    return jsonify({"error": "App not found."}), 404
    
@app.route("/delete-app/<int:id>", methods=["DELETE", "GET"])
def delete_app(id):
    app_entry = App.query.get(id)
    if app_entry:
        db.session.delete(app_entry)
        db.session.commit()
        return jsonify({"message": "App deleted successfully!"}), 200
    return jsonify({"error": "App not found."}), 404


if __name__ == '__main__':  
   app.run()