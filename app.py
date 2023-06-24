"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request
from models import db, connect_db, Cupcake
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:{os.environ.get('DB_PASSWORD')}@localhost/cupcakes"
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)

# API routes


@app.route("/api/cupcakes")
def get_cupcakes():
    """Get data about all cupcakes"""

    cupcakes = Cupcake.query.all()

    serialized_cupcakes = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized_cupcakes)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Get data about a single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create a cupcake"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json.get("image", None)

    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(cupcake)
    db.session.commit()

    serialized_cupcake = cupcake.serialize()

    return (jsonify(cupcake=serialized_cupcake), 201)
