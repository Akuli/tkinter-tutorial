import tkinter as tk


root = tk.Tk()

button = tk.Button(root, text="This stretches")
label = tk.Label(root, text="This doesn't stretch")
statusbar = tk.Label(root, text="This is a status bar", relief='sunken')

button.grid(row=0, column=0, sticky='nswe')
label.grid(row=0, column=1)
statusbar.grid(row=1, column=0, columnspan=2, sticky='we')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.title("Grid Test")
root.geometry('300x150')
root.mainloop()
