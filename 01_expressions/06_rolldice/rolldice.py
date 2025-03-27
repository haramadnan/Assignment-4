import random  # Random module import kar rahe hain

def roll_dice(sides=6):
    """Ye function ek dice roll karega aur 1 se sides tak random number return karega"""
    return random.randint(1, sides)

def roll_two_dice():
    """Ye function do dice roll karega aur unka total return karega"""
    die1 = roll_dice()
    die2 = roll_dice()
    total = die1 + die2
    return die1, die2, total

# Directly dice roll kar rahe hain, kisi function call ki zaroorat nahi
die1, die2, total = roll_two_dice()

# Results print kar rahe hain
print(f"First die: {die1}")
print(f"Second die: {die2}")
print(f"Total of two dice: {total}")