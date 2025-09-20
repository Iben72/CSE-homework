# In ln 24 col 24, the word "looking" was added after the adjective to make it read "furry looking cat".
# Also, in ln 26 col 71, the word "angrily" was introduced after the verb "jump".
print("please enter the following information ")

adjective = input("adjective ")
print(adjective)

animal = input("animal ")
print(animal)

verb1 = input("verb1 ")
print(verb1)

exclamation =input("exclamation ")
print(exclamation)


verb2=input("verb2 ")
print(verb2)

verb3 =input("verb3 ")
print(verb3)

print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f"{adjective} looking {animal} {verb1} down the hallway. \"{exclamation.title()}\" I yelled. But all")
print(f"I could think to do was to {verb2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb3} angrily,")
print(f"right in front of my family.")









adjective = "furry"
print(adjective)

animal = "cat"
print(animal)

verb1 = "walking"
print(verb1)

exclamation = "waoooh!"
print(exclamation)

verb2 = "shout"
print(verb2)

verb3 = "jump"
print(verb3)

print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f"{adjective} looking {animal} {verb1} down the hallway. \"{exclamation.title()}\" I yelled. But all")
print(f"I could think to do was to {verb2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb3} angrily,")
print(f"right in front of my family.")



# import the local library

import locale

money_value = 1245.60

currency_symbol ='RS'

locale_value = 'pt_BR.UTF-8'

# set the local parameters and convert the value

locale.setlocale(locale.LC_ALL, locale_value)
money_formated =locale.currency(money_value,
grouping = True,
symbol = currency_symbol)


