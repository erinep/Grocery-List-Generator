SELECT ingredient.ingre_name, type.type_name, unit, sum FROM 
ingredient
JOIN
ingredient_type as type
ON type.type_key = ingredient.type_key
JOIN 
(SELECT ingre_name, unit, sum(quantity_4ppl)
FROM ingredient_entry
WHERE recipe_name in ('Chicken Bulgur Bowls')
GROUP BY ingre_name, unit
ORDER BY ingre_name) as entry 
ON ingredient.ingre_name = entry.ingre_name
ORDER BY type.type_name;