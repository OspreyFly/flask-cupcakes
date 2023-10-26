from flask import Flask, render_template, redirect, flash, url_for, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretKEY"

connect_db(app)

@app.route('/')
def home():
    return render_template("cupcakes.html")

@app.route("/api/cupcakes")
def getAllCupcakes():
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    
    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:cupcake_id>")
def getOneCupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes", methods=["POST"])
def createCupcake():
    data = request.get_json()
    flavor = data.get('flavor')
    size = data.get('size')
    rating = data.get('rating')
    image = data.get('image')

    if not flavor or not size or rating is None:
        return jsonify(error="Missing data"), 400  

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    
    response = jsonify(new_cupcake.serialize())
    response.headers['Content-Type'] = 'application/json'

    return response, 201 

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def updateCupcake(cupcake_id):
    data = request.get_json()
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    for key, value in data.items():
        setattr(cupcake, key, value)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def deleteCupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Cupcake deleted")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)