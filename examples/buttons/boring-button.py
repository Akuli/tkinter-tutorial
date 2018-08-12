import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text="This is a button test.")
label.pack()
button = ttk.Button(big_frame, text="Click me!")
button.pack()

root.title("Button Test")
root.geometry('200x100')
root.minsize(150, 50)
root.mainloop()
