import math


def compute_area_square(side):
    """Compute the area of a square given the length of its side."""
    return side * side

def compute_area_rectangle(length, width):
    """Compute the area of a rectangle given its length and width."""
    return length * width

def compute_area_circle(radius):
    """Compute the area of a circle given its radius."""
    import math
    return math.pi * radius * radius

shape = ""

while shape != "quit":
    shape = input("Enter the shape (square, rectangle, circle in Meters) or 'quit' to exit: ").strip().lower()
    
    if shape == "square":
        side = float(input("Enter the length of the side: "))
        area = compute_area_square(side)
        print(f"The area of the square is: {area}")
        
    elif shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = compute_area_rectangle(length, width)
        print(f"The area of the rectangle is: {area}")
        
    elif shape == "circle":
        radius = float(input("Enter the radius: "))
        area = compute_area_circle(radius)
        print(f"The area of the circle is: {area}")
        
    elif shape == "quit":
        print("Exiting the program.")
        
    else:
        print("Invalid shape. Please enter 'square', 'rectangle', 'circle', or 'quit'.")
