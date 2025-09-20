shop_list = []
item = []



while True:
    item = input("Please type an item for the shopping list (type 'quit' to stop): ")
    if item.lower() == "quit":
        break
    shop_list.append(item)

print("\nThe items in the shopping list are:")
for item in shop_list:
    print(f" {item}")

for index, item in enumerate(shop_list):  #safer to use enumerate when indexing.
    print(f"{index}: {item}")

for i in range(len(shop_list)): # this also works but it is prone to a higher risk of bug.
    print(f"{i}: {shop_list[i]}")
    

        

          


     

# 