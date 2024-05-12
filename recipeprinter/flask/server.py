# Standard libary imports
import os
import re

# third party imports
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from dotenv import load_dotenv

# local imports
from recipeprinter.database import Database, MyMongo

app = Flask(__name__, template_folder='./templates')
CORS(app, origins=["http://localhost:5173"])

# Setup local environments variables
from dotenv import load_dotenv
load_dotenv()
db_config= {
    "mongo_host": "localhost:27017",
    "mongo_db_name": "testDB",
    "host": os.getenv("DB_HOST"),
    "dbname":os.getenv("DB_NAME"),
    "user":os.getenv("DB_USER"),
    "password":os.getenv("DB_PASS")
}
app.secret_key = os.getenv("SESSION_KEY")

# ===================================
#             ENDPOINTS
# ===================================

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/api/sampleinsert")
def api_insertsample():
    with MyMongo(db_config) as mongo:
        response = mongo.insertfakedata()
    return response

@app.route("/api/getdata")
def api_get():
    with MyMongo(db_config) as mongo:
        response = mongo.getdata()
    return response

@app.route("/api/insertlist", methods=["post"])
def api_insert():
    with MyMongo(db_config) as mongo:
        data = request.get_json()
        response = mongo.insertlist(data['task_list'])
    return response