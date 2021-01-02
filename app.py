"""Flask app for Cupcakes"""

from flask import Flask, json, request, render_template, redirect, flash, session, jsonify
from models import Cupcake, db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db.init_app(app)
connect_db(app)

################################################

@app.route('/')
def home_page():
    """Route for a homepage."""
    
    return render_template("home.html")

################################################

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
    """Route to create a new cupcake and add to the db."""  
    
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def edit_cupcake(id):
    """Route to update/edit cupcake information."""
    
    updated_cupcake = Cupcake.query.get_or_404(id)  ### This is a flask method
    
    updated_cupcake.flavor = request.json.get("flavor", updated_cupcake.flavor)
    updated_cupcake.size = request.json.get("size", updated_cupcake.size)
    updated_cupcake.rating = request.json.get("rating", updated_cupcake.rating)
    updated_cupcake.image = request.json.get("image", updated_cupcake.image)
    
    db.session.commit()
    return jsonify(cupcake=updated_cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Route to delete a specific cupcake by id."""
    
    cupcake = Cupcake.query.get_or_404(id)
    
    db.session.delete(cupcake)
    db.session.commit()
    
    return jsonify(message="Deleted")