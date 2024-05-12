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
	('Lemony Beef and Orzo Bowls'),
	('Salmon and Lemony Lentil Bowls'), 
	('Falafel Couscous'),
	('Creamy Squash Ravioli'),
	('Indonesian-Style Stir-Fried Noodles'),
	('Spicy Apricot Chicken'),
	('Chickpea Shakshuka'),
	('Fiesta Pork Salad'),
	('Sweet Pepper and Black Bean Taquitos'),
	('Ginger-Glazed Tofu Bowls');

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
	('Bread', 8),
	('Other', 9);
		
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
	('Green Onion', 6),
	('Tofu', 4),
	('Jasmine Rice', 2),
	('Sweet Bell Pepper', 6),
	('Edamame', 6),
	('Radish', 6),
	('Cilantro', 6),
	('Cashews', 7),
	('Oyster Sauce', 7),
	('Ginger Sauce', 7),
	('Cornstarch', 7), 
	('Rice Vinegar', 7),
	('Black Beans', 4),
	('Tortillas', 8),
	('Spring Mix', 6),
	('Monterey Jack Cheese', 5),
	('Ground Pork', 4),
	('Tortilla Chips', 7),
	('Corn Kernels',  3),
	('Red Onion', 6),
	('Tex-Mex Paste', 1),
	('Egg', 4),
	('Crushed Tomatoes with Garlic and Onion', 3),
	('Moroccan Spice Blend', 1),
	('Sesame Seeds', 7),
	('Chili Flakes', 1),
	('Chicken Tenders', 4),
	('White Wine', 9),
	('Apricot Spread', 7),
	('Chicken Broth Concentrate', 7),
	('Whole Grain Mustard', 7),
	('Chow Mein Noodles', 2),
	('Shanghai Bok Choy', 6),
	('Coleslaw Cabbage Mix', 6),
	('Crispy Shallots', 6),
	('Soy Sauce', 7),
	('Sweet Chili Sauce', 1),
	('Sesame Oil', 7), 
	('Squash Ravioli', 2),
	('Mushrooms', 6),
	('Parmesan', 5),
	('All-Purpose Flour', 2),
	('Cream', 5),
	('Falafel', 4),
	('Couscous', 2),
	('Carrot, julienned', 6),
	('Spicy Mayo', 7),
	('Salmon', 4),
	('Lentils', 2),
	('Sweet Potato', 6),
	('Vegetable Broth Concentrate', 7)
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
	('Lemony Beef and Orzo Bowls', 'Zesty Garlic Blend', 'tbsp', 1, 2),
	('Ginger-Glazed Tofu Bowls', 'Tofu', '', 1, 2),
	('Ginger-Glazed Tofu Bowls', 'Jasmine Rice', 'cups', 0.75, 1.5),
	('Ginger-Glazed Tofu Bowls', 'Sweet Bell Pepper', '', 1, 2),
	('Ginger-Glazed Tofu Bowls', 'Edamame', 'grams', 56, 113),
	('Ginger-Glazed Tofu Bowls', 'Radish', '', 3, 6),
	('Ginger-Glazed Tofu Bowls', 'Cilantro', 'grams', 7, 14),
	('Ginger-Glazed Tofu Bowls', 'Cashews', 'grams', 28, 56),
	('Ginger-Glazed Tofu Bowls', 'Oyster Sauce', 'tbsp', 4, 8),
	('Ginger-Glazed Tofu Bowls', 'Ginger Sauce', 'tbsp', 4, 8),
	('Ginger-Glazed Tofu Bowls', 'Cornstarch', 'tbsp', 1, 2),
	('Ginger-Glazed Tofu Bowls', 'Rice Vinegar', 'tbsp', 1, 2),
	('Ginger-Glazed Tofu Bowls', 'Garlic Salt', 'tsp', 1, 2),
	('Sweet Pepper and Black Bean Taquitos', 'Black Beans', '', 1, 2),
	('Sweet Pepper and Black Bean Taquitos', 'Tortillas', '', 6, 12),
	('Sweet Pepper and Black Bean Taquitos', 'Sweet Bell Pepper', '', 1, 2),
	('Sweet Pepper and Black Bean Taquitos', 'Baby Tomatoes', 'grams', 113, 227),
	('Sweet Pepper and Black Bean Taquitos', 'Yellow Onion', '', 1, 2),
	('Sweet Pepper and Black Bean Taquitos', 'Spring Mix', 'grams', 56, 113),
	('Sweet Pepper and Black Bean Taquitos', 'Monterey Jack Cheese', 'cups', 1, 2),
	('Sweet Pepper and Black Bean Taquitos', 'Tomato Sauce Base', 'tbsp', 2, 4),
	('Sweet Pepper and Black Bean Taquitos', 'Chipotle Sauce', 'tbsp', 2, 4),
	('Sweet Pepper and Black Bean Taquitos', 'Enchilada Spice Blend', 'tbsp', 1, 2),
	('Sweet Pepper and Black Bean Taquitos', 'Rice Vinegar', 'tbsp', 1,2),
	('Fiesta Pork Salad', 'Ground Pork', 'grams', 250, 500),
	('Fiesta Pork Salad', 'Spring Mix', 'grams', 113, 227),
	('Fiesta Pork Salad', 'Corn Kernels', 'grams', 113, 227),
	('Fiesta Pork Salad', 'Tomato', '', 1,2),
	('Fiesta Pork Salad', 'Red Onion', '', 1, 2),
	('Fiesta Pork Salad', 'Green Onion', '', 1,2),
	('Fiesta Pork Salad', 'Lemon', '', 1,2),
	('Fiesta Pork Salad', 'Sour Cream', 'tbsp', 3, 6),
	('Fiesta Pork Salad', 'Chipotle Sauce', 'tbsp', 2, 4),
	('Fiesta Pork Salad', 'Tex-Mex Paste', 'tbsp', 1,2),
	('Fiesta Pork Salad', 'Rice Vinegar', 'tbsp', 1,2),
	('Fiesta Pork Salad', 'Tortilla Chips', 'grams', 42.5, 85),
	('Chickpea Shakshuka', 'Chickpeas', '', 1,2),
	('Chickpea Shakshuka', 'Egg', '', 2,4),
	('Chickpea Shakshuka', 'Crushed Tomatoes with Garlic and Onion', '', 1,2),
	('Chickpea Shakshuka', 'Garlic', 'cloves', 2, 4),
	('Chickpea Shakshuka', 'Yellow Onion', '', 1,2),
	('Chickpea Shakshuka', 'Sweet Bell Pepper', '', 1, 2),
	('Chickpea Shakshuka', 'Baby Spinach', 'grams', 56, 113),
	('Chickpea Shakshuka', 'Moroccan Spice Blend', 'tbsp', 2, 4),
	('Chickpea Shakshuka', 'Flatbread', '', 2, 4),
	('Chickpea Shakshuka', 'Sesame Seeds', 'tbsp', 1, 2),
	('Chickpea Shakshuka', 'Feta Cheese', 'cups', 0.25, 0.5),
	('Chickpea Shakshuka', 'Chili Flakes', 'tsp', 0.25, 0.25),
	('Spicy Apricot Chicken', 'Chicken Tenders', 'grams', 310, 620),
	('Spicy Apricot Chicken', 'Orzo', 'grams', 170, 340),
	('Spicy Apricot Chicken', 'Sweet Bell Pepper', '', 1,2),
	('Spicy Apricot Chicken', 'Baby Spinach', 'grams', 56, 113),
	('Spicy Apricot Chicken', 'White Wine', 'tbsp', 4, 8),
	('Spicy Apricot Chicken', 'Apricot Spread', 'tbsp', 2, 4),
	('Spicy Apricot Chicken', 'Chicken Broth Concentrate', '', 2,4),
	('Spicy Apricot Chicken', 'Whole Grain Mustard', 'tbsp', 1,2),
	('Spicy Apricot Chicken', 'Garlic Salt', 'tsp', 1,2),
	('Spicy Apricot Chicken', 'Chili Flakes', 'tsp', 1,2),
	('Indonesian-Style Stir-Fried Noodles', 'Egg', '', 2, 4),
	('Indonesian-Style Stir-Fried Noodles', 'Chow Mein Noodles', 'grams', 200, 400),
	('Indonesian-Style Stir-Fried Noodles', 'Sweet Bell Pepper', '',1, 2),
	('Indonesian-Style Stir-Fried Noodles', 'Shanghai Bok Choy', '', 1, 2),
	('Indonesian-Style Stir-Fried Noodles', 'Coleslaw Cabbage Mix', 'grams', 170, 340),
	('Indonesian-Style Stir-Fried Noodles', 'Green Onion', '', 2,2),
	('Indonesian-Style Stir-Fried Noodles', 'Crispy Shallots', 'grams', 28, 56),
	('Indonesian-Style Stir-Fried Noodles', 'Oyster Sauce', 'tbsp', 4,8),
	('Indonesian-Style Stir-Fried Noodles', 'Soy Sauce', 'tbsp', 2,4),
	('Indonesian-Style Stir-Fried Noodles', 'Sweet Chili Sauce', 'tbsp', 2, 4),
	('Indonesian-Style Stir-Fried Noodles', 'Sesame Oil', 'tbsp', 1,2),
	('Creamy Squash Ravioli', 'Squash Ravioli', 'grams', 350, 700),
	('Creamy Squash Ravioli', 'Mushrooms', 'grams', 112, 227),
	('Creamy Squash Ravioli', 'Baby Spinach', 'grams', 28, 56),
	('Creamy Squash Ravioli', 'Parmesan', 'cups', 0.25, 0.5),
	('Creamy Squash Ravioli', 'Vegetable Broth Concentrate', '', 1,2),
	('Creamy Squash Ravioli', 'All-Purpose Flour', 'tbsp', 1,2),
	('Creamy Squash Ravioli', 'Cream', 'ml', 56, 113),
	('Creamy Squash Ravioli', 'White Wine', 'tbsp', 4,8),
	('Falafel Couscous', 'Falafel', '', 8, 16),
	('Falafel Couscous', 'Couscous', 'cups', 0.5, 1),
	('Falafel Couscous', 'Olives', 'grams', 30, 60),
	('Falafel Couscous', 'Baby Tomatoes', 'grams', 227, 454),
	('Falafel Couscous', 'Garlic', 'cloves', 1, 2),
	('Falafel Couscous', 'Feta Cheese','cups', 0.25, 0.5),
	('Falafel Couscous', 'Carrot, julienned', 'grams', 56, 113),
	('Falafel Couscous', 'Lemon', '', 1,1 ),
	('Falafel Couscous', 'Cilantro', 'grams', 7, 14),
	('Falafel Couscous', 'Spicy Mayo', 'tbsp', 4, 8),
	('Falafel Couscous', 'Radish', '', 3, 6),
	('Salmon and Lemony Lentil Bowls', 'Salmon', 'grams', 250, 500),
	('Salmon and Lemony Lentil Bowls', 'Lentils', '', 1,2),
	('Salmon and Lemony Lentil Bowls', 'Baby Spinach', 'grams', 56, 113),
	('Salmon and Lemony Lentil Bowls', 'Lemon', '', 1,2),
	('Salmon and Lemony Lentil Bowls', 'Sour Cream', 'tbsp', 3, 6),
	('Salmon and Lemony Lentil Bowls', 'Feta Cheese', 'cups', 0.25, 0.5),
	('Salmon and Lemony Lentil Bowls', 'Garlic', 'cloves', 2, 4),
	('Salmon and Lemony Lentil Bowls', 'Sweet Potato', '', 1,2)
	;


-- RETURN FINAL RESULTS
SELECT * FROM public.ingredient_entry as e
JOIN public.ingredient as i ON i.ingre_name = e.ingre_name
JOIN public.ingredient_type as t ON i.type_key = t.type_key;

