try:
    cart_list = []
    while True:
        name_item = input("Add an item: type quit to stop: ")
        if name_item == "quit":
            break
        price = float(input("what is the price of the item? "))
        quantity_item = input("how many of the item? ")
        total_price_item = (price * quantity_item
        overall_total = sum(total_price_item)
        cart_list.append((name_item, price,quantity_item,total_price_item))
        print(f"\n{name_item} - ${price}")

    print("Your cart:", cart_list,overall_total)
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
