from io import StringIO
import psycopg2
from psycopg2 import sql
from datetime import datetime 
from menu import menu_fn, ppl_count

output = StringIO("")        # store terminal outputs here
current_date = datetime.now().strftime("%Y-%m-%d")
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

# create list of dictionaries containing recipes name and state 
recipe_list = []
for recipe in recipes:
    recipe_list.append({"name": recipe[0], "is_in_cart": False})


menu_fn(recipe_list)
ppl_count_int = ppl_count()

# Build SQL Query to return recipe content
ingredient_query = sql.SQL("""
SELECT ingre_name, unit, sum({})
FROM ingredients 
WHERE recipe_name in %s
GROUP BY ingre_name, unit
ORDER BY ingre_name
""").format(sql.Identifier(f"quantity_{ppl_count_int}ppl"))

# create list of names of recipes in the cart
recipes_in_cart = []
for r in recipe_list:
    if r["is_in_cart"]:
        recipes_in_cart.append(r["name"])

# print all selected recipes
output.write(f"list generated on {current_date}\n")
output.write(f"serving(s) for {ppl_count_int} people\n")
output.write(f"\nIngredients for the following:\n")
for r in recipes_in_cart:
    output.write(f" - {r}\n")


# print header
output.write(f"""\ningredient                     unit      qty
-----------------------------------------------\n""")

# query items in cart
if recipes_in_cart:
    cur.execute(ingredient_query, (tuple(recipes_in_cart),))
    ingredients = cur.fetchall()
    for i in ingredients:
        i_name = i[0] 
        i_unit = i[1]
        i_qty = i[2]

        output.write(f"{i_name:30} {i_unit:10}")
        # omit decimals if value is a whole number
        if i_qty % 1 == 0:
            output.write(f"{i_qty:<6.0f}")   
        else:
            output.write(f"{i_qty:<6}") 
        output.write(f"\n")
else:
    output.write("\nno items selected...\n")

# save to file?
if(input(f"\nsave to './{file_name}'? (y/n) ").lower() == 'y'):
    with open(file_name, 'w') as f:
        f.write(output.getvalue())

# Close the output buffer
print(f"\nplease wait... generating list...\n")
print(output.getvalue())
output.close()

# Close the cursor
cur.close()

# Close the connection
connection.close()
