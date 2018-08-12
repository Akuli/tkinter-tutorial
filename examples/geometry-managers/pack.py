import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="This stretches")
label = ttk.Label(big_frame, text="This doesn't stretch")
statusbar = ttk.Label(big_frame, text="This is a status bar", relief='sunken')

statusbar.pack(side='bottom', fill='x')
button.pack(side='left', fill='both', expand=True)
label.pack(side='left')

root.title("Pack Test")
root.geometry('300x150')
root.mainloop()
