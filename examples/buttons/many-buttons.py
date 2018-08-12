import functools
import tkinter
from tkinter import ttk


def print_hello_number(number):
    print("hello", number)


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

for i in range(1, 6):
    button = ttk.Button(big_frame, text="Hello %d" % i,
                        command=functools.partial(print_hello_number, i))
    button.pack()

root.mainloop()
