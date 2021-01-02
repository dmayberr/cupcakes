"""Flask app for Cupcakes"""

from flask import Flask, json, request, render_template, redirect, flash, session, jsonify
from models import Cupcake, db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db.init_app(app)
connect_db(app)

@app.route('/api/cupcakes')
def get_all_cupcakes():
    """Route to get all the cupcakes."""
    
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_a_cupcake(id):
    """Route to display a cupcake based on the id."""
    
    cupcake = Cupcake.query.get_or_404(id)      
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def create_new_cupcake():
    
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)