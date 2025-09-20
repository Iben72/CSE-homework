# additional price was added  to subtotal price due to the cost of juice in ln 19.

child_meal_price = float(input(" what is the price of a child's meal? "))

print(f" the price of a child's meal is ${child_meal_price:.2f}")

adult_meal_price = float(input(" what is the price of an adult meal? "))

print(f" the price of an adult meal is ${adult_meal_price:.2f}")

child_count = int(input(" how many children are there? "))

print(f" the number of children is {child_count}")

adult_count = int(input("how many adults are there? "))

print(f" the number of adult is {adult_count}")

cost_of_juice = float(input(" what is the total cost of juice? "))

print(f" the total cost of juice is ${cost_of_juice:.2f}")

subtotal = (child_meal_price * child_count) + (adult_meal_price * adult_count) + (cost_of_juice)

print(f" subtotal amount is ${subtotal:.2f}")
