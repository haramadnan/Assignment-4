phonebook = {}  # Create empty phonebook

def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    """
    global phonebook
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

def print_phonebook():
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

def lookup_numbers():
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])

# Program Execution
read_phone_numbers()
print_phonebook()
lookup_numbers()