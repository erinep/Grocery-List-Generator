# Grocery List Generator

Recipes API server.

## Setup Instructions

1. Set config variables in a .env file. It should contain the following parameters:
    ```
    DB_HOST="example-database-url"
    DB_NAME="example-database-name"
    DB_USER="example-database-user"
    DB_PASS="example-database-password"

    SESSION_KEY="super_secret_key_phrase"
    ```

2. create/activate a python virutal environment and install production dependencies

    ```ps1
    > python -m venv venv
    > venv/scripts/activate.ps1
    > pip install <production wsgi server> # such as waitress, or gunicorn
    ```

3. Install the app `python -m pip install .`


## Web server example

- launch dev server: `python -m flask --app recipeprinter run`
- launch production sever: `python -m waitress-server --host <IP address> recipeprinter:app`

## API Endpoints

### [Get] /api/get-recipes
    returns: { 
        "response": [List of recipe documents]
    }


### [Get] /api/recipe/<id>
    returns: { 
        "response": {
            "task_index": int,
            "task_list": [
                {task 1},
                {task 2},
                {task 3}
            ]
        }
    }

### [Get] /api/create-sample-recipe
    - adds sample recipe document to database. 

    returns: {
        "acknowledged": true | false,
        "recipe_id": int
    }

### [Post] /api/create-recipe
    - insert a new recipe obj into the database

    body: { 
        "task_list": [...]
    }

    returns: { 
        "acknowledged": true | false,
        "recipe_id": int
    }

### [Post] /api/update-recipe-tasks
    - overwrite recipe task_list

    body: { 
        "recipe_id" int
        "task_list": [...]
    }

    returns: { 
        "acknowledged": true | false,
        "recipe_id": int
    }