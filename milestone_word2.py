secret_word = "jonah"

guess = input("What is your guess? ").lower()

guess_count = 0





while True:
    guess = input("what is your guess? ") .lower()
    
    if guess == secret_word:
       print("congratulations! you guessed it!")
    
    else:
        print("your guess was not correct")

    print(f"it took you {guess_count} guesses")
    
    

    
    
    
    
    