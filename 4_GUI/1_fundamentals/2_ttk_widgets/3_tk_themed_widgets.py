import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Labels')
root.iconbitmap('4_GUI\\1_fundamentals\\icons\\squared-menu.ico')
tk.Label(root, text = 'Classic Label').pack()
ttk.Label(root, text = 'Themed Label').pack()
root.geometry(f'300x200+80+80')

root.mainloop()