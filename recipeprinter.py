from io import StringIO
import psycopg2
from psycopg2 import sql
from datetime import date
from menu import menu_fn

output = StringIO("")        # store terminal outputs here
current_date = date.today()
file_name = f"shopping_list_{current_date}.txt"

# Connect to your PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="test_user",
    password="password"
)

# Create a cursor object to execute SQL queries
cur = connection.cursor()

# query all recipes
cur.execute("SELECT * FROM recipes")
recipes = cur.fetchall()

# create hashmap containing recipes keys 
recipe_map = {}
for recipe in recipes:
    recipe_map[recipe[0]] = False


menu_fn(recipe_map)

# Build SQL Query to return recipe content
ingredient_query = sql.SQL("SELECT * FROM ingredients WHERE {} = %s").format(
    sql.Identifier("recipe_name")
)

# query the list of for all selected recipes 
for recipe, in_cart in recipe_map.items():
    if in_cart:
        cur.execute(ingredient_query, (recipe,))
        ingredients = cur.fetchall()
       
        # print recipe contents
        output.write(f"\n{recipe}\n")
        for i in range(len(recipe)):
            output.write("=")
        output.write("\n")

        for ingredient in ingredients:
            i_name = ingredient[1] 
            i_unit = ingredient[3]
            i_qty = ingredient[4]         # index[4] for 2 ppl, index[5] for 4 ppl
            output.write(f"{i_qty} {i_unit} {i_name}\n")
        output.write("\n")

# save to file?
if(input(f"\nsave to {file_name}? (y/n)").lower() == 'y'):
    with open(file_name, 'w') as f:
        f.write(output.getvalue())

# Close the output buffer
print(output.getvalue())
output.close()

# Close the cursor
cur.close()

# Close the connection
connection.close()
