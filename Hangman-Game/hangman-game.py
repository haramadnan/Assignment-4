import random
words = ["enum", "python" , "vs code" , "game" , "colab"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game ! ⭐")
print("_" * len(word))

while attempts > 0:
    guess = input("\n Guess the letters : ").lower()

    if len(guess) !=1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You have already guessed this letter.")
        continue
    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess !")
    else:
        print("Wrong Guess !")
        attempts -= 1
        print(f"You have {attempts} attempts left.")

    word_display = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print(" ".join(word_display))  # Print with spaces

    if "_" not in word_display:
        print("Congratulations! You guessed the word correctly.")
        break

else:
    print(f"Sorry, you ran out of attempts. The word was '{word}'.")


