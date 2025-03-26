#Guess the Number Project (Computer)

import random
def guess_the_number():
    """Guess the Number Game by Computer.🖥️"""
    number = random.randint(1, 50)
    guesses_left = 5
    print("Welcome to the Guess the Number Game! ⭐")
    print("I'm thinking of a number between 1 and 50.")
    
    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number ! 🎉")
            return

        guesses_left -= 1
    
    print(f"Sorry, you've run out of guesses. The number was {number}. 😞")

if __name__ == "__main__":
    guess_the_number()
        
