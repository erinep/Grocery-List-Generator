def menu_fn(my_recipes):
    # Manage user menu selection of recipes

    def print_recipes():
    # print recipe options
        print(f"\nRECIPE LIST")
        for r in my_recipes:
            print(f"[{'x' if my_recipes[r] else ' '}] {r}")

    print(f"\nPlease select recipes to add to your cart")

    # loop while user selects the recipes they want
    while (True):
        print_recipes()
        usr_input = input(f"\nenter recipe name (enter 'c' to checkout): ")

        if usr_input.lower() in ['c']:
            break
        
        if usr_input in my_recipes.keys():
            my_recipes[usr_input] =  True
        else: 
            print('item not found. Please try again')
