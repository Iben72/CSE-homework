# creat your first def function

def greet():
    print("Hello, welcome to Python!")

# call the function by typing

greet()

#add a parameter so that the function can greet someone by name

def greet_person(name):
    print(f"hello, {name}! welcome to Python.")

# now call it with different names

greet_person("Ibene")
greet_person("Alice")

# make the function return something.

def add_numbers(a, b):
    return a + b
    
# now call it
result = add_numbers(5, 7)
print(f"The sum is: {result}")

# add default values; this allows the function to run even if you don't pass arguments

def greet_user(name="Guest"):
    print(f"Hello, {name}! Welcome to Python.")

# call it without passing an argument
greet_user()
greet_user("John")

# add a function that takes multiple parameters and returns a formatted string

def format_message(name, age, city):
    return f"{name} is {age} years old and lives in {city}."
# call it with different values
message = format_message("Alice", 30, "New York")
print(message)


# add a function that takes a variable number of arguments
def sum_all(*args):
    return sum(args)
# call it with different numbers of arguments
total = sum_all(1, 2, 3, 4, 5)
print(f"The total sum is: {total}")

def print_double(value):
    double_value = value*2
    print(double_value)

print_double(12)
print_double(8)
print_double(52)