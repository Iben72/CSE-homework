friends = []

name = None

while name != "end":
    name = input("type the name of a friend: ")

    if name != "end":
        friends.append(name)
print()
print(f"your friends are:")
print(friends)
