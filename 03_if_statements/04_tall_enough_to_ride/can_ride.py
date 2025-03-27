MINIMUM_HEIGHT = 50  # Minimum height required to ride (in arbitrary units)

def can_ride(height):
    """Checks if the given height meets the minimum requirement to ride."""
    return height >= MINIMUM_HEIGHT

while True:
    height = input("How tall are you? ")  # Ask the user for their height
    
    if height == "":  # Stop if the user presses Enter without input
        break

    height = float(height)  # Convert input to a float
    if can_ride(height):
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")