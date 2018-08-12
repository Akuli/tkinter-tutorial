import tkinter
from tkinter import ttk


def display_dialog():
    root2 = tkinter.Tk()      # BAD! NO!!
    big_frame2 = ttk.Frame(root2)
    big_frame2.pack(fill='both', expand=True)

    ttk.Label(big_frame2, text="Hello World").place(relx=0.5, rely=0.3, anchor='center')
    root2.mainloop()


root = tkinter.Tk()
button = ttk.Button(root, text="Click me", command=display_dialog)
button.pack()
root.mainloop()
