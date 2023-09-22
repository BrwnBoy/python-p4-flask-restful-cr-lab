#!/usr/bin/env python3

from flask import Flask, request, jsonify
from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # adjust this if necessary
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/plants', methods=['GET', 'POST'])
def handle_plants():
    if request.method == 'POST':
        new_plant = Plant(
            name=request.json.get('name'),
            image=request.json.get('image'),
            price=request.json.get('price')
        )
        db.session.add(new_plant)
        db.session.commit()

        return jsonify(new_plant.to_dict()), 201

    else:
        plants = Plant.query.all()
        return jsonify([plant.to_dict() for plant in plants]), 200

@app.route('/plants/<int:id>', methods=['GET'])
def handle_plant(id):
    plant = Plant.query.get(id)
    return jsonify(plant.to_dict()), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
