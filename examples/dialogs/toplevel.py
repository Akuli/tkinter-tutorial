import tkinter
from tkinter import ttk


def display_dialog():
    dialog = tkinter.Toplevel()
    big_frame = ttk.Frame(dialog)
    big_frame.pack(fill='both', expand=True)

    label = ttk.Label(big_frame, text="Hello World")
    label.place(relx=0.5, rely=0.3, anchor='center')

    dialog.transient(root)
    dialog.geometry('300x150')
    dialog.wait_window()


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="Click me", command=display_dialog)
button.pack()
root.mainloop()
