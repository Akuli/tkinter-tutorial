import tkinter
from tkinter import ttk


def print_hello():
    print("hello")


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="Print hello", command=print_hello)
button.pack()
root.mainloop()
