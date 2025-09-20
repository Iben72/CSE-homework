import locale

money_value = 1245.60

currency_symbol ='RS'

locale_value = 'pt_BR.UTF-8'

# set the local parameters and convert the value

locale.setlocale(locale.LC_ALL, locale_value)
money_formated =locale.currency(money_value,
grouping = True,
symbol = currency_symbol)

# write a program to convert from Fahrenheit to Celcius.
# display the result to one decimal place of precision.
# to convert degrees in Fahrenheit to Celcius, you need to subtract 32 from the Fahrenheit amount and then multiply by the
# fraction of 5/9

fahrenheit = float(input(" what is the temperature in fahrenheit? "))

fahrenheit_to_celcius = (fahrenheit - 32) * 5/9

print(f"the temoerature in celcius is: {fahrenheit_to_celcius:.1f}")
      
      
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

sales_tax_rate = float(input(" what is the sales tax rate? "))

print(f" the sales tax rate is {sales_tax_rate:.2f}")

sales_tax = sales_tax_rate/100 * subtotal

print(f" the sales tax is ${sales_tax:.2f}")

total = subtotal + sales_tax

print(f" the total cost of meal is ${total:.2f}")

payment_amount = float(input(" what is the payment amount? "))

print(f" the amount paid is ${payment_amount:.2f}")

change = payment_amount - total

print(f" the change is ${change:.2f}")


