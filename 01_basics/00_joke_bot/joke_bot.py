import random

PROMPT = "What do you want? "
JOKES = [
    "Here is a joke for you! Why don’t programmers like nature? It has too many bugs!",
    "Here is a joke for you! Why did the developer go broke? Because he used up all his cache!",
   "Here is a joke for you! Why did the bicycle fall over? Because it was two-tired!",
    "Here is a joke for you! Why do programmers prefer dark mode? Because the light attracts too many bugs!"
]
SORRY = "Sorry, I only tell jokes."

# Get user input
user_input = input(PROMPT).strip().lower()

# Check the input and respond
if user_input == "joke":
    print(random.choice(JOKES))
else:
    print(SORRY)