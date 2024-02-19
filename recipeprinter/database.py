import psycopg2
from psycopg2 import sql

class Database:

    def __init__(self, db_config):
        self.config = db_config


    def __enter__(self):

        # Connect to your PostgreSQL database
        self.connection = psycopg2.connect(**self.config)

        # Create a cursor object to execute SQL queries
        self.cur = self.connection.cursor()

        return self


    def get_recipes(self):

        # query all recipes
        self.cur.execute("SELECT * FROM recipes")
        recipes = self.cur.fetchall()

        # create list containing recipes name and state 
        recipe_list = []
        for recipe in recipes:
            recipe_list.append({"name": recipe[0], "is_in_cart": False})
        return recipe_list


    def get_ingredients(self, recipes, ppl_count):

        # Build SQL Query to return recipe content
        ingredient_query = sql.SQL("""
        SELECT ingredient.ingre_name, unit, sum, type.type_name
        FROM ingredient
        JOIN ingredient_type as type
        ON type.type_key = ingredient.type_key
        JOIN 
        (SELECT ingre_name, unit, sum({})
        FROM ingredient_entry
        WHERE recipe_name in %s
        GROUP BY ingre_name, unit) as entry 
        ON ingredient.ingre_name = entry.ingre_name
        ORDER BY type.type_name;
        """).format(sql.Identifier(f"quantity_{ppl_count}ppl"))


        clean_ingredients = []
        if recipes: # check for empty list

            # query recipes in cart
            self.cur.execute(ingredient_query, (tuple(recipes),))
            raw_ingredients = self.cur.fetchall()

            # create dict for each entry  in cart            
            for i in raw_ingredients:
               
                clean_ingredients.append({
                    "name": i[0],
                    "unit": i[1],
                    "qty": i[2],
                    "type": i[3]
                })
        
        return clean_ingredients


    def __exit__(self, exc_type, exc_valu, exc_tb):

        # Close the cursor
        self.cur.close()

        # Close the connection
        self.connection.close()