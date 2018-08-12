import tkinter
from tkinter import messagebox


def wanna_quit():
    if messagebox.askyesno("Quit", "Do you really want to quit?"):
        # the user clicked yes, let's close the window
        root.destroy()


root = tkinter.Tk()
root.protocol('WM_DELETE_WINDOW', wanna_quit)
root.mainloop()
