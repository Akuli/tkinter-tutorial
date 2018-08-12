import time
import tkinter
from tkinter import ttk


# this must return soon after starting this
def change_text():
    label['text'] = time.asctime()

    # now we need to run this again after one second, there's no better
    # way to do this than timeout here
    root.after(1000, change_text)


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text='0')
label.pack()

change_text()      # don't forget to actually start it :)

root.geometry('200x200')
root.mainloop()
