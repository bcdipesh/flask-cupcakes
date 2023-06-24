"""Flask app for Cupcakes"""

from flask import Flask
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
