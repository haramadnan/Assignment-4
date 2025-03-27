def energy_calculator(mass):
    """Ye function Einstein ka formula E = mc² use karke energy calculate karega"""
    c = 299_792_458  # Speed of light in meters per second (m/s)
    energy = mass * c**2  # Formula: E = mc²
    return energy

# User se mass input lena (kilograms mein)
mass = float(input("Enter mass in kilograms: "))  

# Energy calculate karna
energy = energy_calculator(mass)

# Output show karna
print(f"Energy (E) = {energy} Joules")