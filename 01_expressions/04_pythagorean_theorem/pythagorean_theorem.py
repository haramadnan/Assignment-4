import math  # Math module use kar rahe hain taake sqrt() function mile

def find_hypotenuse(a, b):
    """Ye function Pythagorean theorem se hypotenuse calculate karega"""
    return math.sqrt(a*2 + b*2)  # Formula: c = sqrt(a² + b²)

# User se inputs lena
a = float(input("Enter the first side (a): "))
b = float(input("Enter the second side (b): "))

# Hypotenuse calculate karna
c = find_hypotenuse(a, b)

# Output show karna
print(f"The hypotenuse (c) is: {c:.2f}")