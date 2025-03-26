def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Get input from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert and display the result
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")