import tkinter
from tkinter import ttk, messagebox


def do_hello_world():
    messagebox.showinfo("Important Message", "Hello World!")


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="Click me", command=do_hello_world)
button.pack()
root.mainloop()
