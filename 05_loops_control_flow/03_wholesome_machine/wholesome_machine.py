AFFIRMATION = "I am capable of doing anything I put my mind to."

print("Please type the following affirmation: " + AFFIRMATION)

user_feedback = input()  # User se input lena

# Jab tak user sahi affirmation na likhe, loop chalta rahega
while user_feedback != AFFIRMATION:
    print("That was not the affirmation.")
    print("Please type the following affirmation: " + AFFIRMATION)
    user_feedback = input()  # Dobara input lena

print("That's right! :)")