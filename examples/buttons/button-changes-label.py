import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text='Hello')
label.pack()


def change_text():
    if label['text'] == 'Hello':
        label['text'] = 'World'
    else:
        label['text'] = 'Hello'


button = ttk.Button(big_frame, text="Click here", command=change_text)
button.pack()
root.mainloop()
