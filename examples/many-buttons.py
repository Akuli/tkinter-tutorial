import functools
import tkinter as tk


def print_hello_number(number):
    print("hello", number)


root = tk.Tk()
for i in range(1, 6):
    button = tk.Button(root, text="Hello %d" % i,
                       command=functools.partial(print_hello_number, i))
    button.pack()

root.mainloop()
