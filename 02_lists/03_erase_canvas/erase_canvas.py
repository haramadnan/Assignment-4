import tkinter as tk

def erase_canvas():
    """Canvas ke saare drawings ko erase karega"""
    canvas.delete("all")  # Canvas ke andar sab kuch remove karega

# Tkinter window create karna
root = tk.Tk()
root.title("Erase Canvas Example")

# Canvas create karna
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Example drawing (Ek line aur rectangle draw karna)
canvas.create_line(50, 50, 350, 50, width=3, fill="blue")
canvas.create_rectangle(100, 100, 300, 200, fill="red")

# Erase button create karna
erase_button = tk.Button(root, text="Erase Canvas", command=erase_canvas)
erase_button.pack(pady=10)

# Tkinter loop run karna
root.mainloop()