MAX_LENGTH = 3  # Maximum allowed length of the list

def shorten(lst):
    """
    Removes and prints elements from the list until its length is MAX_LENGTH or less.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove last element
        print(last_elem)  # Print the removed element

def get_list_from_user():
    """
    Prompts the user to enter elements one by one and returns the final list.
    """
    lst = []
    while True:
        elem = input("Enter an element (or press Enter to stop): ")
        if not elem:  # Stop when user presses Enter
            break
        lst.append(elem)  # Add element to list
    return lst

user_list = get_list_from_user()
shorten(user_list)