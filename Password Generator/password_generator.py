import random 
import string

#Password generation function

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#User Input

try:
     password_length = int(input("Enter the desired password length: ")) 
     if password_length < 1:
         print("Password length must be at least 1.") 
     else:
 # Generate Password password = generate_password(password_length) 
      print("Generated Password:", generate_password(password_length)) 
except ValueError:
    print("Invalid input! Please enter a valid number.")