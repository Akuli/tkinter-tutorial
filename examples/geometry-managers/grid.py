import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="This stretches")
label = ttk.Label(big_frame, text="This doesn't stretch")
statusbar = ttk.Label(big_frame, text="This is a status bar", relief='sunken')

button.grid(row=0, column=0, sticky='nswe')
label.grid(row=0, column=1)
statusbar.grid(row=1, column=0, columnspan=2, sticky='we')

big_frame.grid_rowconfigure(0, weight=1)
big_frame.grid_columnconfigure(0, weight=1)

root.title("Grid Test")
root.geometry('300x150')
root.mainloop()
