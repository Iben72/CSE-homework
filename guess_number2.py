import random

keep_playing = "yes"
while keep_playing.lower() == "yes":
    secret_number = random.randint(1, 100)
    guess = -1
    guess_count = 0

    while guess != secret_number:
        try:
            guess = int(input("What is your guess? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        guess_count += 1

        if guess < secret_number:
            print("Higher")
        elif guess > secret_number:
            print("Lower")
        else:
            print("You got it!")

    print(f"It took you {guess_count} guesses.")

    # performance rating
    if guess_count < 3:
        print("Excellent")
    elif guess_count < 5:
        print("Good")
    elif guess_count <= 6:
        print("Fair")
    else:
        print("Poor")

    keep_playing = input("Would you like to play again? (yes/no): ")
    
