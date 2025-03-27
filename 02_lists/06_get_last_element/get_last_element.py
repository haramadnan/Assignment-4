def get_last_element(lst):
    """
    Returns the last element of the provided list.
    If the list is empty, it returns 'None'.
    """
    return lst[-1] if lst else None  # Safe way to get last element

def get_list():
    """
    Takes multiple inputs from the user to create a list.
    Returns the list when the user presses Enter without typing anything.
    """
    lst = []
    while True:
        elem = input("Enter an element (or press Enter to stop): ")
        if not elem:  # Stop when user presses enter
            break
        lst.append(elem)
    return lst

# 🚀 Program Execution (Without main function)
user_list = get_list()
last_element = get_last_element(user_list)

if last_element is not None:
    print("Last element of the list:", last_element)
else:
    print("The list is empty, so no last element.")