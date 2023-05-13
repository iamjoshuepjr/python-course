# To make the application more interactive, 
# the widgets need to respond to events such as: 
# + Mouse clicks 
# + Key presses 
# This requires assigning a callback function to a specific event

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')

# callback function
def button_clicked():
    print('Button cliked')

button = ttk.Button(root, text = 'Click Me', command = button_clicked)
button.pack()

def select(option):
    print(option)

ttk.Button(root, text = 'Rock', command = lambda: select('Rock')).pack()
ttk.Button(root, text = 'Paper', command = lambda: select('Paper')).pack()
ttk.Button(root, text = 'Scissors', command = lambda: select('Scissors')).pack()
root.mainloop()