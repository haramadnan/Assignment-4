def get_first_element(lst):
    """
    Returns the first element of the provided list.
    If the list is empty, it returns 'None'.
    """
    return lst[0] if lst else None  # Short & safe way to get first element

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


user_list = get_list()
first_element = get_first_element(user_list)

if first_element is not None:
    print("First element of the list:", first_element)
else:
    print("The list is empty, so no first element.")