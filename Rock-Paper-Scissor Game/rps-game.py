import random

choices = ["rock" , "paper" , "scissor"]


player_choice = input("Enter your choice (rock, paper, scissor): ").lower()

if player_choice not in choices:
    print("Invalid choice. Please choose from rock, paper, or scissor.")
else:
    computer_choice = random.choice(choices)

    print("Computer chose:", computer_choice)
    print("Player chose:", player_choice)

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissor") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissor" and computer_choice == "paper"):
    print("You win! 🌟")
else:
    print("Computer wins!")