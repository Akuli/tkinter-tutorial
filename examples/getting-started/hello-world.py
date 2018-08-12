import tkinter
from tkinter import ttk

root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text="Hello World!")
label.pack()
root.mainloop()
