import tkinter as tk

root = tk.Tk()
root.title('GUI Demo')

window_width = 700
window_height = 500

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-alpha', 0.9)
root.attributes('-topmost', 1)
root.iconbitmap('4_GUI\\1_fundamentals\\icons\\cow.ico')
root.mainloop()