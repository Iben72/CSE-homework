# nested if statements were included in the code. The game was also played by two friends
# who said they observed different outputs based on the user response.



print(
"You started on an adventure to the woods with your bicycle. "
"Halfway into your destination, you encountered an unexpected guest: "
"a huge bear."
)

scene1 = input("Would you RUN away or STAND still? ").strip().lower()

if scene1 == "run":
   print(
"\nYou quickly run with all your strength and eventually arrive at "
"a lake infested with hungry-looking crocodiles."
)


scene2 = input("Would you DIVE into the lake or PUSH back? ").strip().lower()

if scene2 == "dive":
    print(
        "\nYou dive into the lake and soon discover that the crocodiles "
        "are rather friendly to you, but the water is too cold to endure."
    )

    scene3 = input("Would you ACCEPT the crocodile friendship or RESIST it? ").strip().lower()

    if scene3 == "accept":
        print(
            "\nYou accept the friendship in fear of the consequence of not accepting, "
            "and you are constantly looking for a way of escape."
        )
    elif scene3 == "resist":
        print(
            "\nYou resign to fate and resist the crocodile friendship advances. "
            "With your eyes closed, you take your last breath."
        )
    else:
        print("\nYou become frozen in the unbearable ice-laden lake.")

elif scene2 == "push back":
    print(
        "\nYou push back and find a narrow trail leading to a hidden cave. "
        "Inside, you find shelter and begin to warm up."
    )
else:
    print("\nConfused and indecisive, you slip and fall into the lake.")


if scene1 == "stand still":
    print("\nYou stand still as the bear sniffs around. To your surprise, it turns and walks away. "
         "You continue your journey, both shaken and amazed.")

else:
    print("\nFrozen by indecision, the bear approaches and you slowly back away into the woods.")