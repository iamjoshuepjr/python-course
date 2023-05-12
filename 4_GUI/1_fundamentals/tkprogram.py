from tkinter import *
from tkinter import ttk

class Farm:
    def __init__(self, my_window):
        self.my_window = my_window
        self.my_window.title("Student GUI")
        
        frame = LabelFrame(self.my_window, text = "Student")
        frame.grid(row = 0, columnspan = 3, pady = 20)
        # Lables
        Label(frame, text = "Name: ").grid(row = 0, column = 0)
        Entry(frame).grid(row = 0, column = 1)

        Label(frame, text = "Password: ").grid(row = 1, column = 0)
        Entry(frame).grid(row = 1, column = 1)

        # buttons
        ttk.Button(self.my_window, text = "Save").grid(row = 2, columnspan = 2, sticky = W + E)

if __name__ == '__main__':
    my_window = Tk()
    app = Farm(my_window)
    my_window.mainloop()