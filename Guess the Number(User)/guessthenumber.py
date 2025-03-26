#Guess the Number Game (User)


import random
print("Welcome to the Guess the Number Game! 💭")
print("Guess the number between 1 and 50!")

#Generate Random Number
random_number = random.randint(1, 50)

while True:
    guess = int(input("Enter your guess number: "))

    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number! 🌟")
        break