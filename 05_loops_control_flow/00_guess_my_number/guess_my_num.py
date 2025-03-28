import random

# Random secret number generate karna
secret_number = random.randint(1, 99)
print("I am thinking of a number between 1 and 99...")

# User se pehla guess lena
guess = int(input("Enter a guess: "))

# Jab tak guess sahi na ho, loop chalta rahega
while guess != secret_number:
    if guess < secret_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

    print()  # Achhe formatting ke liye ek empty line
    guess = int(input("Enter a new guess: "))  # Naya guess lena

# Sahi guess hone par message print karna
print(f"Congrats! The number was: {secret_number}")