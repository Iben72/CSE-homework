secret_word = "jonah"
guess = input("What is your guess? ").lower()
guess_count = 0


hint = "-" * len(secret_word)

while True:
    print(f"The hint is: {hint}")
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if guess == secret_word:
        print("Congratulations! You got it!")
        print(f"it took you {guess_count} guesses")
        break

    new_hint = ""
    for i in range(len(secret_word)):
        if i < len(guess):
            
            if guess[i] == secret_word[i]:
                new_hint += guess[i].upper()  # Correct letter in correct position
            elif guess[i] in secret_word:
                new_hint += guess[i].lower() 
            else:
                new_hint = "_"
        else:
             new_hint = "_"
    else:
               print("sorry, the guess must have the same number of letters as the secret word")                                              # Correct letter in wrong poselse:
    new_hint += "-"               # Letter not in the word
        

    hint = new_hint
