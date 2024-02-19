-- remove old tables
DROP TABLE IF EXISTS public.ingredient_entry, public.ingredient,  public.ingredient_type, public.recipes;

-- CREATE recipes table
CREATE TABLE IF NOT EXISTS public.recipes
(
    recipe_name text PRIMARY KEY
) TABLESPACE pg_default;

-- create ingredients categories table
CREATE TABLE IF NOT EXISTS public.ingredient_type
(
	type_name text,
	type_key integer PRIMARY KEY
);

-- create ingredients list
CREATE TABLE IF NOT EXISTS public.ingredient
(
    ingre_name text PRIMARY KEY,
	type_key integer,
	FOREIGN KEY (type_key) REFERENCES public.ingredient_type(type_key)
);

-- CREATE ingredient recipe entry table
CREATE TABLE IF NOT EXISTS public.ingredient_entry
(
	ingre_entry_key integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	ingre_name text,
	recipe_name text,
	unit text,
	quantity_2ppl numeric(6, 2),
	quantity_4ppl numeric(6,2),
	FOREIGN KEY (ingre_name) REFERENCES public.ingredient(ingre_name),
	FOREIGN KEY (recipe_name) REFERENCES public.recipes(recipe_name)
) TABLESPACE pg_default;



-- Give test user access
GRANT SELECT ON ALL TABLES IN SCHEMA public TO test_user;



-- INSERT recipes into tables
INSERT INTO public.recipes(recipe_name )
VALUES 
	('Chicken Bulgur Bowls'),
	('Beef Taco Salad Bowls'),
	('Fattoush-Inspired Salad'),
	('Tangy Beef Burgers'),
	('Lemony Beef and Orzo Bowls');

-- INSERT ingredients types
INSERT INTO public.ingredient_type (type_name, type_key)
VALUES 
	('Spices', 1),
	('Grains', 2),
	('Canned Goods', 3),
	('Protein', 4),
	('Dairy', 5),
	('fruit and veggie', 6),
	('Condements', 7), 
	('Bread', 8);
		
-- INSERT ingredient
INSERT into public.ingredient (ingre_name, type_key)
VALUES
	('Chicken Breasts', 4), 
	('Baby Spinach', 6),
	('Sour Cream', 5), 
	('Mayonnaise', 7),
	('Lemon', 6),
	('Jalapeno', 6),
	('Smoked Paprika Garlic Blend', 1),
	('Bulgur Wheat', 2),
	('Parsley', 6),
	('Garlic', 6),
	('Tomato', 6),
	('Ground Beef', 4),
	('Green Bell Pepper', 6),
	('Guacamole', 7),
	('Cheddar Cheese', 5),
	('Chipotle Sauce', 7),
	('Enchilada Spice Blend', 1),
	('Chickpeas', 3),
	('Shawarma Spice Blend', 1),
	('Flatbread',8 ),
	('Baby Tomatoes', 6),
	('Olives', 3),
	('White Wine Vinegar', 7),
	('Sweet Bell Pepper', 6),
	('Atrisan Bun', 8),
	('Dijon Mustard', 7),
	('Dill Pickle', 7),
	('Red Potato', 6),
	( 'Yellow Onion', 6),
	( 'Panko Breadcrumbs', 7),
	( 'Ketchup', 7),
	( 'Orzo', 2),
	( 'Feta Cheese', 5),
	( 'Tomato Sauce Base', 7),
	( 'Garlic Salt', 1),
	( 'Zesty Garlic Blend', 1),
	('Green Onion', 6)
	;
	
	
	

-- INSERT ingredients entries in recipe
INSERT INTO public.ingredient_entry (recipe_name, ingre_name, unit, quantity_2ppl, quantity_4ppl)
VALUES
	('Chicken Bulgur Bowls', 'Chicken Breasts', '', 2, 4),
	('Chicken Bulgur Bowls', 'Baby Spinach', 'grams', 56, 113),
	('Chicken Bulgur Bowls', 'Sour Cream', 'tbsp', 3, 6),
	('Chicken Bulgur Bowls', 'Mayonnaise', 'tbsp', 2, 4),
	('Chicken Bulgur Bowls', 'Lemon', '', 1, 2),
	('Chicken Bulgur Bowls', 'Jalapeno', '', 1, 2),
	('Chicken Bulgur Bowls', 'Smoked Paprika Garlic Blend', 'tbsp', 1, 2),
	('Chicken Bulgur Bowls', 'Bulgur Wheat', 'cups', 0.5, 1),
	('Chicken Bulgur Bowls', 'Parsley', 'grams', 7, 14),
	('Chicken Bulgur Bowls', 'Garlic', 'cloves', 1, 2),
	('Chicken Bulgur Bowls', 'Tomato', '', 1, 2),
	('Beef Taco Salad Bowls', 'Ground Beef', 'grams', 250, 500),
	('Beef Taco Salad Bowls', 'Baby Spinach', 'grams', 113, 227),
	('Beef Taco Salad Bowls', 'Green Bell Pepper', '', 1, 2),
	('Beef Taco Salad Bowls', 'Tomato', '', 1, 2),
	('Beef Taco Salad Bowls', 'Guacamole', 'tbsp', 3, 6),
	('Beef Taco Salad Bowls', 'Lemon', '', 0.5, 1),
	('Beef Taco Salad Bowls', 'Green Onion', '', 1, 2),
	('Beef Taco Salad Bowls', 'Cheddar Cheese', 'cups', 0.25, 0.5),
	('Beef Taco Salad Bowls', 'Sour Cream', 'tbsp', 3, 6),
	('Beef Taco Salad Bowls', 'Chipotle Sauce', 'tbsp', 2, 4),
	('Beef Taco Salad Bowls', 'Enchilada Spice Blend', 'tbsp', 1, 2),
	('Fattoush-Inspired Salad', 'Chickpeas', 'ml', 370, 740),
	('Fattoush-Inspired Salad', 'Shawarma Spice Blend', 'tbsp', 1, 2),
	('Fattoush-Inspired Salad', 'Garlic', 'cloves', 2, 4),
	('Fattoush-Inspired Salad', 'Flatbread', '', 2, 4),
	('Fattoush-Inspired Salad', 'Baby Tomatoes', 'grams', 113, 227),
	('Fattoush-Inspired Salad', 'Parsley', 'grams', 7, 14),
	('Fattoush-Inspired Salad', 'Olives', 'grams', 30, 60),
	('Fattoush-Inspired Salad', 'Green Onion', '', 2, 4),
	('Fattoush-Inspired Salad', 'White Wine Vinegar', 'tbsp', 2, 4),
	('Fattoush-Inspired Salad', 'Sweet Bell Pepper', '', 1,2),
	('Fattoush-Inspired Salad', 'Feta Cheese', 'cups', 0.5, 1),
	('Tangy Beef Burgers', 'Ground Beef', 'grams', 250, 500),
	('Tangy Beef Burgers', 'Atrisan Bun', '', 2, 4),
	('Tangy Beef Burgers', 'Dijon Mustard', 'tbsp', 1,2),
	('Tangy Beef Burgers', 'Dill Pickle', 'ml', 90, 180),
	('Tangy Beef Burgers', 'Red Potato', 'grams', 350, 700),
	('Tangy Beef Burgers', 'Yellow Onion', '', 1,2),
	('Tangy Beef Burgers', 'Mayonnaise', 'tbsp', 4, 8),
	('Tangy Beef Burgers', 'Parsley', 'grams', 7, 7),
	('Tangy Beef Burgers', 'Cheddar Cheese', 'cups', 0.25, 0.5),
	('Tangy Beef Burgers', 'Panko Breadcrumbs', 'cups', 0.25, 0.5),
	('Tangy Beef Burgers', 'Ketchup', 'tbsp', 2, 4),
	('Lemony Beef and Orzo Bowls', 'Ground Beef', 'grams', 250, 500),
	('Lemony Beef and Orzo Bowls', 'Orzo', 'grams', 170, 340),
	('Lemony Beef and Orzo Bowls', 'Feta Cheese', 'cups', 0.5, 1),
	('Lemony Beef and Orzo Bowls', 'Sweet Bell Pepper', '', 1, 2),
	('Lemony Beef and Orzo Bowls', 'Baby Tomatoes', 'grams', 113, 227),
	('Lemony Beef and Orzo Bowls', 'Baby Spinach', 'grams', 56, 113),
	('Lemony Beef and Orzo Bowls', 'Lemon', '', 1, 1),
	('Lemony Beef and Orzo Bowls', 'Tomato Sauce Base', 'tbsp', 2,4),
	('Lemony Beef and Orzo Bowls', 'Garlic Salt', 'tsp', 1, 2),
	('Lemony Beef and Orzo Bowls', 'Zesty Garlic Blend', 'tbsp', 1, 2)
	;


-- RETURN FINAL RESULTS
SELECT * FROM public.ingredient_entry as e
JOIN public.ingredient as i ON i.ingre_name = e.ingre_name
JOIN public.ingredient_type as t ON i.type_key = t.type_key;

