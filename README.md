# Grocery List Generator

Recipes Reast API server.

## Setup Instructions

1. Set config variables in a .env file. It should contain the following parameters:
    ```
    DB_HOST="example-database-url"
    DB_NAME="example-database-name"
    DB_USER="example-database-user"
    DB_PASS="example-database-password"

    SESSION_KEY="super_secret_key_phrase"
    ```

2. run the create_tables.sql script to populate your postgress server
3. create/activate a python virutal environment and install production dependencies

    ```ps1
    > python -m venv venv
    > venv/scripts/activate.ps1
    > pip install <production wsgi server> # such as waitress, or gunicorn
    ```

4. Install the app `python -m pip install .`


## Web server example

- launch dev server: `python -m flask --app recipeprinter run`
- launch production sever: `python -m waitress-server --host <IP address> recipeprinter:app`

## API Endpoints

### [Get] /api/sampleinsert
    - adds sample task list to database. 
    - returns {insert_status: true | false}

### [Get] /api/getdata
    - returns { "response": [...]}


### [Post] /api/insertlist
    - insert a new task list into the database
    - body: {
        "task_list": [...]
    }
    - returns {insert_status: true | false}