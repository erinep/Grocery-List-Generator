# Standard libary imports
import os
import re

# third party imports
from flask import Flask, request, session, redirect, jsonify

# local imports
from recipeprinter.database import MyMongo

app = Flask(__name__)
db = MyMongo()

# ===================================
#             ENDPOINTS
# ===================================


@app.route("/api/test")
def test():
    return db.TestConnection()

@app.route("/api/recipes")
def api_list_recipes():
    return db.GetRecipeList()

@app.route("/api/delete/recipe", methods=["POST"])
def api_delete_recipe():
    if 'id' in request.json:
        return db.DeleteRecipe(request.json['id'])
    else:
        return {
            "error": "missing 'id' parameter"
        }, 400

@app.route("/api/recipe/<id>")
def api_recipe(id):
    return db.GetRecipe(id)

@app.route("/api/create-sample-recipe")
def api_insertsample():
    return db.CreateSampleRecipe()

@app.route("/api/create-recipe", methods=["post"])
def api_insert():
    data = request.get_json()
    response = db.CreateRecipe(data['task_list'])
    return response

@app.route("/api/update-recipe-tasks", methods=["post"])
def api_update_task():
    request_json = request.get_json()
    if ('recipe_id' in request_json) and ('task_list' in request_json):
        id = request_json['recipe_id']
        task_list = request_json['task_list']

    else:
        return {"error": "missing parameters"}

    recipe = db.GetRecipe(id)
    response = db.SetTaskList(recipe['task_id'], task_list)

    return response