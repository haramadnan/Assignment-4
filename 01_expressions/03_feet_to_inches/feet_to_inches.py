def feet_to_inches(feet):
    """Ye function feet ko inches mein convert karega"""
    return feet * 12  # 1 foot = 12 inches

# User se input lena (feet mein)
feet = float(input("Enter length in feet: "))

# Conversion karna
inches = feet_to_inches(feet)

# Output show karna
print(f"{feet} feet is equal to {inches} inches.")