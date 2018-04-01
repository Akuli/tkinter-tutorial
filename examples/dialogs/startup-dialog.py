import tkinter as tk


# only use this before creating the main root window! otherwise you get
# two root windows at the same time, and that's bad, see above
def startup_dialog(labeltext):
    result = None
    rooty_dialog = tk.Tk()

    # result is left to None if the dialog is closed without clicking OK
    def on_ok():
        # usually 'result = entry.get()' creates a local variable called
        # result, but this thing makes it also appear outside on_ok()
        nonlocal result

        result = entry.get()
        rooty_dialog.destroy()   # stops rooty_dialog.mainloop()

    label = tk.Label(rooty_dialog, text=labeltext)
    label.place(relx=0.5, rely=0.3, anchor='center')
    entry = tk.Entry(rooty_dialog)
    entry.place(relx=0.5, rely=0.5, anchor='center')
    okbutton = tk.Button(rooty_dialog, text="OK", command=on_ok)
    okbutton.place(relx=0.5, rely=0.8, anchor='center')

    rooty_dialog.geometry('250x150')
    rooty_dialog.mainloop()
    # now the dialog's mainloop has stopped, so the dialog doesn't exist
    # anymore and creating another root window is ok

    return result


name = startup_dialog("Enter your name:")
if name is not None:      # the user clicked OK
    root = tk.Tk()
    label = tk.Label(root, text=("Hello %s!" % name))
    label.pack()
    root.mainloop()
