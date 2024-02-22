# standard libary imports
from io import StringIO
from datetime import datetime 

# local imports
import recipeprinter.database as db
import recipeprinter.cli.helpers as cli_fn

def run(db_config):
    # launch CLI controller

    output = StringIO("")        # store terminal outputs here
    current_date = datetime.now().strftime("%Y-%m-%d")
    file_name = f"shopping_list_{current_date}.txt"

    # setup database connection
    with db.Database(db_config) as d:

        # get list of recipes from database
        all_recipes_list = d.get_recipes()

        # get user to select recipes
        cli_fn.menu_loop(all_recipes_list)
        ppl_count_int = cli_fn.ppl_count()

        # create list of names of recipes in the cart
        selected_recipes = []
        for r in all_recipes_list:
            if r["is_in_cart"]:
                selected_recipes.append(r["name"])

        # get list of ingredients from database
        ingredients = d.get_ingredients(selected_recipes, ppl_count_int)


    ##################################################
    #              START PRINTING                    #
    ##################################################

    # headers
    output.write(f"list generated on {current_date}\n")
    output.write(f"serving(s) for {ppl_count_int} people\n")
    output.write(f"\nIngredients for the following:\n")
    for r in selected_recipes: 
        output.write(f" - {r}\n")
    output.write("\ningredient                     unit      qty   type\n")
    output.write("-----------------------------------------------------------\n")

    # ingredients contents
    for i in ingredients:

        output.write(f"{i["name"]:30} {i["unit"]:10}")
        # omit decimals if value is a whole number
        if i["qty"] % 1 == 0:
            output.write(f"{i["qty"]:<6.0f}")   
        else:
            output.write(f"{i["qty"]:<6}") 
        output.write(f"{i["type"]:10}\n")


    ##################################################
    #                   STOP PRINTING                #
    ##################################################

    # save to file?
    if(input(f"\nsave to './{file_name}'? (y/n) ").lower() == 'y'):
        with open(file_name, 'w') as f:
            f.write(output.getvalue())

    # Close the output buffer
    print(f"\nplease wait... generating list...\n")
    print(output.getvalue())
    output.close()