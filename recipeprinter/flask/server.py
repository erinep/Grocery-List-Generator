# Standard libary imports
import os

# third party imports
from flask import Flask, render_template, request, session, redirect
from dotenv import load_dotenv

# local imports
from recipeprinter.database import Database

app = Flask(__name__, template_folder='./templates')

# Setup local environments variables
from dotenv import load_dotenv
load_dotenv()
db_config= {
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

@app.route("/recipes")
def recipes():

    with Database(db_config) as d:
        list = d.get_recipes_list()

    return render_template("recipes_page.html", recipes=list)

@app.route("/ingredients")
def ingredients():

    with Database(db_config) as d:
        i = d.get_ingredients(session.get('recipes'), session.get('qty'))
    return render_template("ingredients_page.html", recipes=session.get('recipes'), qty=session.get('qty'), ingredients=i)
    

@app.route("/set-i", methods=["POST"] )
def set_session_recipes():

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/x-www-form-urlencoded'):

        recipes = []

        for r in request.form:
            if r != 'qty':
                recipes.append(r)

        session['recipes'] = recipes
        session['qty'] = request.form['qty']

    else:
        data = 'invalid content-type'

    return redirect(app.url_for('ingredients'))
