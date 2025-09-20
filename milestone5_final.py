# for creativity, the quantity of each item and their respective total price where determine.
# the payment options were also included for customers to make their choice.


print("Welcome to the Shopping Cart Activity")

items = []      
prices = []     
quantities = [] 

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = input("Please enter an action: ")

    if action == "1":
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        quantity = int(input(f"How many '{item}' would you like to add? "))
        items.append(item)
        prices.append(price)
        quantities.append(quantity)
        print(f"{quantity} x '{item}' has been added to the cart.")

    elif action == "2":
        if not items:
            print("Your cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            print(f"{'No.':<5}{'Item':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
            for i in range(len(items)):
                total = prices[i] * quantities[i]
                print(f"{i+1:<5}{items[i]:<15}{quantities[i]:<5}${prices[i]:<9.2f}${total:.2f}")

    elif action == "3":
        if not items:
            print("Your cart is empty.")
            continue
        print("The contents of the shopping cart are:")
        for i in range(len(items)):
            print(f"{i+1}. {items[i]} - {quantities[i]} x ${prices[i]:.2f}")
        index = int(input("Which item would you like to remove? ")) - 1
        if 0 <= index < len(items):
            removed_item = items.pop(index)
            prices.pop(index)
            quantities.pop(index)
            print(f"{removed_item} removed from the cart.")
        else:
            print("Sorry, that is not a valid item number.")

    elif action == "4":
        total = sum(prices[i] * quantities[i] for i in range(len(items)))
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    elif action == "5":
        print("Thank you")
        break
    else:
        print("Invalid option. Please choose between 1 and 5.")
while True:
    print("\nYour payment options are:")
    print("1. Cash")
    print("2. Credit Card")
    print("3. Cheque")

    option = input("Please choose a payment option: ")

    if option in ["1", "2", "3"]:
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 3.")
 
