# Grocery List Generator

CLI tool to generate a Grocery Shopping list

## Instructions

- Use create_tables.sql file to populate your postgress server
- navigate to project root (`cd <PROJECT-ROOT>`)
- setup your db config parameters in ./recipeprinter/__main__.py
- Dev build commands: `pip install -e . ; python -m recipeprinter` 
- Create python wheel using `python -m build` (and run it using: `pip install <PATH-TO-WHL-FILE> ; python -m recipeprinter`)

## Sample user input

```
> python .\recipeprinter\__main__.py

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
list generated on 2024-02-18
serving(s) for 2 people

Ingredients for the following:
 - Chicken Bulgur Bowls
 - Lemony Beef and Orzo Bowls

ingredient                     unit      qty   type
-----------------------------------------------------------
Mayonnaise                     tbsp      2     Condements
Tomato Sauce Base              tbsp      2     Condements
Sour Cream                     tbsp      3     Dairy     
Feta Cheese                    cups      0.50  Dairy     
Parsley                        grams     7     fruit and veggie
Garlic                         cloves    1     fruit and veggie
Tomato                                   1     fruit and veggie
Baby Tomatoes                  grams     113   fruit and veggie
Baby Spinach                   grams     112   fruit and veggie
Sweet Bell Pepper                        1     fruit and veggie
Lemon                                    2     fruit and veggie
Jalapeno                                 1     fruit and veggie
Bulgur Wheat                   cups      0.50  Grains    
Orzo                           grams     170   Grains    
Chicken Breasts                          2     Protein   
Ground Beef                    grams     250   Protein   
Smoked Paprika Garlic Blend    tbsp      1     Spices    
Garlic Salt                    tsp       1     Spices    
Zesty Garlic Blend             tbsp      1     Spices    

```
