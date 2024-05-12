# Standard libary imports
import os
import re

# third party imports
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from dotenv import load_dotenv

# local imports
from recipeprinter.database import Database

app = Flask(__name__, template_folder='./templates')
CORS(app, origins=["http://localhost:5173"])

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

@app.route("/api/sampletasks")
def test():
    return { 
        "task_list" : [
            {"task_type": 'text', "task_content": "1,2,3", "id": 0},
            {"task_type": 'text', "task_content": '4,5,6', "id": 1},
            {"task_type": "other", "task_content": "7, 8, 9", "id": 2}
        ],
        "task_index": 2
    }

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
@app.route("/recipe-details")
def show_recipe_details():
    return render_template("recipe_content_page.html")

@app.route("/add")
def create_recipe():

    with Database(db_config) as d:
        types = d.get_categories()
    return render_template("create_recipe_page.html", types=types)


@app.route("/set-active-recipes", methods=["POST"] )
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




@app.route("/parse-new-recipe", methods=["POST"])
def parse_new_recipe():

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/x-www-form-urlencoded'):

        r_name = request.form['recipe_name']


        # PARSE INGREDIENTS
        clean_ingredients = []
        recipe_contents = []
        for key in request.form:
            # parse the key using regex
            # key_type: remove all character up to and including the ':'    
            # key_uuid: remove all character including and after the ':'
            key_type = re.sub(r'[\w-]+:', '', key)
            key_uuid = re.sub(r':[\w]+', '', key)

            if(key_type == 'name'):
                i_type = request.form[f'{key_uuid}:type']
                i_name = request.form[f'{key_uuid}:name']
                clean_ingredients.append((i_name, i_type))
                
                i_unit = request.form[f'{key_uuid}:unit']
                i_2ppl = request.form[f'{key_uuid}:2ppl']
                i_4ppl = request.form[f'{key_uuid}:4ppl']
                recipe_contents.append((r_name, i_name, i_unit, i_2ppl, i_4ppl))

                
    else:
        return redirect(app.url_for('ingredients')) # TODO redirect to error page


    # ADD TO DATABASE
    with Database(db_config) as d:
        
        d.add_ingredients(clean_ingredients)
        d.add_recipe(r_name)
        d.add_ingredient_enties(recipe_contents)

    return redirect(app.url_for('recipes'))