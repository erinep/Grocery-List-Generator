import recipeprinter.cli as cli

if __name__ == '__main__':

    db_config = {
    "host":"localhost",
    "dbname":"postgres",
    "user":"test_user",
    "password":"password"}

    cli.run(db_config)