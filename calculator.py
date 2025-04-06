# Create a calculator.py program that calculates the area of one of the following shapes: Square, Rectangle, Triangle, Circle
# The program should present a menu for the user to choose which shape to calculate, then ask them for the appropriate values (side, length, width, etc.).
# Then, it should calculate the area and print it out.

# Here are the area equations for each shape:

# Square	area = side**2
# Rectangle	area = length∗width
# Triangle	area = (height∗base)/2
# Circle	area = π ∗ (radius)**2
 
# Note: For pi π in the area of a circle, feel free to either use 3.14 or import the math module to use the math.pi variable.

# The output should look something like this:

# 1) Triangle
# 2) Rectangle
# 3) Square
# 4) Circle
# 5) Quit

# Which shape: 1
# Base: 5
# Height: 6
# The area is 15

print("1 - Triangle\n" 
"2 - Rectangle\n" 
"3 - Square\n" 
"4 - Circle\n" 
"5 - Quit")

shape = float(input('Please enter a shape for which you want to calculate Equation (1-5): '))


if shape == 1: # Triangle
    height = float(input("Enter height: "))
    base = float(input("Enter base: "))
    area = (height*base)/2
    print(area)
elif shape == 2: # Rectangle
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))               
    area = length*width
    print(area)
elif shape == 3: # Square
    side = float(input("Enter side: "))
    area = side**2
    print(area)
elif shape == 4: # Circle
    radius = float(input("Enter radius: "))
    area = 3.14 * (radius)**2
    print(area)
elif shape == 5: # Quit
    print("Quit")
else:
    print("Wrong input.")