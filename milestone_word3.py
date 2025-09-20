secret_word = "jonah"
guess_count = 0

while True:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break
    else:
        print("Your guess was not correct.")
