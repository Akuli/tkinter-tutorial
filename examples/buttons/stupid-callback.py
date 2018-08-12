import time
import tkinter
from tkinter import ttk


def ok_callback():
    print("hello")


def stupid_callback():
    time.sleep(5)


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button1 = ttk.Button(big_frame, text="This is OK", command=ok_callback)
button1.pack()
button2 = ttk.Button(big_frame, text="This sucks", command=stupid_callback)
button2.pack()

root.mainloop()
