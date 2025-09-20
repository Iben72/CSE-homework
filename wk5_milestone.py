print("Welcome to the Shopping Cart activity")

cart = []

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
        cart.append(item)
        print(f"'{item}' has been added to the cart.")
    elif action == "2":
        print("The contents of the shopping cart are:")
        for item in cart:
            print(item)
    elif action == "5":
        print("Thank you. Goodbye.")
        break
    else:
        print("This option is not available.")
