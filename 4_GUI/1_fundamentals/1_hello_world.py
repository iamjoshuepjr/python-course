import tkinter as tk

# creating a window object
root = tk.Tk()

# label
message = tk.Label(root, text = "Hello, World!")

# showing it onto the screen
message.pack()

# window object dimensions
root.geometry(f'300x200+80+80')

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()