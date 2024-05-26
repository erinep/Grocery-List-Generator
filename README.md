# Grocery List Generator

Recipes API server.

## Docker setup

`Docker build -t "IMAGE_NAME"`

`Docker run -p 5000:5000 IAMGE_NAME`


## local server setup

- python env: `python -m venv venv; source venv/bin/activate`
- install dependencies: `pip install -r requirements.txt`
- launch dev server: `python -m flask --debug --app recipeprinter:app run`

## API Endpoints

### [Get] /api/test
    returns: {
        "db_connected": True | False
    }

### [Get] /api/recipes
    returns: {
        "response": list of recipe _IDs
    }


### [Get] /api/recipes-full
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
