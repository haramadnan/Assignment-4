import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def generate_random_numbers():
    """Generates and prints N random numbers within the specified range."""
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

# Call the function directly
generate_random_numbers()