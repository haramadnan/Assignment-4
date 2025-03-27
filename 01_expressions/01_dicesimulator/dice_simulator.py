import random  # Random module import kar rahe hain taake random number generate ho

def roll_dice():
    """Ye function ek dice ko roll karega aur random number return karega"""
    return random.randint(1, 6)  # 1 se 6 tak ka random number generate kar raha hai

while True:
    input("Press Enter to roll the dice...")  # User se enter press karne ka keh raha hai
    dice_value = roll_dice()  # Dice roll kar rahe hain
    print(f"You rolled: {dice_value}")  # Output mein dice ka number show kar rahe hain

    play_again = input("Roll again? (yes/no): ").strip().lower()  # User se pooch rahe hain dobara khelna hai ya nahi
    if play_again != "yes":  # Agar user "yes" nahi likhta to loop break kar dena
        print("Thanks for playing!")
        break  # Loop stop kar dena