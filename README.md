# Grocery List Generator

Recipes API server.

## Docker setup

`Docker build -t "IMAGE_NAME"`

`Docker run -p 5000:5000 IAMGE_NAME`


## local server setup

- python env: `python -m venv venv; source venv/bin/activate`
- install dependencies: `pip install -r requirements.txt`
- launch dev server: `python -m flask --debug --app recipeprinter:app run`

## Database Schema

Recipes: {
    _id: ObjectId
    name: str
    task_id: ObjectId
}

Tasks: {
    _id: ObjectId,
    task_list: [
        {type: str, content:str }
    ]
}

## API Endpoints

### [Get] /api/test
    returns: {
        "db_connected": bool
    }

### [Get] /api/recipes
    returns: {
        "response": [
            {"name": str, "_id": str},
            {"name": str, "_id": str},
        ]
    }

### [Get] /api/recipe/<id>
    returns: { 
        "response": {
            "recipe_id": str
            "recipe_name": str,
            "task_list": [
                {task 1},
                {task 2},
                {task 3}
            ]
        }
    }

### [Get] /api/create-sample-recipe
    - adds sample recipe document to database. 

    return {
        "recipe_created": bool,
        "tasks_created": bool,
        "tasks_id": int,
        "recipe_id": int
    }

### [Post] /api/delete/recipe
    - deletes a recipe
    body: {
        "recipe_id": int
    }
    return 200 OK {
        "recipe_deleted": bool,
        "tasks_deleted": bool,
        "recipes_deleted_count": int,
        "tasks_deleted_count": int,
    }
    return 400 {
        "error": str
    }


### [Post] /api/create-recipe
    - insert a new recipe obj into the database

    body: { 
        "task_list": [...]
    }

    return { 
        "recipe_created": bool,
        "tasks_created": bool,
        "tasks_id": int,
        "recipe_id": int
    }

### [Post] /api/update-recipe-tasks
    - overwrite recipe task_list

    body: { 
        "recipe_id" int
        "task_list": [...]
    }

    return { 
        "task_updated": bool,
    }
