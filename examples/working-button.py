import tkinter as tk

def print_hello():
    print("hello")

root = tk.Tk()
button = tk.Button(root, text="Print hello", command=print_hello)
button.pack()
root.mainloop()
