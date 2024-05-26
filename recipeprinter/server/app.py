# Standard libary imports
import os
import re

# third party imports
from flask import Flask, render_template, request, session, redirect

# local imports
frojm recipeprinter.database import MyMongo

app = Flask(__name__)

# ===================================
#             ENDPOINTS
# ===================================


@app.route("/api/test")
def test():
    return MyMongo().TestConnection()

@app.route("/api/get-recipes")
def api_get():
    with MyMongo() as mongo:
        response = mongo.GetAllRecipes()
    return response

@app.route("/api/recipe/<id>")
def api_recipe(id):
    with MyMongo() as mongo:
        response = mongo.GetRecipe(id)
    return response

@app.route("/api/create-sample-recipe")
def api_insertsample():
    with MyMongo() as mongo:
        response = mongo.CreateSampleRecipe()
    return response

@app.route("/api/create-recipe", methods=["post"])
def api_insert():
    with MyMongo() as mongo:
        data = request.get_json()
        response = mongo.CreateRecipe(data['task_list'])
    return response

@app.route("/api/update-recipe-tasks", methods=["post"])
def api_update_task():
    with MyMongo() as mongo:
        request_json = request.get_json()
        id = request_json['recipe_id']
        task_list = request_json['task_list']

        response = mongo.UpdateRecipe(id, task_list)
    return response