def find_remainder(dividend, divisor):
    """Ye function remainder calculate karega using modulus operator (%)"""
    return dividend % divisor  # Remainder find kar raha hai

# User se input lena
dividend = int(input("Enter the dividend: "))  # Jis number ko divide karna hai
divisor = int(input("Enter the divisor: "))  # Jis se divide karna hai

# Remainder calculate karna
remainder = find_remainder(dividend, divisor)

# Output show karna
print(f"The remainder when {dividend} is divided by {divisor} is: {remainder}")