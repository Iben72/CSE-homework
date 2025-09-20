secret_word = "jonah"
guess_count = 0

hint = "-" * len(secret_word)

while True:
    print(f"The hint is: {hint}")
    guess = input("What is your guess? ").lower()
    guess_count += 1
    



    if len(guess) != len(secret_word):
        print(f"Sorry, the guess must have {len(secret_word)} letters.")
        continue

    if guess == secret_word:
        print("Congratulations! You got it!")
        print(f"It took you {guess_count} guesses.")

        break

    new_hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            new_hint += guess[i].upper()  
        elif guess[i] in secret_word:
            new_hint += guess[i].lower()  
        else:
            new_hint += "-"               

    hint = new_hint

if guess_count < 3:
    print("Excellent")
elif guess_count < 5:
    print("Good")
elif guess_count <= 6:
    print("Fair")
else:
    print("Poor")

