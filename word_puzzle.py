secret_word = "jonah"

hint = "-----"

correct_letter = "letter.upper()"
wrong_letter   = "letter.lower()"
absent_letter  = "-"

guess = input(f"the hint is: {hint} ")
guess1 = input("what is your guess? ")

while True:
    print(f"your guess is: {secret_word}")
    print ("you got it")
    exit

    if absent_letter == "-":
        print("absent_letter")
    elif wrong_letter == "letter.lower()":
        print("wrong_letter")
    else:
        print("correct_letter")

        break

