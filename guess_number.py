# first define a secrate number
secrate_number = 42

# define a guess number thet is unlikely to be choosen by the user like negative number

guess = -1
guess_count = 0
while guess != secrate_number:
    guess = int(input("what is your guess? "))
    guess_count = guess_count + 1
    if guess < secrate_number:
        print("higher")
    elif guess > secrate_number:
        print("lower")
    else:
        print("you got it")

print(f"it took {guess_count} guesses")
keep_playing = input("would you want to play again (yes/no)")

performance = "number of guess_count"
Excellent = "guess_count < 3"
Good      = "guess_count < 5"
Fair      = "guess_count <=6"
Poor      = "guess_count > 6"

secrate_number = 42

# define a guess number thet is unlikely to be choosen by the user like negative number
import random

keep_playing = "yes"
while keep_playing == "yes":
    secrate_number = random.randint(1,100)
    guess = -1
    guess_count = 0

    while guess != secrate_number:
        guess = int(input("what is your guess? "))
        guess_count = guess_count + 1
        if guess < secrate_number:
           print("higher")
        elif guess > secrate_number:
           print("lower")
        else:
           print("you got it")

    print(f"it took {guess_count} guesses")
    while performance != guess_count:
     if performance is guess_count < 3:
      print("excellent")
     elif performance is guess_count < 5:
          print("good")
     elif performance is guess_count <=6:
          print("fair")
else:
   print("poor")
          