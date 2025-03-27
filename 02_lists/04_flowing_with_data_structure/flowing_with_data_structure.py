def add_three_copies(my_list, data):
    """Adds three copies of the data to the list."""
    my_list.extend([data] * 3)  


message = input("Enter a message to copy: ")
my_list = []
print("List before:", my_list)

add_three_copies(my_list, message)

print("List after:", my_list)