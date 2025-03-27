def get_list_from_user():
    """
    Prompts the user to enter values one by one and stores them in a list.
    Returns the final list when the user presses Enter without typing anything.
    """
    lst = []  # Empty list to store user inputs
    while True:
        val = input("Enter a value (or press Enter to stop): ")  
        if not val:  # Stop when user presses Enter
            break
        lst.append(val)  # Add value to the list
    return lst


user_list = get_list_from_user()
print("Here's the list:", user_list)