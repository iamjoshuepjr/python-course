import tkinter as tk

# beginning
root = tk.Tk()

root.title('Grid')
root.iconbitmap('4_GUI\\1_fundamentals\\icons\\squared-menu.ico')

# labels
message = tk.Label(root, text = "Hello, World!")
name = tk.Label(root, text = "My name is Joshuép Jr.")

# location on screen
message.grid(row = 0, column = 0)
name.grid(row = 0, column = 2)

# ending
root.mainloop()