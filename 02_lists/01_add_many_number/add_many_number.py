def add_numbers():
    """Yeh function user se multiple numbers input lekar unka sum calculate karega"""
    
    # User se input lena (comma-separated numbers)
    numbers = input("Enter numbers separated by spaces: ")
    
    # Numbers ko split karke list me convert karna, aur integer banake sum lena
    total = sum(map(float, numbers.split()))
    
    # Result print karna
    print(f"Sum of given numbers: {total}")

# Function call karke program run karna
add_numbers()