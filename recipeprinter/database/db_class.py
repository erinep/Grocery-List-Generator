# third party modules
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

    def get_recipes_list(self):

        # query all recipes
        self.cur.execute("SELECT recipe_name FROM recipes")
        recipes = self.cur.fetchall()

        # create list containing recipes name and state 
        recipe_list = []
        for recipe in recipes:
            recipe_list.append(recipe[0])
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


    def get_categories(self):
        # return list of tuples with ingredient type_names and type_key


        # Build SQL Query to return ingredient categories
        type_query = sql.SQL("SELECT * FROM ingredient_type;")
        self.cur.execute(type_query)
        types = self.cur.fetchall()
        return types
        
    
    def add_ingredient(self, ingredient):
        ''' add a single new ingredient: ingredient is a tuple of type = (ingre_name, type_key) '''


        print('inserting ', ingredient)
        self.cur.execute("""
        INSERT
        INTO ingredient (ingre_name, type_key)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;""", 
        ingredient)


    def add_ingredients(self, ingredients):
        '''
        Add a list of ingredients to database
        '''
        for i in ingredients:
            self.add_ingredient(i)


    def add_recipe(self, recipe_name):
        '''
        Add a recipe name to the recipes table database
        '''

        self.cur.execute("""
        INSERT
        INTO recipes (recipe_name)
        VALUES (%s)
        ON CONFLICT DO NOTHING;""",
        (recipe_name,))


    def add_ingredient_entry(self, ingredient):
        '''
        Add an entry in the recipe_ingredient table
        '''
        self.cur.execute("""
        INSERT
        INTO ingredient_entry (recipe_name, ingre_name, unit, quantity_2ppl, quantity_4ppl)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;""",
        ingredient)



    def add_ingredient_enties(self, ingredients):
        '''
        Add a list of ingredient entries
        '''
        for i in ingredients:
            self.add_ingredient_entry(i)
  

    def __exit__(self, exc_type, exc_valu, exc_tb):

        # commint your changes
        self.connection.commit()

        # Close the cursor
        self.cur.close()

        # Close the connection
        self.connection.close()