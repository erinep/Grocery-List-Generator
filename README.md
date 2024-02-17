# Grocery List Generator

CLI tool to generate a Grocery Shopping list

## Instructions

- Use create_tables.sql file to populate your postgress server
- run `python recipeprinter.py`
- Selects the recipes you want and the script will output a list of what to buy

## Sample user input

```
> python .\recipeprinter.py

Please select recipes to add to your cart

RECIPE LIST
 1. [ ] Chicken Bulgur Bowls
 2. [ ] Beef Taco Salad Bowls
 3. [ ] Fattoush-Inspired Salad
 4. [ ] Tangy Beef Burgers
 5. [ ] Lemony Beef and Orzo Bowls

enter recipe number (or 'c' to checkout): 1

RECIPE LIST
 1. [x] Chicken Bulgur Bowls
 2. [ ] Beef Taco Salad Bowls
 3. [ ] Fattoush-Inspired Salad
 4. [ ] Tangy Beef Burgers
 5. [ ] Lemony Beef and Orzo Bowls

enter recipe number (or 'c' to checkout): 6
invalid item. Please try again

RECIPE LIST
 1. [x] Chicken Bulgur Bowls
 2. [ ] Beef Taco Salad Bowls
 3. [ ] Fattoush-Inspired Salad
 4. [ ] Tangy Beef Burgers
 5. [ ] Lemony Beef and Orzo Bowls

enter recipe number (or 'c' to checkout): 5

RECIPE LIST
 1. [x] Chicken Bulgur Bowls
 2. [ ] Beef Taco Salad Bowls
 3. [ ] Fattoush-Inspired Salad
 4. [ ] Tangy Beef Burgers
 5. [x] Lemony Beef and Orzo Bowls

enter recipe number (or 'c' to checkout): c

How many people? (2 or 4) 2

save to './shopping_list_2024-02-17.txt'? (y/n) y

please wait... generating list...
```

## Sample Output:

```
list generated on 2024-02-17
serving(s) for 2 people

Ingredients for the following:
 - Chicken Bulgur Bowls
 - Lemony Beef and Orzo Bowls

ingredient                     unit      qty
-----------------------------------------------
Baby Spinach                   grams     112
Baby Tomatoes                  grams     113
Bulgur Wheat                   cups      0.50
Chicken Breats                           2
Feta Cheese                    cups      0.50
Garlic                         cloves    1
Garlic Salt                    tsp       1
Ground Beef                    grams     250
Jalapeno                                 1
Lemon                                    2
Mayonnaise                     tbsp      2
Orzo                           grams     170
Parsley                        grams     7
Smoked Paprika Garlic Blend    tbsp      1
Sour Cream                     tbsp      3
Sweet Bell Pepper                        1
Tomato                                   1
Tomato Sauce Base              tbsp      2
Zesty Garlic Blend             tbsp      1 
```