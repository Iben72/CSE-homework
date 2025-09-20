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