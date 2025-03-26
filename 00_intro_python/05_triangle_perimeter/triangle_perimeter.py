def triangle_perimeter(a, b, c):
    return a + b + c

# Get input from the user
side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))

# Calculate and display the perimeter
perimeter = triangle_perimeter(side1, side2, side3)
print(f"The perimeter of the triangle is: {perimeter}")