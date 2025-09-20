import math
# areas of square, rectangle and circle

# ask for the informatiom

side = float(input(" what is the length of the side of the square? "))

# if you input directly, it will show error because you cant multiply two strings
# convert the string to interger by using the function int. however, int will only allow for integers.
# Therefore to allow for numbers with decimal points, float function becomes handy.
# assuming the lenght of the side is 5.2

# calculate the area

area = side * side

# display the value
print(f" the area of the square is: {area}")

# notice that the area of the square on display in the terminal is in many decimal
# places, this can be shortened to required decimal places by using format strings.
# assuming you want it in 4 decimal places

print(f" the area of the square is: {area:.4f}")
# with this it cahnges to 27.0400 on display.

# following the same process for a rectangle

# ask for the information

length = float(input(" what is the length of the rectangle? "))
width =  float(input(" what is the width of the rectangle? "))

# assuming the length is 7 and the width is 6

# calculate the area
area_rectangle = length * width


print(f" the area of the rectangle is: {area_rectangle}")


# for area of a circle 
# the equation is pi * radius squared

radius = float(input(" the radius of the circle is? "))
circle_area = 3.14 * radius **2
print(f" the area of the circle is: {circle_area}")

# note that to get the exact value of pi, i could import the math library at the beginning.
# with this in mind,

circle_area = math.pi * radius **2
print(f" the area of the circle is: {circle_area}")

# need to express the values in centimeters and square centimeters.
# note that a centimeter is 1/100th of a meter
# a square centemeter is 1/10,000th of a square meter. 

side = float(input(" what is the length of the side of the square (in cm)? "))

area = side * side

print(f" the area of the square is: {area:.4f} cm^2")

area_in_meters = area/10000

print(f" the area of the square in meters is: {area_in_meters:.4f} m^2")

# for rectangle

length = float(input(" what is the length of the rectangle (in cm)? "))
width =  float(input(" what is the width of the rectangle (in cm)? "))

area_rectangle = length * width

rectangle_area_meters = area_rectangle/10000

print(f" the area of the rectangle is: {area_rectangle} cm^2")

print(f" the area of the rectangle in meters is: {rectangle_area_meters} m^2")

# for circle

radius = float(input(" the radius of the circle is (in cm? "))
circle_area = 3.14 * radius **2

circle_area_meters = circle_area/10000

print(f" the area of the circle is: {circle_area} cm^2")

print(f" the area of the circle in meters is: {circle_area_meters} m^2")