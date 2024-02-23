# standard libary imports
import os

# third party imports
from dotenv import load_dotenv

# local imports
import recipeprinter.cli as cli

if __name__ == '__main__':

    load_dotenv()
    db_config = {
    "host": os.getenv("DB_HOST"),
    "dbname":os.getenv("DB_NAME"),
    "user":os.getenv("DB_USER"),
    "password":os.getenv("DB_PASS")}

    cli.run(db_config)