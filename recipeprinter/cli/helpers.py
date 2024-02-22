
def menu_loop(my_recipes):
    # Manage user menu selection of recipes

    def print_recipes():
    # print recipe options
        print(f"\nRECIPE LIST")
        count = 1
        for r in my_recipes:
            print(f" {count}. [{'x' if r["is_in_cart"] else ' '}] {r["name"]}")
            count += 1

    print(f"\nPlease select recipes to add to your cart")

    # loop while user selects the recipes they want
    while (True):
        print_recipes()
        usr_input = input(f"\nenter recipe number (or 'c' to checkout): ")

        if usr_input.lower() in ['c']:
            break
        
        try: 
            usr_input_number = int(usr_input)
            if usr_input_number in range(1, len(my_recipes)+1):
                my_recipes[usr_input_number -1]["is_in_cart"] =  True
            else:
                print('invalid item. Please try again')


        except:
            print('invalid input. Please try again')

def ppl_count():
    user_input =  input(f"\nHow many people? (2 or 4) ")
    while (user_input not in ['2', '4']):
        print("invalid input...")
        user_input =  input(f"\nHow many people? (2 or 4) ")
    return user_input