import tkinter as tk


def display_dialog():
    dialog = tk.Toplevel()

    label = tk.Label(dialog, text="Hello World")
    label.place(relx=0.5, rely=0.3, anchor='center')

    dialog.transient(root)
    dialog.geometry('300x150')
    dialog.wait_window()


root = tk.Tk()
button = tk.Button(root, text="Click me", command=display_dialog)
button.pack()
root.mainloop()
