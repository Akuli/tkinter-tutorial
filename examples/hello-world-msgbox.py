import tkinter as tk
from tkinter import messagebox


def do_hello_world():
    messagebox.showinfo("Important Message", "Hello World!")


root = tk.Tk()
button = tk.Button(root, text="Click me", command=do_hello_world)
button.pack()
root.mainloop()
